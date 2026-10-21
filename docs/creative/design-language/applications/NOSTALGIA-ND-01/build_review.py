"""Measured placement only. Generated artwork pixels are not repainted.

Run in this directory with Pillow installed. Reuses round04 cached blanks and
its explicitly provisional transform: 17.8 px/in, origin y=97, center x=303.
No photographed garment size or physical neckline offset is established.
"""
from pathlib import Path
import hashlib, json
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).parent
BLANKS=ROOT.parent/'CAR-WRONG-04/blanks'
COLORS=['Pepper','Ivory','Blue Jean','Moss']
COLOR_HEX={'Pepper':'#514f4c','Ivory':'#fff4d9','Blue Jean':'#707e8d','Moss':'#6b7053'}
FONTP='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def label(im,xy,text,size=20):
    ImageDraw.Draw(im).text(xy,text,font=ImageFont.truetype(FONTP,size),fill='#263739')
def page(w,h,title,subtitle):
    im=Image.new('RGB',(w,h),'#f5f3ed');label(im,(24,20),title,26);label(im,(24,60),subtitle,16);return im
def save(im,name):
    target=ROOT/'assets'/name
    temporary=target.with_name(target.stem+'-writing.png')
    im.save(temporary)
    temporary.replace(target)
sources={}
specs=[]
for k,name,widths,color in [('A','A-heritage-v3.png',[8.75,10.25],'Ivory'),('B','B-artifact-v1.png',[8.25,9.5],'Pepper')]:
    original=Image.open(ROOT/'assets'/name).convert('RGBA')
    bbox=original.getchannel('A').point(lambda a:255 if a>=16 else 0).getbbox()
    crop=original.crop(bbox)
    sources[k]={'image':crop,'bbox':bbox,'name':name,'widths':widths,'color':color}
    for variant,width in zip(['compact','medium'],widths):
        height=width*crop.height/crop.width;left=(12-width)/2;top=1.5
        canvas=Image.new('RGBA',(1800,2400))
        resized=crop.resize((round(width*150),round(height*150)),Image.Resampling.LANCZOS)
        canvas.alpha_composite(resized,(round(left*150),round(top*150)))
        filename=f'{k}-{variant}-12x16.png';canvas.save(ROOT/'layouts'/filename,dpi=(150,150))
        specs.append({'design':k,'family':'DLF-003' if k=='A' else 'DLF-006','artwork':name,'variant':variant,'canvas_inches':[12,16],'visible_bounds_inches':{'left':left,'top':top,'width':width,'height':round(height,4)},'position_reference':'12x16 print-canvas top-left, NOT neckline','native_visible_bbox':bbox,'native_effective_ppi':round(crop.width/width,1),'layout_file':filename,'selected':variant=='compact','selected_color':color,'native_master_sha256':hashlib.sha256((ROOT/'assets'/name).read_bytes()).hexdigest(),'mockup_reference_size':'unknown','local_geometry':'round04 provisional transform; 17.8px/in; origin y=97, center x=303 on 602px blank','size_chart_width_percent':{s:round(width/v*100,1) for s,v in [('S',18.25),('L',22),('2XL',26)]}})
def shirt(k,color,width,scale=1):
    base=Image.new('RGBA',(602,602),COLOR_HEX[color])
    base.alpha_composite(Image.open(BLANKS/(color.replace(' ','-')+'.png')).convert('RGBA').resize((602,602)))
    a=sources[k]['image'];w=round(width*17.8);h=round(w*a.height/a.width)
    base.alpha_composite(a.resize((w,h),Image.Resampling.LANCZOS),(round(303-w/2),round(97+1.5*17.8)))
    return base.resize((round(602*scale),round(602*scale)),Image.Resampling.LANCZOS)
def paste_shirt(im,k,color,width,xy,scale=1):
    a=shirt(k,color,width,scale);im.paste(a,xy,a)
im=page(1260,790,'Saturday at Grandma\'s — two visual families','Comfort Colors 1717 / DTG front / provisional local geometry; actual photographed size unknown')
for j,k in enumerate(['A','B']):
    s=sources[k];paste_shirt(im,k,s['color'],s['widths'][0],(20+j*620,100))
    sp=next(x for x in specs if x['design']==k and x['selected'])
    label(im,(35+j*620,718),f"{k} / {'Heritage' if k=='A' else 'Framed artifact'} / {s['color']}",22)
    label(im,(35+j*620,752),f"Visible art {sp['visible_bounds_inches']['width']} x {sp['visible_bounds_inches']['height']} in; top 1.5 in",16)
save(im,'review-board.png')
im=page(1260,1070,'Compact and medium — same art, blank, color and top anchor','Width and height change together. These are alternative footprints, not sizes on one shirt.')
for r,k in enumerate(['A','B']):
    s=sources[k]
    for c,w in enumerate(s['widths']):
        x=20+c*620;y=100+r*465
        label(im,(x+20,y),f"{k} / {'compact' if c==0 else 'medium'} / {w} in wide",20)
        paste_shirt(im,k,s['color'],w,(x+80,y+30),.7)
label(im,(24,1035),'Local garment relationships are estimates; artwork inches do not prove physical fit.',16)
save(im,'footprint-comparison.png')
im=page(1420,950,'Four-color trial — unchanged inks within each row','Cached provider blank images; color appearance is approximate. Selected: A Ivory / B Pepper.')
for r,k in enumerate(['A','B']):
    s=sources[k]
    for c,color in enumerate(COLORS):
        x=15+c*350;y=105+r*405
        label(im,(x+15,y),f'{k} / {color}',20);paste_shirt(im,k,color,s['widths'][0],(x,y+35),.56)
save(im,'color-comparison.png')
im=page(1260,900,'Artwork detail — actual selected masters','Ivory and Pepper viewing grounds only; both source masters have alpha transparency.')
for j,k in enumerate(['A','B']):
    s=sources[k];a=s['image'];a=a.resize((540,round(540*a.height/a.width)),Image.Resampling.LANCZOS)
    x=35+j*620;y=115
    ImageDraw.Draw(im).rectangle((x-15,y-15,x+555,850),fill='#fff4d9' if k=='A' else '#514f4c')
    im.paste(a,(x,y),a)
save(im,'artwork-detail.png')
(ROOT/'layout-specs.json').write_text(json.dumps(specs,indent=2)+'\n')
print(json.dumps(specs,indent=2))
