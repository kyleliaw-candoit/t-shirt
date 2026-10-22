"""Measured compositing only; source pixels are not repainted or cleaned."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import hashlib, json
R=Path(__file__).parent
B=R.parent.parent/'CAR-WRONG-04/blanks'
COLORS={'Pepper':'#514f4c','Ivory':'#fff4d9','Blue Jean':'#707e8d','Moss':'#6b7053'}
SOURCE=R/'assets/TE-quiet-v1.png'
im=Image.open(SOURCE).convert('RGBA')
bbox=im.getchannel('A').point(lambda a:255 if a>=16 else 0).getbbox()
art=im.crop(bbox)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def txt(im,xy,s,size=20):
    ImageDraw.Draw(im).text(xy,s,font=ImageFont.truetype(FONT,size),fill='#263739')
def page(w,h,title,sub):
    im=Image.new('RGB',(w,h),'#f5f3ed');txt(im,(24,20),title,27);txt(im,(24,62),sub,16);return im
def put(im,a,xy):im.paste(a,xy,a)
def shirt(color,width):
    bg=Image.new('RGBA',(602,602),COLORS[color]);bg.alpha_composite(Image.open(B/(color.replace(' ','-')+'.png')).convert('RGBA').resize((602,602)))
    w=round(width*17.8);h=round(w*art.height/art.width)
    bg.alpha_composite(art.resize((w,h),Image.Resampling.LANCZOS),(round(303-w/2),round(97+1.5*17.8)))
    return bg
specs=[]
for variant,width in [('compact',7.5),('medium',8.5)]:
    height=width*art.height/art.width;left=(12-width)/2
    assert left>=0 and 1.5+height<=16
    c=Image.new('RGBA',(1800,2400));c.alpha_composite(art.resize((round(width*150),round(height*150)),Image.Resampling.LANCZOS),(round(left*150),225));c.save(R/'layouts'/f'TE-quiet-{variant}-12x16.png',dpi=(150,150))
    specs.append({'variant':variant,'selected':variant=='medium','concept':'T-E','family':'DLF-002 boundary: typography-led quiet vignette','color':'Pepper','blank':'Comfort Colors 1717','method':'DTG front','visible_inches':{'width':width,'height':round(height,4),'left':left,'top':1.5},'anchor':'12x16 print canvas origin, NOT physical neckline','native_bbox_alpha16':bbox,'native_effective_ppi':round(art.width/width,1),'master_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'reference_garment_size':'unknown','geometry':'provisional round04; 17.8px/in, center x303, print origin y97 on 602px blank','nominal_width_percent':{s:round(width/v*100,1) for s,v in [('S',18.25),('L',22),('2XL',26)]}})
(R/'layout-specs.json').write_text(json.dumps(specs,indent=2)+'\n')
out=page(1280,790,'T-E quiet variant — compact / medium','Same artwork, Pepper blank and top anchor; local geometry provisional.')
for j,(v,w) in enumerate([('Compact',7.5),('Medium',8.5)]):
    put(out,shirt('Pepper',w),(20+j*625,100));txt(out,(40+j*625,725),f'{v} / {w} in wide / top 1.5 in',20)
out.save(R/'assets/footprint-comparison.png')
out=page(1280,1430,'Four approved garment colors','Selected medium 8.5 in width; unchanged ivory artwork. Screen colors approximate.')
for j,color in enumerate(COLORS):
    x=20+(j%2)*625;y=100+(j//2)*650;put(out,shirt(color,8.5),(x,y));txt(out,(x+20,y+608),color,20)
out.save(R/'assets/color-comparison.png')
out=page(650,770,'T-E / Quiet typography','1717 / Pepper / provisional geometry; photographed size unknown')
put(out,shirt('Pepper',8.5),(24,100));txt(out,(30,720),'8.5 in wide; print-canvas top 1.5 in',20);out.save(R/'assets/selected-shirt.png')
out=page(1280,790,'T-E — two distinct visual treatments','Left: approved Playful. Right: new quiet typography for review. Same Pepper blank.')
approved=Image.open(R.parent/'assets/TE-shirt.png').convert('RGBA').crop((24,100,626,702))
put(out,approved,(20,100));put(out,shirt('Pepper',8.5),(645,100));txt(out,(40,725),'A / Approved Playful / 8 in wide',20);txt(out,(665,725),'B / Quiet typography / 8.5 in wide',20);out.save(R/'assets/paired-review.png')
detail=Image.new('RGBA',art.size,COLORS['Pepper']);detail.alpha_composite(art);detail.convert('RGB').save(R/'assets/artwork-detail.png')
print(json.dumps(specs,indent=2))
