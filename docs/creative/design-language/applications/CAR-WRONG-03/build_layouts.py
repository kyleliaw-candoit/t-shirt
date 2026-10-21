"""Place unchanged review artwork in a measured 12 x 16 inch print canvas.

Only the viewBox clips faint peripheral generation artifacts. No redraw,
recolor, or claim of added native resolution. CairoSVG is the layout renderer.
"""
from pathlib import Path
import base64, json
from PIL import Image
import cairosvg

ROOT = Path(__file__).parent
records = []
for design, file in [('A', 'A-heritage-draft.png'), ('B', 'B-playful-draft.png')]:
    p = ROOT / 'assets' / file
    im = Image.open(p)
    # Exclude near-invisible peripheral noise from the visible artwork measure.
    bbox = im.getchannel('A').point(lambda a: 255 if a >= 16 else 0).getbbox()
    x, y, right, bottom = bbox
    w, h = right-x, bottom-y
    data = base64.b64encode(p.read_bytes()).decode()
    for label, width in [('compact', 8.5), ('medium', 10.0)]:
        height = width*h/w
        left, top = (12-width)/2, .5
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="12in" height="16in" viewBox="0 0 12 16">
<svg x="{left}" y="{top}" width="{width}" height="{height}" viewBox="{x} {y} {w} {h}" overflow="hidden">
<image width="{im.width}" height="{im.height}" xlink:href="data:image/png;base64,{data}"/>
</svg></svg>'''
        out = ROOT / 'layouts' / f'{design}-{label}-12x16'
        out.with_suffix('.svg').write_text(svg)
        cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out.with_suffix('.png')),output_width=1800,output_height=2400)
        records.append(dict(design=design,variant=label,canvas_inches=[12,16],visible_bounds_inches=dict(left=left,top=top,width=width,height=round(height,4)),source_pixels=list(im.size),source_visible_bbox=list(bbox),native_effective_ppi=round(w/width,1),rendered_canvas_pixels=[1800,2400],status='review only; native source below 150ppi at these widths; not production-ready'))
(ROOT/'layout-specs.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
