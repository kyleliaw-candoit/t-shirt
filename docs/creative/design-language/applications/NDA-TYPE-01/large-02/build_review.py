from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib
R=Path(__file__).parent;A=R.parent.parent
src=R/'balanced-master.png';im=Image.open(src).convert('RGBA');bbox=im.getchannel('A').point(lambda x:255 if x>=16 else 0).getbbox();a=im.crop(bbox)
w=10.5;h=w*a.height/a.width;left=(12-w)/2;top=2
assert top+h<16
c=Image.new('RGBA',(1800,2400));c.alpha_composite(a.resize((round(w*150),round(h*150)),Image.Resampling.LANCZOS),(round(left*150),300));c.save(R/'NDA-large-balanced-12x16.png',dpi=(150,150))
f='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def text(im,xy,s,n=20):ImageDraw.Draw(im).text(xy,s,font=ImageFont.truetype(f,n),fill='#263739')
def shirt(art,width):
 art=art.crop(art.getchannel('A').point(lambda x:255 if x>=16 else 0).getbbox());pw=round(width*17.8);ph=round(pw*art.height/art.width)
 b=Image.new('RGBA',(602,602),'#fff4d9');b.alpha_composite(Image.open(A/'CAR-WRONG-04/blanks/Ivory.png').convert('RGBA'));b.alpha_composite(art.resize((pw,ph),Image.Resampling.LANCZOS),(round(303-pw/2),133));return b
board=Image.new('RGB',(1244,740),'#f5f3ed');text(board,(20,15),'N-D-A / balanced spacing + large footprint',25);text(board,(20,52),'Comfort Colors 1717 / Ivory / lowered top anchor retained / local geometry provisional',17)
for j,(art,width) in enumerate([(Image.open(R.parent/'serif-script-trial.png').convert('RGBA'),8.75),(im,10.5)]):board.paste(shirt(art,width),(10+j*622,85))
text(board,(25,695),'Previous trial / 8.75 in wide');text(board,(647,695),'Revised / 10.5 in wide');board.save(R/'shirt-comparison.jpg',quality=94)
detail=Image.new('RGBA',im.size,'#fff4d9');detail.alpha_composite(im);detail.convert('RGB').save(R/'artwork-detail.jpg',quality=94)
# Compare spacing alone at constant width separately from enlargement.
board=Image.new('RGB',(1244,740),'#f5f3ed');text(board,(20,15),'Spacing check / both at 10.5 inches wide',25)
for j,art in enumerate([Image.open(R.parent/'serif-script-trial.png').convert('RGBA'),im]):board.paste(shirt(art,10.5),(10+j*622,85))
text(board,(25,695),'Before / lower gap too tight');text(board,(647,695),'Revised / balanced optical gaps');board.save(R/'spacing-comparison.jpg',quality=92)
s=dict(width_inches=w,height_inches=h,left_inches=left,top_inches=top,bottom_inches=top+h,anchor='Print-canvas origin, not neckline',native_effective_ppi=a.width/w,canvas_inches=[12,16],export_ppi=150,native_bbox=bbox,master_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),canvas_sha256=hashlib.sha256((R/'NDA-large-balanced-12x16.png').read_bytes()).hexdigest(),width_percent_nominal_flat={k:round(w/v*100,1) for k,v in [('S',18.25),('L',22),('2XL',26)]},provider_status='Revised design not yet verified in Printful')
(R/'specs.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s))
