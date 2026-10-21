"""Measured layout only; artwork generated separately and never repainted here.

python build_review.py [--previous /path/to/CAR-WRONG-04]
Dependencies: Pillow (alpha measurement), cairosvg (SVG rendering).
Geometry matches the provisional round04 local preview, not a physical size.
"""
from pathlib import Path
import argparse, base64, html, json
from PIL import Image
import cairosvg

ROOT=Path(__file__).parent
p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,default=ROOT.parent/'CAR-WRONG-04');p.add_argument('--source',default='A-heritage-spacing-v2.png');args=p.parse_args()
OLD=args.previous
def uri(p):return 'data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()
def txt(x,y,s,size=18):return f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" fill="#333">{html.escape(s)}</text>'
sources={}
for key,path in [('before',OLD/'assets/A-heritage-draft.png'),('after',ROOT/'assets'/args.source),('playful',OLD/'assets/B-playful-draft.png')]:
    im=Image.open(path);bbox=im.getchannel('A').point(lambda a:255 if a>=16 else 0).getbbox();x,y,r,b=bbox
    sources[key]=dict(path=str(path),data=uri(path),size=im.size,bbox=bbox,w=r-x,h=b-y)
def art(key,x,y,w):
    s=sources[key];bx,by,_,_=s['bbox'];h=w*s['h']/s['w']
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{bx} {by} {s["w"]} {s["h"]}" overflow="hidden"><image width="{s["size"][0]}" height="{s["size"][1]}" href="{s["data"]}"/></svg>'
def emit(name,body,w,h):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"><rect width="100%" height="100%" fill="#f7f6f1"/>{body}</svg>'
    (ROOT/'assets'/f'{name}.svg').write_text(svg);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(ROOT/'assets'/f'{name}.png'))
def shirt(key,x,y,scale=1,color='Ivory'):
    bg='#fff4d9' if color=='Ivory' else '#514f4c';base=uri(OLD/'blanks'/f'{color}.png');aw=8.5*17.8
    return f'<g transform="translate({x} {y}) scale({scale})"><rect width="602" height="602" fill="{bg}"/><image width="602" height="602" href="{base}"/>{art(key,303-aw/2,97+1.5*17.8,aw)}</g>'

s=sources['after'];height=8.5*s['h']/s['w']
layout=f'<svg xmlns="http://www.w3.org/2000/svg" width="12in" height="16in" viewBox="0 0 12 16">{art("after",1.75,1.5,8.5)}</svg>'
(ROOT/'layouts/A-heritage-spaced-12x16.svg').write_text(layout)
cairosvg.svg2png(bytestring=layout.encode(),write_to=str(ROOT/'layouts/A-heritage-spaced-12x16.png'),output_width=1800,output_height=2400)
spec=dict(artwork=args.source,canvas_inches=[12,16],visible_bounds_inches=dict(left=1.75,top=1.5,width=8.5,height=round(height,4)),anchor='provider print-canvas top-left, NOT collar',native_visible_bbox=s['bbox'],native_effective_ppi=round(s['w']/8.5,1),mockup_actual_garment_size='unknown',local_geometry='provisional round04 transform, 17.8 pixels/inch, print origin y=97, center x=303 in a 602px preview; not physically calibrated')
(ROOT/'layout-specs.json').write_text(json.dumps(spec,indent=2)+'\n')
body=txt(24,34,'Heritage — internal spacing revision',26)+txt(24,65,'Controlled local comparison: same Ivory blank, 8.5-inch width and 1.5-inch print-canvas top offset.',16)
for col,key in enumerate(['before','after']):
    x=20+col*620
    body+=txt(x+15,104,'Before · round04' if key=='before' else 'After · round05',21)
    body+=f'<rect x="{x+25}" y="125" width="550" height="510" rx="4" fill="#fff4d9"/>'+art(key,x+45,145,510)
    body+=shirt(key,x,660)
body+=txt(24,1290,'Artwork above / garment below. Local garment geometry is provisional; photographed size unknown.',16)
emit('spacing-comparison',body,1260,1320)
body=txt(24,34,'CAR: WRONG — Heritage revision and retained Playful',25)+txt(24,65,'Local layouts · Comfort Colors 1717 · 8.5-inch visible width · top 1.5 inches from print-canvas origin',16)
body+=shirt('after',20,85)+shirt('playful',640,85,color='Pepper')
body+=txt(45,725,'A · Heritage / Ivory · more internal breathing room',19)+txt(665,725,'B · Playful / Pepper · unchanged',19)
body+=txt(24,775,'Provisional preview geometry, actual garment size unknown. Review drafts; not physical print proofs.',16)
emit('review-board',body,1260,805)
if (ROOT/'evidence/A-Ivory-mockup.jpg').exists():
    body=txt(24,35,'Heritage — actual Printful previews',27)+txt(24,68,'Before · round04',20)+txt(624,68,'After · round05',20)
    for col,path in enumerate([OLD/'evidence/A-Ivory-mockup.jpg',ROOT/'evidence/A-Ivory-mockup.jpg']):
        data='data:image/jpeg;base64,'+base64.b64encode(path.read_bytes()).decode()
        body+=f'<svg x="{15+col*600}" y="85" width="580" height="580" viewBox="690 110 550 550"><image width="1363" height="936" href="{data}"/></svg>'
    body+=txt(24,710,'Ivory / 8.5-inch visible width / top 1.5 inches from print canvas. Actual photographed size unknown.',16)
    body+=txt(24,742,'Uniformly scaled screenshot crops; full provider screenshots retained. Review drafts.',16)
    emit('provider-comparison',body,1215,770)
print(json.dumps(spec,indent=2))
