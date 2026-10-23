from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib
R=Path(__file__).parent;A=R.parent.parent
old=Image.open(A/'NOSTALGIA-ND-01/assets/A-heritage-v3.png').convert('RGBA');new=Image.open(R/'NDA-balanced-master.png').convert('RGBA')
assert old.size==new.size
import numpy as np
x=np.array(old.crop((280,280,1050,940)));y=np.array(new.crop((280,230,1050,890)));assert np.max(abs(x[x[:,:,3]>0].astype(int)-y[x[:,:,3]>0].astype(int)))<=1
assert old.crop((0,0,1315,230)).tobytes()==new.crop((0,0,1315,230)).tobytes()
assert old.crop((0,940,1315,1197)).tobytes()==new.crop((0,940,1315,1197)).tobytes()
bbox=old.getchannel('A').point(lambda a:255 if a>=16 else 0).getbbox();a=new.crop(bbox)
w=8.75;h=w*a.height/a.width
c=Image.new('RGBA',(1800,2400));c.alpha_composite(a.resize((round(w*150),round(h*150)),Image.Resampling.LANCZOS),(round((12-w)*75),300));c.save(R/'NDA-balanced-12x16.png',dpi=(150,150))
f='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def label(im,xy,s,n=20):ImageDraw.Draw(im).text(xy,s,font=ImageFont.truetype(f,n),fill='#263739')
def shirt(canvas):
 b=Image.new('RGBA',(602,602),'#fff4d9');b.alpha_composite(Image.open(A/'CAR-WRONG-04/blanks/Ivory.png').convert('RGBA'));p=canvas.resize((214,285),Image.Resampling.LANCZOS);b.alpha_composite(p,(196,97));return b
board=Image.new('RGB',(1244,740),'#f5f3ed');label(board,(20,15),'N-D-A / balanced internal spacing',25);label(board,(20,52),'Same lettering, original illustration pixels, 8.75-inch width and lowered top anchor',17)
for j,im in enumerate([Image.open(R.parent/'layouts/N-D-A-lowered-12x16.png').convert('RGBA'),c]):board.paste(shirt(im),(10+j*622,85))
label(board,(25,695),'Before: tighter below the bowl');label(board,(647,695),'Revised: balanced breathing room');board.save(R/'shirt-comparison.jpg',quality=93)
board=Image.new('RGB',(1244,690),'#fff4d9')
for j,im in enumerate([old,new]):
 p=im.resize((600,546),Image.Resampling.LANCZOS);board.paste(p,(10+j*622,75),p)
label(board,(20,20),'Before',25);label(board,(642,20),'Revised / illustration moved up',25);board.save(R/'detail-comparison.jpg',quality=93)
(R/'specs.json').write_text(json.dumps(dict(width_inches=w,height_inches=h,top_inches=2,left_inches=(12-w)/2,canvas_inches=[12,16],anchor='Print-canvas origin, not neckline',illustration_shift_native_pixels=-50,source_bbox=bbox,master_sha256=hashlib.sha256((R/'NDA-balanced-master.png').read_bytes()).hexdigest(),provider_status='pending'),indent=2)+'\n')
print('Pixel checks passed; footprint',w,h)
