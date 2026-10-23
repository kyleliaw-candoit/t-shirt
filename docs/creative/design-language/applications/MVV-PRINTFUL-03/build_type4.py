from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageCms
import json,hashlib
R=Path(__file__).parent;P=R.parent;old=P/'MVV-PRINTFUL-02';source=P/'MVV-PRINTFUL-01'
s=next(x for x in json.loads((source/'layout-specs.json').read_text()) if x['design_id']=='Type-Led-4')
a=Image.open(source/'assets/Type-Led-4-v1.png').convert('RGBA').crop(s['bbox_alpha16']);w=10.5;h=w*a.height/a.width;top=2.;left=.75
assert top+h<=16
c=Image.new('RGBA',(1800,2400));c.alpha_composite(a.resize((round(w*150),round(h*150)),Image.Resampling.LANCZOS),(round(left*150),round(top*150)))
c.save(R/'layouts/MVV3-Type-Led-4-12x16.png',dpi=(150,150),icc_profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes())
bg=Image.new('RGBA',(602,602),'#fff4d9');bg.alpha_composite(Image.open(P/'CAR-WRONG-04/blanks/Ivory.png').convert('RGBA').resize((602,602)));sw=round(w*17.8);sh=round(h*17.8);bg.alpha_composite(a.resize((sw,sh),Image.Resampling.LANCZOS),(round(303-sw/2),round(97+top*17.8)));bg.convert('RGB').save(R/'assets/Type-Led-4-large.jpg',quality=92)
out=Image.new('RGB',(1204,650),'white');out.paste(Image.open(old/'assets/Type-Led-4-shirt.jpg'),(0,40));out.paste(bg.convert('RGB'),(602,40));d=ImageDraw.Draw(out);f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20);d.text((20,10),'Previous: medium / 9 in wide',font=f,fill='black');d.text((622,10),'Revised: large / 10.5 in wide',font=f,fill='black');out.save(R/'assets/Type-Led-4-before-after.jpg',quality=92)
sp=dict(design_id='Type-Led-4',footprint='large',visible_inches=dict(width=w,height=round(h,4),left=left,top=top,bottom=round(top+h,4)),blank='Comfort Colors 1717',color='Ivory',method='DTG front',artwork_source='../MVV-PRINTFUL-01/assets/Type-Led-4-v1.png',native_ppi=round(a.width/w,2),export_ppi=150,anchor='Print area origin; not neckline',mockup_size='Unknown',provider_check='pending',production_resolution='Higher-detail master required; preview resampling adds no detail',canvas_sha256=hashlib.sha256((R/'layouts/MVV3-Type-Led-4-12x16.png').read_bytes()).hexdigest())
(R/'Type-Led-4-spec.json').write_text(json.dumps(sp,indent=2)+'\n');print(sp)
