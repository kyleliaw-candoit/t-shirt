"""Measured layout of imagegen edits; no repainting or alpha cleanup."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import hashlib,json
R=Path(__file__).parent;B=R.parent.parent/'CAR-WRONG-04/blanks'
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
DESIGNS=[('TE','TE-sofa-v3.png','Pepper','#514f4c',8.5),('NA','NA-tagged-v2.png','Ivory','#fff4d9',8.0)]
def txt(im,xy,s,size=20):ImageDraw.Draw(im).text(xy,s,font=ImageFont.truetype(F,size),fill='#263739')
def page(w,h,title,sub):
 im=Image.new('RGB',(w,h),'#f5f3ed');txt(im,(24,20),title,27);txt(im,(24,62),sub,16);return im
shirts={};specs=[]
for cid,file,color,hexcolor,width in DESIGNS:
 p=R/'assets'/file;a=Image.open(p).convert('RGBA');bbox=a.getchannel('A').point(lambda x:255 if x>=16 else 0).getbbox();a=a.crop(bbox);height=width*a.height/a.width;left=(12-width)/2
 assert left>=0 and height+1.5<=16
 c=Image.new('RGBA',(1800,2400));c.alpha_composite(a.resize((round(width*150),round(height*150)),Image.Resampling.LANCZOS),(round(left*150),225));c.save(R/'layouts'/f'{cid}-revised-12x16.png',dpi=(150,150))
 bg=Image.new('RGBA',(602,602),hexcolor);bg.alpha_composite(Image.open(B/(color.replace(' ','-')+'.png')).convert('RGBA').resize((602,602)));w=round(width*17.8);h=round(w*a.height/a.width);bg.alpha_composite(a.resize((w,h),Image.Resampling.LANCZOS),(round(303-w/2),124));shirts[cid]=bg
 out=page(650,770,cid+' / Revised object cue','1717 / DTG front / local geometry provisional; photographed size unknown');out.paste(bg,(24,100),bg);txt(out,(30,720),f'{color} / {width} in wide / top 1.5 in',20);out.save(R/'assets'/f'{cid}-shirt.png')
 specs.append({'concept':cid,'source':file,'blank':'Comfort Colors 1717','method':'DTG front','color':color,'canvas_inches':[12,16],'visible_inches':{'width':width,'height':round(height,4),'left':left,'top':1.5},'anchor':'print-canvas origin, not physical neckline','native_bbox_alpha16':bbox,'native_effective_ppi':round(a.width/width,1),'master_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'geometry':'provisional round04; 17.8px/in, center x303, print origin y97 on 602px blank','reference_size':'unknown','nominal_width_percent':{s:round(width/v*100,1) for s,v in [('S',18.25),('L',22),('2XL',26)]}})
out=page(1280,790,'Revised object cues — T-E and N-A','Established widths, colors and top anchor retained; revised artwork for review.')
for j,(cid,label) in enumerate([('TE','T-E B / vintage three-seat sofa'),('NA','N-A / price tag attached to bowl')]):
 out.paste(shirts[cid],(20+j*625,100),shirts[cid]);txt(out,(35+j*625,725),label,21)
out.save(R/'assets/review-board.png')
out=page(1280,1440,'Before / after — object cues','Typography-led T-E and framed N-A: compare semantic clarity at shirt scale.')
for j,(cid,oldpath) in enumerate([('TE',R.parent/'TE-quiet-02/assets/selected-shirt.png'),('NA',R.parent/'assets/NA-shirt.png')]):
 old=Image.open(oldpath).convert('RGBA').crop((24,100,626,702));y=100+j*650;out.paste(old,(20,y),old);out.paste(shirts[cid],(645,y),shirts[cid]);txt(out,(40,y+610),cid+' / prior version',20);txt(out,(665,y+610),cid+' / revised cue',20)
out.save(R/'assets/before-after.png')
(R/'layout-specs.json').write_text(json.dumps(specs,indent=2)+'\n');print(json.dumps(specs,indent=2))
if all((R/'evidence'/f'{c}-provider-mockup.jpg').exists() for c in ['TE','NA']):
 out=page(1145,695,'Printful previews — revised object cues','Comfort Colors 1717 / DTG front / generated previews, not physical samples')
 for j,(cid,label) in enumerate([('TE','T-E B / vintage sofa / Pepper'),('NA','N-A / attached $8 tag / Ivory')]):
  shot=Image.open(R/'evidence'/f'{cid}-provider-mockup.jpg').convert('RGB').crop((690,110,1240,660));out.paste(shot,(15+j*565,100));txt(out,(24+j*565,660),label,20)
 out.save(R/'evidence/provider-pair.png')
