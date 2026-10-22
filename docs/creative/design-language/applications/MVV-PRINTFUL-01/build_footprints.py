from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
R=Path(__file__).parent;B=R.parent/'CAR-WRONG-04/blanks';F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
for s in json.loads((R/'layout-specs.json').read_text()):
 id=s['design_id'];a=Image.open(R/'assets'/f'{id}-v1.png').convert('RGBA').crop(s['bbox_alpha16']);out=Image.new('RGB',(1240,755),'#f5f3ed');d=ImageDraw.Draw(out);d.text((20,15),id+' / controlled footprint comparison',font=ImageFont.truetype(F,25),fill='black');d.text((20,52),'1717 Ivory; same top anchor; provisional local geometry',font=ImageFont.truetype(F,18),fill='black')
 for j,factor in enumerate([.85,1]):
  w=s['visible_inches']['width']*factor;h=w*a.height/a.width;bg=Image.new('RGBA',(602,602),'#fff4d9');bg.alpha_composite(Image.open(B/'Ivory.png').convert('RGBA'));sw=round(w*17.8);sh=round(sw*a.height/a.width);bg.alpha_composite(a.resize((sw,sh),Image.Resampling.LANCZOS),(round(303-sw/2),round(97+s['visible_inches']['top']*17.8)));out.paste(bg.convert('RGB'),(15+j*615,90));d.text((30+j*615,705),f'{"Compact" if j==0 else "Selected"}: {w:.2f} x {h:.2f} in',font=ImageFont.truetype(F,20),fill='black')
 out.save(R/'assets'/f'{id}-footprints.jpg',quality=86)
