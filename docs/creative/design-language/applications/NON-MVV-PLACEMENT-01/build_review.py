"""Translate approved padded exports only; no regeneration or resampling of print pixels."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, hashlib
R=Path(__file__).parent; A=R.parent
rows=[('T-E-A','NEXT-03-2026-10-21/layouts/TE-compact-12x16.png','Pepper',8,7.8358),('T-E-B','NEXT-03-2026-10-21/cue-revisions-04/layouts/TE-cue04-12x16.png','Pepper',8.5,6.3447),('N-A','NEXT-03-2026-10-21/cue-revisions-04/layouts/NA-cue04-12x16.png','Ivory',8,9.9783),('N-D-A','NOSTALGIA-ND-01/layouts/A-compact-12x16.png','Ivory',8.75,8.3794),('N-D-B','NOSTALGIA-ND-01/layouts/B-compact-12x16.png','Pepper',8.25,10.401)]
(R/'layouts').mkdir(exist_ok=True);(R/'assets').mkdir(exist_ok=True)
f='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def text(im,xy,s,n=20):ImageDraw.Draw(im).text(xy,s,font=ImageFont.truetype(f,n),fill='#263739')
def shirt(canvas,color):
 b=Image.new('RGBA',(602,602),'#514f4c' if color=='Pepper' else '#fff4d9');b.alpha_composite(Image.open(A/'CAR-WRONG-04/blanks'/f'{color}.png').convert('RGBA'))
 p=canvas.resize((round(12*17.8),round(16*17.8)),Image.Resampling.LANCZOS);b.alpha_composite(p,(round(303-p.width/2),97));return b.convert('RGB')
specs=[]
for ident,src,color,w,h in rows:
 old=Image.open(A/src).convert('RGBA');assert old.size==(1800,2400)
 assert old.getchannel('A').getbbox()[3]+75<=2400
 new=Image.new('RGBA',old.size);new.paste(old,(0,75))
 assert new.crop((0,75,1800,2400)).tobytes()==old.crop((0,0,1800,2325)).tobytes()
 dest=R/'layouts'/f'{ident}-lowered-12x16.png';new.save(dest,dpi=(150,150))
 check=Image.open(dest).convert('RGBA');assert check.tobytes()==new.tobytes()
 page=Image.new('RGB',(1244,740),'#f5f3ed');text(page,(20,15),ident+' / placement comparison',25)
 text(page,(20,52),'Comfort Colors 1717 / '+color+' / same artwork and footprint; local geometry provisional',17)
 for j,im in enumerate([old,new]):page.paste(shirt(im,color),(10+j*622,85))
 text(page,(25,695),'Before: top 1.5 in');text(page,(647,695),'Revised: top 2.0 in (+0.5 in down)')
 page.save(R/'assets'/f'{ident}-comparison.jpg',quality=92)
 specs.append(dict(id=ident,source='../'+src,source_sha256=hashlib.sha256((A/src).read_bytes()).hexdigest(),layout=str(dest.relative_to(R)),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),garment='Comfort Colors 1717',color=color,method='DTG front',canvas_inches=[12,16],export_ppi=150,translation_pixels=[0,75],old_top_inches=1.5,visible_inches=dict(width=w,height=h,left=(12-w)/2,top=2,bottom=round(2+h,4)),anchor='Print-canvas origin, NOT neckline',pixel_preservation='Exact RGBA translation verified; zero clipping',provider_status='Revised placement not yet checked in Printful'))
(R/'layout-specs.json').write_text(json.dumps(specs,indent=2)+'\n')
print(json.dumps([{'id':x['id'],'bytes':(R/x['layout']).stat().st_size,'bottom':x['visible_inches']['bottom']} for x in specs]))
