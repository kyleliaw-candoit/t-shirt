"""Measured layout revision only. Reuse round01 art unchanged; upsampling adds no detail."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageCms
import json,hashlib,io,os
R=Path(__file__).parent;OLD=R.parent/'MVV-PRINTFUL-01';B=R.parent/'CAR-WRONG-04/blanks/Ivory.png'
S=json.loads((OLD/'layout-specs.json').read_text());WIDTHS=[8.5,8,8,9,10.5,9,10.5,10.5,8.5,9]
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
def label(im,xy,t):ImageDraw.Draw(im).text(xy,t,font=font,fill='#26372d')
def shirt(a,w,h,t):
 bg=Image.new('RGBA',(602,602),'#fff4d9');bg.alpha_composite(Image.open(B).convert('RGBA').resize((602,602)));sw=round(w*17.8);sh=round(h*17.8);bg.alpha_composite(a.resize((sw,sh),Image.Resampling.LANCZOS),(round(303-sw/2),round(97+t*17.8)));return bg.convert('RGB')
specs=[];shirts=[]
for s,w in zip(S,WIDTHS):
 id=s['design_id'];p=OLD/'assets'/f'{id}-v1.png';a=Image.open(p).convert('RGBA');a=a.crop(s['bbox_alpha16']);h=w*a.height/a.width;t=s['visible_inches']['top']+.5;l=(12-w)/2
 assert h+t<=16 and w<=12
 c=Image.new('RGBA',(1800,2400));c.alpha_composite(a.resize((round(w*150),round(h*150)),Image.Resampling.LANCZOS),(round(l*150),round(t*150)))
 out=R/'layouts'/f'MVV2-{id}-12x16.png';tmp=out.with_suffix('.writing');c.save(tmp,format='PNG',dpi=(150,150),icc_profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes());os.replace(tmp,out)
 new=shirt(a,w,h,t);new.save(R/'assets'/f'{id}-shirt.jpg',quality=92);shirts.append(new)
 board=Image.new('RGB',(1204,660),'white');board.paste(Image.open(OLD/'assets'/f'{id}-shirt.jpg'),(0,40));board.paste(new,(602,40));label(board,(20,10),f'{id} — previous {s["visible_inches"]["width"]:g} in');label(board,(622,10),f'Revised {w:g} in / lowered 0.5 in');board.save(R/'assets'/f'{id}-before-after.jpg',quality=91)
 s2=dict(design_id=id,artwork_source=f'../MVV-PRINTFUL-01/assets/{id}-v1.png',master_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),blank=s['blank'],color=s['color'],method=s['method'],footprint='large' if id in ['YIF-F','Fashion-1D-F'] else ('retained wide strip' if id=='C3B' else 'medium'),visible_inches=dict(width=w,height=round(h,4),left=l,top=t,bottom=round(t+h,4)),previous_visible_inches=s['visible_inches'],native_ppi=round(a.width/w,2),export_ppi=150,canvas_inches=[12,16],canvas_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),width_percent_flat_garment={z:round(w/d*100,1) for z,d in [('S',18.25),('L',22),('2XL',26)]},anchor='Print area origin; not neckline',mockup_size='Unknown',production_resolution_status='Native >=150' if a.width/w>=150 else 'Higher-detail production master required; resampling is preview only')
 specs.append(s2)
board=Image.new('RGB',(1500,700),'white');label(board,(15,8),'Revised footprints / provisional local geometry / 1717 Ivory')
for i,(s,im) in enumerate(zip(specs,shirts)):
 x=i%5*300;y=40+i//5*330;board.paste(im.resize((300,300)),(x,y));label(board,(x+8,y+300),s['design_id'])
board.save(R/'assets/revised-overview.jpg',quality=92)
(R/'layout-specs.json').write_text(json.dumps(specs,indent=2)+'\n')
print([(s['design_id'],s['visible_inches'],s['native_ppi']) for s in specs])
