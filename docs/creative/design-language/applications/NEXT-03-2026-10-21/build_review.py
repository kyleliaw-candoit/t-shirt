"""Measured layout only. No generated artwork is repainted or cleaned here.

Run with Pillow. Uses CAR-WRONG-04 cached blanks and provisional transform;
actual photographed garment size/physical neckline geometry remain unknown.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json,hashlib
ROOT=Path(__file__).parent
BLANKS=ROOT.parent/'CAR-WRONG-04/blanks'
COLORS={'Pepper':'#514f4c','Ivory':'#fff4d9','Blue Jean':'#707e8d','Moss':'#6b7053'}
DESIGNS=json.loads((ROOT/'designs.json').read_text())
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def text(im,xy,s,size=20):ImageDraw.Draw(im).text(xy,s,font=ImageFont.truetype(FONT,size),fill='#263739')
def page(w,h,title,sub):
    im=Image.new('RGB',(w,h),'#f5f3ed');text(im,(24,20),title,27);text(im,(24,62),sub,16);return im
def save(im,target,**kwargs):
    tmp=target.with_name(target.stem+'-writing.png');im.save(tmp,**kwargs);tmp.replace(target)
sources={};specs=[]
for d in DESIGNS:
    p=ROOT/'assets'/d['source'];im=Image.open(p).convert('RGBA')
    bbox=im.getchannel('A').point(lambda a:255 if a>=16 else 0).getbbox()
    a=im.crop(bbox);sources[d['id']]=a
    for variant,width in zip(['compact','medium'],d['widths']):
        h=width*a.height/a.width;left=(12-width)/2
        spec={'id':d['id'],'concept':d['concept'],'family':d['family'],'source':d['source'],'variant':variant,'selected':variant==d['selected_variant'],'color':d['color'],'canvas_inches':[12,16],'visible_bounds_inches':{'left':left,'top':d['top'],'width':width,'height':round(h,4)},'anchor':'12x16 print-canvas origin, NOT neckline','native_bbox_alpha16':bbox,'native_effective_ppi':round(a.width/width,1),'master_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'mockup_reference_size':'unknown','local_geometry':'provisional round04: 17.8px/in, center x=303, print origin y=97 on a 602px blank','width_percent_nominal_flat':{s:round(width/v*100,1) for s,v in [('S',18.25),('L',22),('2XL',26)]}}
        assert left>=0 and d['top']+h<=16
        canvas=Image.new('RGBA',(1800,2400));r=a.resize((round(width*150),round(h*150)),Image.Resampling.LANCZOS)
        canvas.alpha_composite(r,(round(left*150),round(d['top']*150)))
        save(canvas,ROOT/'layouts'/f'{d["id"]}-{variant}-12x16.png',dpi=(150,150));specs.append(spec)
def selected(d):return next(x for x in specs if x['id']==d['id'] and x['selected'])
def shirt(d,color,width,scale=1):
    base=Image.new('RGBA',(602,602),COLORS[color]);base.alpha_composite(Image.open(BLANKS/(color.replace(' ','-')+'.png')).convert('RGBA').resize((602,602)))
    a=sources[d['id']];w=round(width*17.8);h=round(w*a.height/a.width)
    base.alpha_composite(a.resize((w,h),Image.Resampling.LANCZOS),(round(303-w/2),round(97+d['top']*17.8)))
    return base.resize((round(602*scale),round(602*scale)),Image.Resampling.LANCZOS)
def put(im,a,xy):im.paste(a,xy,a)
im=page(1880,800,'Three concepts — selected local shirt treatments','1717 / DTG front / garment geometry provisional; photographed size unknown')
for j,d in enumerate(DESIGNS):
    sp=selected(d);b=sp['visible_bounds_inches'];x=15+j*620
    put(im,shirt(d,d['color'],b['width']),(x,105))
    text(im,(x+20,724),f"{d['concept']} / {d['title']} / {d['color']}",20)
    text(im,(x+20,758),f"{b['width']} x {b['height']} in visible art; top {d['top']} in",16)
save(im,ROOT/'assets/review-board.png')
im=page(1280,1570,'Compact / medium — controlled within each concept','Same art, blank, color and top anchor; width and height change together.')
for row,d in enumerate(DESIGNS):
    for col,(variant,w) in enumerate(zip(['compact','medium'],d['widths'])):
        x=25+col*625;y=105+row*480
        text(im,(x,y),f"{d['concept']} / {variant} / {w} in wide",20)
        put(im,shirt(d,d['color'],w,.7),(x+70,y+30))
save(im,ROOT/'assets/footprint-comparison.png')
im=page(1420,1370,'Four approved garment colors — unchanged inks','Screen comparisons support selection, not precise physical color matching.')
for row,d in enumerate(DESIGNS):
    for col,color in enumerate(COLORS):
        x=15+col*350;y=100+row*415
        text(im,(x+12,y),f"{d['concept']} / {color}",19);put(im,shirt(d,color,selected(d)['visible_bounds_inches']['width'],.56),(x,y+35))
save(im,ROOT/'assets/color-comparison.png')
im=page(1880,980,'Artwork detail — selected masters','Garment-color viewing grounds; source masters retain alpha. Native detail and edge opacity need separate review.')
for j,d in enumerate(DESIGNS):
    x=35+j*620;y=120;a=sources[d['id']];scale=min(540/a.width,800/a.height)
    a=a.resize((round(a.width*scale),round(a.height*scale)),Image.Resampling.LANCZOS)
    ImageDraw.Draw(im).rectangle((x-15,y-15,x+555,940),fill=COLORS[d['color']]);put(im,a,(x+(540-a.width)//2,y))
save(im,ROOT/'assets/artwork-detail.png')
# Each selected concept also has a directly reviewable whole-shirt image.
for d in DESIGNS:
    im=page(650,770,d['concept']+' / '+d['title'],'Local preview; geometry provisional, actual photographed size unknown')
    sp=selected(d);put(im,shirt(d,d['color'],sp['visible_bounds_inches']['width']),(24,100));text(im,(30,720),d['family']+' / 1717 / '+d['color'],20)
    save(im,ROOT/'assets'/f'{d["id"]}-shirt.png')
(ROOT/'layout-specs.json').write_text(json.dumps(specs,indent=2)+'\n')
print(json.dumps([x for x in specs if x['selected']],indent=2))
