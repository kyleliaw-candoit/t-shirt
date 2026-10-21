"""Measured SVG layout; source illustration pixels remain unchanged.

Local garment transform is provisional, matched visually to the round03
Printful design preview, not calibrated to a known garment reference size.
"""
from pathlib import Path
import base64, json, html
from PIL import Image
import cairosvg

ROOT=Path(__file__).parent
COLORS={'Pepper':'#514f4c','Ivory':'#fff4d9','Blue Jean':'#707e8d','Moss':'#6b7053'}
def uri(p): return 'data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()
def txt(x,y,s,size=18): return f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" fill="#333">{html.escape(s)}</text>'
def emit(name,body,w,h):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="#f7f6f1"/>{body}</svg>'
    (ROOT/'assets'/f'{name}.svg').write_text(svg)
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(ROOT/'assets'/f'{name}.png'))
sources={}
for key,name in [('A','A-heritage-draft.png'),('B','B-playful-draft.png')]:
    p=ROOT/'assets'/name; im=Image.open(p)
    bbox=im.getchannel('A').point(lambda a:255 if a>=16 else 0).getbbox()
    x,y,r,b=bbox
    sources[key]=dict(data=uri(p),size=im.size,bbox=bbox,w=r-x,h=b-y)
def art(key,x,y,w):
    s=sources[key]; bx,by,_,_=s['bbox']; h=w*s['h']/s['w']
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{bx} {by} {s["w"]} {s["h"]}" overflow="hidden"><image width="{s["size"][0]}" height="{s["size"][1]}" xlink:href="{s["data"]}"/></svg>'
records=[]
for key in sources:
    for label,width,top in [('compact-lower',8.5,1.5),('medium-lower',10,1.5),('compact-lowest',8.5,2.0)]:
        left=(12-width)/2; height=width*sources[key]['h']/sources[key]['w']
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="12in" height="16in" viewBox="0 0 12 16">{art(key,left,top,width)}</svg>'
        stem=ROOT/'layouts'/f'{key}-{label}-12x16'
        stem.with_suffix('.svg').write_text(svg)
        cairosvg.svg2png(bytestring=svg.encode(),write_to=str(stem.with_suffix('.png')),output_width=1800,output_height=2400)
        records.append(dict(design=key,variant=label,canvas_inches=[12,16],visible_bounds_inches=dict(left=left,top=top,width=width,height=round(height,4)),anchor='top-left of provider print canvas; NOT neckline',source_visible_bbox=list(sources[key]['bbox']),native_effective_ppi=round(sources[key]['w']/width,1),status='review draft; no added native detail from canvas resampling'))
(ROOT/'layout-specs.json').write_text(json.dumps(records,indent=2)+'\n')
# 602px garment preview: origin y~97, center x~303, scale~17.8px/in.
# Estimated from unchanged round03 B 8.5in layout in provider design preview.
def shirt(key,color,width,top,x,y,scale=.68):
    base=uri(ROOT/'blanks'/(color.replace(' ','-')+'.png'))
    aw=width*17.8; ay=97+top*17.8
    return f'<g transform="translate({x} {y}) scale({scale})"><rect width="602" height="602" fill="{COLORS[color]}"/><image width="602" height="602" xlink:href="{base}"/>{art(key,303-aw/2,ay,aw)}</g>'
body=txt(24,35,'CAR: WRONG — vertical placement comparison',26)+txt(24,66,'Same artwork and 8.5-inch width. Offsets are from print-area top, not the collar.',16)
for row,key in enumerate(['A','B']):
    color='Ivory' if key=='A' else 'Pepper'; y=100+row*470
    for col,(top,label) in enumerate([(0.5,'Previous anchor · 0.5 in'),(1.5,'Preferred trial · 1.5 in'),(2.0,'Lower alternative · 2.0 in')]):
        x=20+col*420; body+=txt(x,y,f'{key} / {label}',17)+shirt(key,color,8.5,top,x,y+10)
body+=txt(24,1050,'PROVISIONAL local geometry · actual photographed garment size unknown · no physical collar inches inferred',15)
emit('placement-comparison',body,1280,1080)
body=txt(24,35,'CAR: WRONG — compact / medium',26)+txt(24,66,'Both use the proposed 1.5-inch print-area offset; size changes preserve artwork aspect ratio.',16)
for row,key in enumerate(['A','B']):
    y=100+row*470; color='Ivory' if key=='A' else 'Pepper'
    for col,(width,label) in enumerate([(8.5,'Compact · 8.5 in wide'),(10,'Medium · 10 in wide')]):
        x=20+col*440; body+=txt(x,y,key+' / '+label,18)+shirt(key,color,width,1.5,x,y+10)
body+=txt(24,1050,'Provisional local preview; compact preferred for both. Dimensions belong to visible art, not padding.',14)
emit('footprint-comparison',body,900,1080)
body=txt(24,35,'CAR: WRONG — four-color trial',26)+txt(24,66,'Unchanged inks within each row. Compact placement; screen color is not a fabric/print proof.',16)
for row,key in enumerate(['A','B']):
    y=100+row*400
    for col,color in enumerate(COLORS):
        x=20+col*335; body+=txt(x,y,key+' / '+color,18)+shirt(key,color,8.5,1.5,x,y+10,.54)
body+=txt(24,930,'Shortlist: A Ivory; B Pepper and Moss. Garment geometry provisional; art remains review resolution.',17)
emit('color-comparison',body,1370,960)
body=txt(24,35,'CAR: WRONG — proposed revisions',28)+txt(24,67,'Comfort Colors 1717 · A Ivory / B Pepper · 8.5-inch visible width',18)
for col,key in enumerate(['A','B']):
    x=20+col*620; color='Ivory' if key=='A' else 'Pepper'
    body+=shirt(key,color,8.5,1.5,x,90,1)+txt(x+25,720,'A / Heritage · slimmer serif + blue linework' if key=='A' else 'B / Playful · artwork unchanged',20)
body+=txt(24,770,'Local layout simulation · lower placement trial · provider check and evidence recorded separately',17)
emit('review-board',body,1260,800)
if all((ROOT/'evidence'/f'{key}-{color}-mockup.jpg').exists() for key,color in [('A','Ivory'),('B','Pepper')]):
    body=txt(24,35,'CAR: WRONG — actual Printful previews',27)+txt(24,65,'Heritage / Ivory',20)+txt(624,65,'Playful / Pepper',20)
    for col,(key,color) in enumerate([('A','Ivory'),('B','Pepper')]):
        p=ROOT/'evidence'/f'{key}-{color}-mockup.jpg'
        data='data:image/jpeg;base64,'+base64.b64encode(p.read_bytes()).decode()
        body+=f'<svg x="{15+col*600}" y="85" width="580" height="580" viewBox="690 110 550 550"><image width="1363" height="936" xlink:href="{data}"/></svg>'
    body+=txt(24,710,'8.5-inch visible width · top 1.5 inches from print-area origin · photographed size unknown',17)
    body+=txt(24,742,'Uniformly scaled screenshot crops; full provider screenshots retained in evidence/. Review drafts.',16)
    emit('provider-review-board',body,1215,770)
print(json.dumps(records,indent=2))
