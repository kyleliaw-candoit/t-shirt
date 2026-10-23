"""Measured layouts only; original generated alpha and artwork remain unchanged."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageCms
import json,hashlib,io,os
R=Path(__file__).parent; B=R.parent/'CAR-WRONG-04/blanks'; F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
IDS=['B2','A1','A3','YIF-M','YIF-F','C2','C3B','Fashion-1D-F','Type-Led-3','Type-Led-4']
WIDTHS=[6.25,5.5,5.5,7,7.25,6.5,10.5,7.25,6,7.25]
def text(im,pos,s,size=18):ImageDraw.Draw(im).text(pos,s,fill='#25352b',font=ImageFont.truetype(F,size))
def save(im,p):
 b=io.BytesIO();im.save(b,format='PNG',dpi=(150,150),icc_profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()); t=p.with_suffix('.writing');t.write_bytes(b.getvalue());os.replace(t,p);Image.open(p).verify()
specs=[]; shirts={}
for id,w in zip(IDS,WIDTHS):
 p=R/'assets'/f'{id}-v1.png'
 if not p.exists():continue
 a=Image.open(p).convert('RGBA');histo=a.getchannel('A').histogram();bbox=a.getchannel('A').point(lambda x:255 if x>=16 else 0).getbbox();a=a.crop(bbox);h=w*a.height/a.width;top=1.5 if id!='C3B' else 2.25;left=(12-w)/2
 c=Image.new('RGBA',(1800,2400));c.alpha_composite(a.resize((round(w*150),round(h*150)),Image.Resampling.LANCZOS),(round(left*150),round(top*150)));path=R/'layouts'/f'MVV-{id}-12x16.png';save(c,path)
 bg=Image.new('RGBA',(602,602),'#fff4d9');bg.alpha_composite(Image.open(B/'Ivory.png').convert('RGBA').resize((602,602)));sw=round(w*17.8);sh=round(sw*a.height/a.width);bg.alpha_composite(a.resize((sw,sh),Image.Resampling.LANCZOS),(round(303-sw/2),round(97+top*17.8)));shirts[id]=bg
 detail=Image.new('RGBA',a.size,'#fff4d9');detail.alpha_composite(a);detail.thumbnail((900,1000));detail.convert('RGB').save(R/'assets'/f'{id}-detail.jpg',quality=92)
 bg.convert('RGB').save(R/'assets'/f'{id}-shirt.jpg',quality=92)
 specs.append(dict(design_id=id,blank='Comfort Colors 1717',method='DTG front',color='Ivory',canvas_inches=[12,16],visible_inches=dict(width=w,height=round(h,4),left=left,top=top),bbox_alpha16=bbox,master_size=list(Image.open(p).size),native_ppi=round(a.width/w,2),alpha_nonzero_below240_percent=round(sum(histo[1:240])/sum(histo[1:])*100,2),master_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),canvas_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),width_percent_flat_garment={s:round(w/d*100,1) for s,d in [('S',18.25),('L',22),('2XL',26)]},anchor='Print area origin; not neckline',mockup_size='Unknown',local_geometry='Provisional round04, 17.8px/in, center303, origin97'))
for part in range(2):
 out=Image.new('RGB',(1810,1430),'#f5f3ed');text(out,(25,16),f'MVV production review / {part+1} of 2',28);text(out,(25,57),'1717 Ivory / DTG front / local shirt geometry provisional; reference garment size unknown',18)
 for k,id in enumerate(IDS[part*5:part*5+5]):
  if id not in shirts:continue
  x=(k%3)*602;y=100+(k//3)*650;out.paste(shirts[id].convert('RGB'),(x,y));sp=next(s for s in specs if s['design_id']==id);text(out,(x+20,y+605),f'{id} / {sp["visible_inches"]["width"]} x {sp["visible_inches"]["height"]:.2f} in',20)
 out.save(R/'assets'/f'review-{part+1}.jpg',quality=92)
(R/'layout-specs.json').write_text(json.dumps(specs,indent=2)+'\n');print([(s['design_id'],s['native_ppi'],s['visible_inches']) for s in specs])
