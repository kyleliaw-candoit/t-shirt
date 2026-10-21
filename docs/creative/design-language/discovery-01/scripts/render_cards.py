from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,html,os
R=Path(__file__).resolve().parents[5];D=R/'docs/creative/design-language/discovery-01'
F=json.loads((D/'families.json').read_text());M={r['id']:r for r in json.loads((D/'review-log.json').read_text())}
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf';ITALIC='/usr/share/fonts/opentype/urw-base35/URWBookman-LightItalic.otf'
def font(n,b=False):return ImageFont.truetype(BOLD if b else FONT,n)
def lines(d,text,x,y,w,size=23,color='#293738',bold=False,gap=6):
 ff=font(size,bold); words=text.split();line=''
 for word in words:
  cand=(line+' '+word).strip()
  if d.textlength(cand,font=ff)>w and line:
   d.text((x,y),line,font=ff,fill=color);y+=size+gap;line=word
  else:line=cand
 if line:d.text((x,y),line,font=ff,fill=color);y+=size+gap
 return y
def center(d,s,y,n=36,c='#e7dbc1',face=BOLD):
 ff=ImageFont.truetype(face,n);d.text((260-d.textlength(s,font=ff)/2,y),s,font=ff,fill=c)
def neutral(f):
 im=Image.new('RGB',(520,480),'#f2efe8');d=ImageDraw.Draw(im)
 dark='#263a3d';cream='#e8dcc3';rust='#bd6f4c';blue='#64a9aa'
 d.polygon([(155,45),(211,24),(309,24),(365,45),(470,100),(423,180),(370,155),(370,440),(150,440),(150,155),(97,180),(50,100)],fill=dark)
 d.arc((210,0,310,80),0,180,fill='#738486',width=3)
 n=f['n']
 if n==1:
  for j,t in enumerate(['CLEAR','SHORT','WORDS']):center(d,t,140+j*44,37)
 elif n==2:
  d.arc((205,160,315,220),180,355,fill=cream,width=4);d.line((205,203,315,203),fill=cream,width=4)
  d.ellipse((220,181,225,186),fill=cream);center(d,'small note',219,17,face=FONT)
 elif n==3:
  center(d,'OBJECT STUDY',125,26,face=SERIF)
  d.polygon([(235,190),(285,190),(303,267),(217,267)],outline=cream,width=4)
  d.arc((235,178,285,205),0,360,fill=cream,width=3)
  for x in range(227,295,9):d.line((x,227,x-6,258),fill=rust,width=2)
  center(d,'FIELD NOTE',287,24,face=SERIF)
 elif n==4:
  center(d,'PLAYFUL',125,38,c=rust)
  d.rounded_rectangle((180,190,246,270),radius=12,outline=cream,width=5)
  d.ellipse((260,180,336,256),outline=blue,width=6)
  d.line((260,260,329,275),fill=blue,width=5)
  center(d,'FORMS',282,46,c=rust)
 elif n==5:
  center(d,'Good',140,49,face=ITALIC);center(d,'form',193,49,face=ITALIC)
  d.line((197,255,327,255),fill=rust,width=5)
 elif n==6:
  d.rounded_rectangle((183,112,337,345),radius=12,outline=cream,width=3)
  d.rectangle((193,122,327,335),outline=cream,width=1)
  d.line((260,165,260,285),fill=cream,width=3)
  for y in [185,215,245]:
   d.ellipse((222,y-14,260,y+8),outline=cream,width=2);d.ellipse((260,y-3,300,y+19),outline=cream,width=2)
  center(d,'STUDY',304,20,face=SERIF)
 elif n==7:
  d.ellipse((185,125,335,275),fill=cream);d.ellipse((245,145,295,195),fill=rust)
  d.polygon([(185,230),(226,180),(260,227),(286,205),(335,240),(310,270),(210,270)],fill=dark)
  d.line((210,279,310,279),fill=blue,width=3)
 elif n==8:
  center(d,'a little note',170,28,face=ITALIC)
  d.arc((174,188,337,215),0,150,fill=cream,width=1)
 im.save(D/f"assets/{f['id']}-neutral.png")
 return im

