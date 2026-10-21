"""Lay out unaltered Printful screenshot regions with comparison labels."""
from pathlib import Path
import base64, html
from PIL import Image
import cairosvg
R=Path(__file__).parent
def photo(path,x,y,w,h,crop):
    im=Image.open(path); data=base64.b64encode(path.read_bytes()).decode()
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{crop}" overflow="hidden"><image width="{im.width}" height="{im.height}" href="data:image/jpeg;base64,{data}"/></svg>'
def txt(x,y,s,size=20,weight=400):
    return f'<text x="{x}" y="{y}" font-family="DejaVu Sans,sans-serif" font-size="{size}" font-weight="{weight}" fill="#242823">{html.escape(s)}</text>'
def save(name,w,h,body):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"><rect width="100%" height="100%" fill="#f5f3ed"/>{body}</svg>'
    (R/'assets'/f'{name}.svg').write_text(svg)
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(R/'assets'/f'{name}.png'))
body=txt(40,48,'CAR: WRONG.  /  Controlled placement comparison',30,700)
body+=txt(40,82,'Printful Comfort Colors 1717 · Pepper · actual mockup garment size unverified',18)
for row,(design,style) in enumerate([('A','Heritage'),('B','Playful')]):
    for col,(variant,wd,ht) in enumerate([('compact','8.50','7.24' if design=='A' else '7.46'),('medium','10.00','8.52' if design=='A' else '8.78')]):
        x,y=40+col*560,128+row*585
        body+=txt(x,y,f'{design} {style} · {variant.title()} · {wd} × {ht} in',20,700)
        body+=photo(R/'evidence'/f'{design}-{variant}-Pepper-Printful.jpg',x,y+12,520,520,'690 110 550 550')
body+=txt(40,1300,'Artwork top: 0.50 in below print-area origin. Raster masters are review drafts, not production files.',17)
save('placement-comparison',1160,1330,body)

body=txt(36,45,'Four trial colors · one compact placement',29,700)
body+=txt(36,78,'Actual Printful design previews · 1717 · visible art width 8.50 in · reference garment size unverified',16)
colors=['Pepper','Ivory','Blue-Jean','Moss']
for row,(design,style) in enumerate([('A','Heritage'),('B','Playful')]):
    body+=txt(36,118+row*380,f'{design} / {style}',20,700)
    for col,color in enumerate(colors):
        x,y=36+col*280,135+row*380
        body+=photo(R/'evidence'/f'{design}-compact-{color}-controls.jpg',x,y,260,290,'650 240 520 580')
        body+=txt(x,y+316,color.replace('-',' '),18,700)
body+=txt(36,895,'Color appearance is a screen preview; confirm the chosen artwork/garment colorway with a printed sample.',15)
save('color-comparison',1160,925,body)
