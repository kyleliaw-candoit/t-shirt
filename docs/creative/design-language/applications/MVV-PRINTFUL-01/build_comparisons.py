from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
R=Path(__file__).parent;S=R.parents[2]/'assets/R012'; F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
specs=json.loads((R/'layout-specs.json').read_text())
for sp in specs:
 id=sp['design_id'];p=S/f'R012-{id}-LOCKED.png'
 if not p.exists():p=S/f'R012-{id}-LOCKED-SOURCE.png'
 out=Image.new('RGB',(1500,850),'#f5f3ed');d=ImageDraw.Draw(out);d.text((25,20),id+' / archived approval and production derivative',font=ImageFont.truetype(F,26),fill='black')
 old=Image.open(p).convert('RGB');old.thumbnail((830,690));out.paste(old,(15,100));new=Image.open(R/'assets'/f'{id}-shirt.jpg');new.thumbnail((620,620));out.paste(new,(870,100));d.text((880,740),'1717 Ivory / measured layout',font=ImageFont.truetype(F,20),fill='black');d.text((880,775),'Local geometry provisional',font=ImageFont.truetype(F,18),fill='black');out.save(R/'assets'/f'{id}-comparison.jpg',quality=88)