for f in F:
 card=Image.new('RGB',(1600,1780),'#f5f2eb');d=ImageDraw.Draw(card)
 d.rectangle((0,0,1600,130),fill='#203a3b')
 d.text((42,22),f"{f['id']}  /  {f['name']}",font=font(38,True),fill='white')
 d.text((44,79),'PROVISIONAL  •  image-native discovery  •  20 October 2026',font=font(22),fill='#bed6d1')
 for k,id in enumerate(f['refs']):
  x=42+k*518;rec=M[id];src=Image.open(R/rec['image']).convert('RGB');im=ImageOps.contain(src,(486,420));card.paste(im,(x+(486-im.width)//2,155))
  d.text((x,586),id,font=font(22,True),fill='#203a3b')
  lines(d,rec['title'][:73] + ('…' if len(rec['title'])>73 else ''),x,617,480,18)
 d.line((42,680,1558,680),fill='#b9c2bc',width=2)
 d.text((42,705),'ANCHOR DETAIL',font=font(22,True),fill='#203a3b')
 rec=M[f['anchor']];src=Image.open(R/rec['image']).convert('RGB');box=tuple(round(z*(src.width if i%2==0 else src.height)) for i,z in enumerate(f['box']));crop=src.crop(box)
 crop.save(D/f"assets/{f['id']}-detail.jpg",quality=93)
 ci=ImageOps.contain(crop,(470,315));card.paste(ci,(42+(470-ci.width)//2,750))
 # Three numbered horizontal observation zones, not claims of exact semantic boundaries.
 for j,p in enumerate([.16,.50,.84]):
  yy=750+int(ci.height*p);d.ellipse((45,yy-12,69,yy+12),fill='#bb593c');d.text((52,yy-10),str(j+1),font=font(15,True),fill='white')
 lines(d,f['detail'],42,1086,480,21)
 d.text((560,705),'NEUTRAL RECONSTRUCTION',font=font(22,True),fill='#203a3b')
 ni=neutral(f);ni=ImageOps.contain(ni,(490,340));card.paste(ni,(560,745))
 lines(d,'Independent structural diagram. Generic forms and substitute type; source crops carry the finer style evidence. Not production artwork.',560,1086,480,21)
 d.text((1080,705),'OBSERVED RELATIONSHIPS',font=font(22,True),fill='#203a3b')
 y=lines(d,f['observed'],1080,751,470,23)
 y=lines(d,'Mockup estimate',1080,y+20,470,21,bold=True)
 lines(d,f['metric'],1080,y+6,470,20)
 d.line((42,1275,1558,1275),fill='#b9c2bc',width=2)
 d.text((42,1300),'PALETTE ROLES',font=font(20,True),fill='#203a3b')
 for j,c in enumerate(f['palette']):
  xx=42+j*146;d.rectangle((xx,1339,xx+125,1383),fill=c,outline='#b5b5a8');d.text((xx,1392),c,font=font(18),fill='#203a3b')
 lines(d,'Interpretive screen-color proxies, not measured ink formulas.',42,1434,460,20)
 d.text((560,1300),'ESSENTIAL',font=font(20,True),fill='#203a3b');lines(d,f['essential'],560,1341,480,22)
 d.text((1080,1300),'FLEXIBLE',font=font(20,True),fill='#203a3b');lines(d,f['flexible'],1080,1341,470,22)
 d.text((42,1560),'GARMENT + APPLICATION',font=font(20,True),fill='#203a3b');lines(d,f['garment'],42,1601,1490,22)
 card.save(D/f"assets/{f['id']}-card.jpg",quality=90)
 f['measurement']={'source':f['anchor'],'normalized_artwork_box_xyxy':f['box'],'pixel_box_xyxy':list(box),'visible_torso_x_limits':f['body'],'method':'manual visual bounds; denominator is horizontal visible torso width at artwork level, not shoulder/sleeve width; approximately ±5 percentage points for flat mockups, ±10 or more for styled/folded photos','limitations':'Perspective, folds, occlusion and reproduction may distort ratios. Ranges describe these images, not universal recipe limits.'}
 refs='\n'.join(f"- [{id}]({os.path.relpath(R/M[id]['record'],D/'families')}) — [retained full image]({os.path.relpath(R/M[id]['image'],D/'families')}); [source product]({M[id]['url']})." for id in f['refs'])
 text=f"# {f['id']} — {f['name']}\n\nProvisional visual family · 2026-10-20 · Analyst interpretation, not purchase validation.\n\n![Visual recipe card](../assets/{f['id']}-card.jpg)\n\n## References and evidence\n\n{refs}\n\nCore examples: {', '.join(f['core'])}.\n\nBoundary examples: {', '.join(f['bridge'])}. These share some relationships but differ in lettering, image treatment, framing, scale or garment; membership is not all-or-nothing. Full record links and original observations are in the [220-image review log](../Review-Log.md). Source-order and commercial-signal limitations remain attached to each source record.\n\n"
 for label,key in [('Observed combination','observed'),('Essential relationships — working hypothesis','essential'),('Flexible relationships and subtypes','flexible'),('Garment relationship','garment'),('Audience and semantic fit — transfer hypothesis','fit'),('Failure conditions','failure'),('Measured relationships','metric'),('Application guidance — proposed choice','proposal')]:text+=f"## {label}\n\n{f[key]}\n\n"
 text+=f"Measurement source: {f['anchor']}; normalized artwork box `{f['box']}` (x1, y1, x2, y2 as fractions of the full retained image). Pixel crop `{list(box)}`. {f['measurement']['method']}. {f['measurement']['limitations']} Palette hex values are interpretive visual proxies, not sampled production inks. Crop callouts 1–3 mark upper/middle/lower observation zones; the adjacent note explains their relationship.\n\nThe independent [neutral reconstruction](../assets/{f['id']}-neutral.png) substitutes generic words and shapes. It preserves an interpretation of composition and palette relationships; it does not reproduce the source font, distinctive artwork, exact texture or creator intent. Use the full references and detail crop alongside it.\n\n## Application evidence\n\n"
 text+=('[CAR: WRONG round 02](../../applications/CAR-WRONG-02/README.md) tests this family. Read its frozen assessment and limitations before claiming transfer.\n' if f['n'] in [3,4] else 'Not applied in this round. Source recurrence alone does not establish transfer to a new audience or concept.\n')
 (D/f"families/{f['id']}.md").write_text(text)
(D/'families.json').write_text(json.dumps(F,indent=2,ensure_ascii=False)+'\n')
print('Rendered 8 cards, 8 detail crops and 8 independent structural diagrams.')
