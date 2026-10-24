from pathlib import Path
import hashlib,json
import cv2,numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageCms
from scipy.ndimage import distance_transform_edt
from skimage.metrics import structural_similarity
R=Path(__file__).parent;A=R.parent;src=A/'NOSTALGIA-ND-01/assets/B-artifact-v1.png';model=R/'models/FSRCNN_x4.pb'
assert hashlib.sha256(model.read_bytes()).hexdigest()=='5c68d18db561aed8ead4ffedf1b897ea615baaf60ebf6c35f8e641f8fa4a21bf'
im=Image.open(src).convert('RGBA');bbox=(129,75,1061,1250);a=im.crop(bbox);x=np.array(a);al=x[:,:,3];mask=al>=128;ground=np.array([81,79,76],np.float32)
rgb=np.uint8(np.clip(x[:,:,:3]*(al[:,:,None]/255)+ground*(1-al[:,:,None]/255),0,255));nearest=distance_transform_edt(~mask,return_distances=False,return_indices=True);ext=rgb[nearest[0],nearest[1]]
cv2.setNumThreads(4);sr=cv2.dnn_superres.DnnSuperResImpl_create();sr.readModel(str(model));sr.setModel('fsrcnn',4)
pred=cv2.cvtColor(sr.upsample(cv2.cvtColor(ext,cv2.COLOR_RGB2BGR)),cv2.COLOR_BGR2RGB)
w=8.25;h=w*1175/932;target=(round(w*300),round(h*300));neural=cv2.resize(pred,target,interpolation=cv2.INTER_AREA);base=cv2.resize(ext,target,interpolation=cv2.INTER_CUBIC)
colour=np.uint8(np.clip(.65*neural.astype(float)+.35*base.astype(float),0,255));outmask=cv2.resize(al,target,interpolation=cv2.INTER_CUBIC)>=128;y=np.dstack([colour,np.uint8(outmask)*255]);y[~outmask,:3]=0;b=Image.fromarray(y)
canvas=Image.new('RGBA',(3600,4800));canvas.alpha_composite(b,(round(1.875*300),600));icc=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes();canvas.save(R/'NDB-restored-300ppi.png',dpi=(300,300),icc_profile=icc)
def flat(im):
 bg=Image.new('RGBA',im.size,'#514f4c');bg.alpha_composite(im);return bg.convert('RGB')
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
board=Image.new('RGB',(1200,820),'#eeeae2');d=ImageDraw.Draw(board)
for j,art in enumerate([a,b]):
 p=flat(art);p.thumbnail((550,720));board.paste(p,(25+j*600,65));d.text((25+j*600,20),['Approved source','Restoration candidate'][j],font=f,fill='black')
board.save(R/'whole-comparison.jpg',quality=94)
# matched physical detail panels: header, faces, lower caption and outer frame.
old=a.resize(target,Image.Resampling.LANCZOS)
for name,box in [('header',(280,40,1480,340)),('faces',(800,650,2000,1250)),('payoff',(500,2640,1700,3040)),('frame',(0,1000,450,1600))]:
 parts=[flat(z.crop(box)) for z in [old,b]];page=Image.new('RGB',(parts[0].width*2,parts[0].height+45),'#eeeae2')
 for j,p in enumerate(parts):page.paste(p,(j*p.width,45))
 ImageDraw.Draw(page).text((15,10),'Source enlarged | Restored — same print-size region',font=f,fill='black');page.save(R/(name+'-detail.jpg'),quality=95)
checked=Image.open(R/'NDB-restored-300ppi.png').convert('RGBA');z=np.array(checked);bounds=checked.getchannel('A').getbbox();assert checked.size==(3600,4800);assert set(np.unique(z[:,:,3]))=={0,255};assert bounds[0]>0 and bounds[1]>0 and bounds[2]<3600 and bounds[3]<4800
before=np.array(flat(a));after=np.array(flat(b.resize(a.size,Image.Resampling.LANCZOS)))
result=dict(source=str(src.relative_to(A)),source_native_ppi=932/8.25,method='FSRCNN x4, 65% learned restoration / 35% bicubic, final-size reduction; Pepper-specific near-opaque ink appearance; binary alpha',visible_inches=dict(width=w,height=h,left=1.875,top=2,bottom=2+h),actual_bounds_inches=[v/300 for v in bounds],export_ppi=300,canvas_pixels=[3600,4800],alpha_values=np.unique(z[:,:,3]).tolist(),roundtrip_ssim=float(structural_similarity(before,after,channel_axis=2,data_range=255)),roundtrip_mae=float(np.abs(before.astype(float)-after.astype(float)).mean()),sha256=hashlib.sha256((R/'NDB-restored-300ppi.png').read_bytes()).hexdigest(),file_bytes=(R/'NDB-restored-300ppi.png').stat().st_size,status='visual review pending; not proof of recovered native detail')
(R/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
