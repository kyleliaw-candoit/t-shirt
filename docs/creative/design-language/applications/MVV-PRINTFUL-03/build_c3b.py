"""Measured arrangement of unchanged graphic and generated caption; no pixel repainting."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageCms
import json,hashlib
R=Path(__file__).parent;P=R.parent
s=next(x for x in json.loads((P/'MVV-PRINTFUL-01/layout-specs.json').read_text()) if x['design_id']=='C3B')
g=Image.open(P/'MVV-PRINTFUL-01/assets/C3B-v1.png').convert('RGBA').crop(s['bbox_alpha16'])
t=Image.open(R/'assets/C3B-caption.png').convert('RGBA');t=t.crop(t.getchannel('A').point(lambda x:255 if x>=16 else 0).getbbox())
gw=10.5;gh=gw*g.height/g.width;tw=8.8;th=tw*t.height/t.width;gap=.4;top=2.75;total=gh+gap+th
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',23);spec=[];shirts=[];details=[]
for variant in ['above','below']:
 ty=top if variant=='above' else top+gh+gap;gy=top+th+gap if variant=='above' else top
 c=Image.new('RGBA',(1800,2400));c.alpha_composite(g.resize((round(gw*150),round(gh*150)),Image.Resampling.LANCZOS),(round((12-gw)/2*150),round(gy*150)));c.alpha_composite(t.resize((round(tw*150),round(th*150)),Image.Resampling.LANCZOS),(round((12-tw)/2*150),round(ty*150)))
 path=R/'layouts'/f'MVV3-C3B-{variant}-12x16.png';c.save(path,dpi=(150,150),icc_profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes())
 bg=Image.new('RGBA',(602,602),'#fff4d9');bg.alpha_composite(Image.open(P/'CAR-WRONG-04/blanks/Ivory.png').convert('RGBA').resize((602,602)))
 for a,w,h,y in [(g,gw,gh,gy),(t,tw,th,ty)]:
  aw=round(w*17.8);ah=round(h*17.8);bg.alpha_composite(a.resize((aw,ah),Image.Resampling.LANCZOS),(round(303-aw/2),round(97+y*17.8)))
 bg.convert('RGB').save(R/'assets'/f'C3B-{variant}-shirt.jpg',quality=93);shirts.append(bg.convert('RGB'))
 crop=c.crop((round(.75*150),round(top*150),round(11.25*150),round((top+total)*150)));d=Image.new('RGBA',crop.size,'#fff4d9');d.alpha_composite(crop);d.convert('RGB').save(R/'assets'/f'C3B-{variant}-detail.jpg',quality=93);details.append(d.convert('RGB'))
 spec.append(dict(variant=variant,caption='ANTIQUE MALL MOOD SWINGS',graphic_inches=dict(width=gw,height=gh,left=.75,top=gy),caption_inches=dict(width=tw,height=th,left=(12-tw)/2,top=ty),gap_inches=gap,overall_top=top,overall_height=total,overall_bottom=top+total,native_ppi_graphic=g.width/gw,native_ppi_caption=t.width/tw,canvas_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),anchor='Print area origin, not neckline',mockup_geometry='provisional'))
board=Image.new('RGB',(1204,1030),'white');d=ImageDraw.Draw(board)
for i,v in enumerate(['above','below']):
 x=i*602;d.text((x+20,12),f'Copy {v}',font=font,fill='black');board.paste(shirts[i],(x,50));im=details[i];im.thumbnail((560,330));board.paste(im,(x+(602-im.width)//2,680))
board.save(R/'assets/C3B-above-below.jpg',quality=93)
(R/'C3B-specs.json').write_text(json.dumps(spec,indent=2)+'\n');print(spec)
