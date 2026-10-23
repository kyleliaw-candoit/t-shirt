"""Source-faithful vector tracing / FSRCNN restoration. No generative redesign.
Usage: python repair.py --model /absolute/path/FSRCNN_x4.pb [--ids ID ...]
Model URL + SHA in MODEL below; dependencies in requirements.txt.
"""
from pathlib import Path
import argparse,hashlib,json,io,tempfile,gzip
import numpy as np
import cv2,vtracer,cairosvg
from PIL import Image,ImageDraw,ImageFont,ImageCms
from scipy.ndimage import distance_transform_edt,binary_erosion
from skimage.metrics import structural_similarity
R=Path(__file__).resolve().parent; OLD=R.parent/'MVV-PRINTFUL-01'
MODEL='5c68d18db561aed8ead4ffedf1b897ea615baaf60ebf6c35f8e641f8fa4a21bf'
VECTORS={'Fashion-1D-F','Type-Led-3','Type-Led-4'}
IVORY=np.array([255,244,217],np.float32)
ICC=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
FONT=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
def flatten(a):
 x=np.array(a,dtype=np.float32);al=x[:,:,3:]/255
 return Image.fromarray(np.uint8(np.clip(x[:,:,:3]*al+IVORY*(1-al),0,255)))
def board(a,b,id,w):
 out=Image.new('RGB',(1200,650),'white');d=ImageDraw.Draw(out)
 for i,im in enumerate([a,b]):
  im=flatten(im);im.thumbnail((570,570));out.paste(im,(i*600+(600-im.width)//2,60));d.text((i*600+15,15),('Approved source' if i==0 else 'Repair candidate')+' — '+id,font=FONT,fill='black')
 out.save(R/'review'/f'{id}-comparison.jpg',quality=92)
def shirt(a,s):
 bg=Image.new('RGBA',(602,602),'#fff4d9');bg.alpha_composite(Image.open(R.parent/'CAR-WRONG-04/blanks/Ivory.png').convert('RGBA').resize((602,602)));v=s['visible_inches'];im=a.resize((round(v['width']*17.8),round(v['height']*17.8)),Image.Resampling.LANCZOS);bg.alpha_composite(im,(round(303-im.width/2),round(97+v['top']*17.8)));return bg.convert('RGB')
def palette_save(im,path):
 # Lossless PNG container; 255-color quantization is separately measured below.
 x=np.array(im); mask=x[:,:,3]>0
 q=im.convert('RGB').quantize(colors=255,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE)
 idx=np.array(q,dtype=np.uint8)+1;idx[~mask]=0
 out=Image.fromarray(idx,'P');out.putpalette([0,0,0]+q.getpalette()[:765]);out.info['transparency']=0
 out.save(path,dpi=(300,300),icc_profile=ICC,optimize=True)
 recon=np.asarray(out.convert('RGB'));err=np.abs(recon.astype(float)-x[:,:,:3])[mask]
 return float(err.mean()),float(np.percentile(err,99))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--model',required=True);ap.add_argument('--ids',nargs='*');args=ap.parse_args()
 assert hashlib.sha256(Path(args.model).read_bytes()).hexdigest()==MODEL
 cv2.setNumThreads(4);sr=cv2.dnn_superres.DnnSuperResImpl_create();sr.readModel(args.model);sr.setModel('fsrcnn',4)
 old={s['design_id']:s for s in json.loads((OLD/'layout-specs.json').read_text())};spec={s['design_id']:s for s in json.loads((R.parent/'MVV-PRINTFUL-02/layout-specs.json').read_text())};spec['Type-Led-4']=json.loads((R.parent/'MVV-PRINTFUL-03/Type-Led-4-spec.json').read_text())
 results=json.loads((R/'repair-results.json').read_text()) if args.ids and (R/'repair-results.json').exists() else []
 results=[x for x in results if x['design_id'] not in (args.ids or [])]
 for id,s in spec.items():
  if id=='C3B' or (args.ids and id not in args.ids):continue
  a=Image.open(OLD/'assets'/f'{id}-v1.png').convert('RGBA').crop(old[id]['bbox_alpha16']);x=np.array(a);alpha=x[:,:,3];mask=alpha>=128
  # Composite near-opaque ink against the approved Ivory reference to retain its appearance.
  rgb=np.asarray(flatten(a)).copy();rgb[~mask]=0
  v=s['visible_inches'];target=(round(v['width']*300),round(v['height']*300))
  if id in VECTORS:
   # Trace a compact palette; preserve existing letter contours and intentional holes.
   src=Image.fromarray(np.dstack([rgb,np.uint8(mask)*255]));q=src.convert('RGB').quantize(colors=64,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE).convert('RGBA');q.putalpha(Image.fromarray(np.uint8(mask)*255))
   with tempfile.TemporaryDirectory() as td:
    tmp=Path(td)/'trace.png';q.save(tmp)
    vtracer.convert_image_to_svg_py(str(tmp),str(Path(td)/'trace.svg'),colormode='color',hierarchical='stacked',mode='spline',filter_speckle=0,color_precision=8,layer_difference=4,corner_threshold=60,length_threshold=3.5,max_iterations=10,splice_threshold=45,path_precision=3)
    svg=(Path(td)/'trace.svg').read_bytes()
   (R/'vectors'/f'{id}.svgz').write_bytes(gzip.compress(svg,mtime=0));raw=cairosvg.svg2png(bytestring=svg,output_width=target[0],output_height=target[1]);b=Image.open(io.BytesIO(raw)).convert('RGBA');y=np.array(b);y[:,:,3]=np.where(y[:,:,3]>=128,255,0);b=Image.fromarray(y)
   method='VTracer spline paths; 64-tone palette; unfiltered distress; compressed SVG, no embedded bitmap'
  else:
   # Extend nearest interior RGB into transparent space before SR to prevent black/ivory fringe.
   nearest=distance_transform_edt(~mask,return_distances=False,return_indices=True);extended=rgb[nearest[0],nearest[1]]
   pred=sr.upsample(cv2.cvtColor(extended,cv2.COLOR_RGB2BGR));pred=cv2.cvtColor(pred,cv2.COLOR_BGR2RGB)
   neural=cv2.resize(pred,target,interpolation=cv2.INTER_AREA)
   base=cv2.resize(extended,target,interpolation=cv2.INTER_CUBIC)
   colour=np.clip(.65*neural.astype(float)+.35*base.astype(float),0,255).astype(np.uint8)
   smooth=cv2.resize(alpha,target,interpolation=cv2.INTER_CUBIC);outmask=smooth>=128
   b=Image.fromarray(np.dstack([colour,np.uint8(outmask)*255]));method='FSRCNN x4; 65% learned reconstruction + 35% bicubic; final-size reduction'
  # All candidate ink is opaque; fully clear exterior/counters. No faded halo.
  y=np.array(b);y[y[:,:,3]==0,:3]=0;b=Image.fromarray(y)
  canvas=Image.new('RGBA',(3600,4800));canvas.alpha_composite(b,(round(v['left']*300),round(v['top']*300)))
  path=R/'layouts'/f'MVV4-{id}-300ppi.png';qe,q99=palette_save(canvas,path)
  # Compare at original source resolution on the approved Ivory, not enlarged pixels.
  before=np.asarray(flatten(a));after=np.asarray(flatten(b.resize(a.size,Image.Resampling.LANCZOS)));mae=float(np.abs(before.astype(float)-after.astype(float)).mean());ssim=structural_similarity(before,after,channel_axis=2,data_range=255)
  full=np.array(Image.open(path).convert('RGBA'));bb=Image.fromarray(full[:,:,3]).getbbox();inter=binary_erosion(mask,iterations=3);vals=alpha[inter]
  results.append(dict(design_id=id,method=method,source_native_ppi=round(a.width/v['width'],2),export_ppi=300,canvas_pixels=[3600,4800],approved_inches=v,actual_ink_bounds_inches=[round(z/300,4) for z in bb],alpha_values=np.unique(full[:,:,3]).tolist(),source_interior_alpha_below200_percent=round(float(np.mean(vals<200))*100,3),roundtrip_rgb_mae=round(mae,3),roundtrip_ssim=round(float(ssim),5),palette_ink_channel_mae=round(qe,3),palette_ink_channel_error_p99=q99,file_bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),status='candidate; visual review required; not proof of recovered native detail'))
  board(a,b,id,v['width']);shirt(b,s).save(R/'review'/f'{id}-shirt.jpg',quality=92)
  # Pixel detail pairs around the centre: same physical region, 300-PPI render.
  src=a.resize(target,Image.Resampling.LANCZOS);cx,cy=target[0]//2,target[1]//2;box=(max(0,cx-300),max(0,cy-250),cx+300,cy+250);detail=Image.new('RGB',(1200,550),'white');detail.paste(flatten(src.crop(box)),(0,50));detail.paste(flatten(b.crop(box)),(600,50));ImageDraw.Draw(detail).text((10,10),'Source enlarged | Repair — same 2-inch region at 300 PPI',font=FONT,fill='black');detail.save(R/'review'/f'{id}-detail.jpg',quality=95)
  print(id,results[-1],flush=True)
 (R/'repair-results.json').write_text(json.dumps(results,indent=2)+'\n')
main()
