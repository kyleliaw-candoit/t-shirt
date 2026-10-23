from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).parent;A=R.parent
board=Image.new('RGB',(1244,740),'#f5f3ed');d=ImageDraw.Draw(board);f='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
d.text((20,15),'N-D-A / typography exploration',font=ImageFont.truetype(f,25),fill='#263739')
d.text((20,52),'Same 8.75-inch width and lowered top anchor / provisional local garment geometry',font=ImageFont.truetype(f,17),fill='#263739')
for j,path in enumerate([A/'NON-MVV-PLACEMENT-01/NDA-spacing-02/NDA-balanced-master.png',R/'serif-script-trial.png']):
 a=Image.open(path).convert('RGBA');a=a.crop(a.getchannel('A').point(lambda x:255 if x>=16 else 0).getbbox());w=round(8.75*17.8);h=round(w*a.height/a.width)
 b=Image.new('RGBA',(602,602),'#fff4d9');b.alpha_composite(Image.open(A/'CAR-WRONG-04/blanks/Ivory.png').convert('RGBA'));b.alpha_composite(a.resize((w,h),Image.Resampling.LANCZOS),(round(303-w/2),133));board.paste(b,(10+j*622,85))
 d.text((25+j*622,695),['Approved slab serif','Trial: soft serif + handwritten script'][j],font=ImageFont.truetype(f,20),fill='#263739')
board.save(R/'shirt-comparison.jpg',quality=93)
