import json, math, sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
from PIL import Image, ImageDraw, ImageFont

S = 3  # supersampling
W, H = 1080, 1350
BG = (16, 16, 16)
FG = (243, 245, 247)
GRAY = (119, 119, 119)
ICON = (220, 222, 224)
F = os.path.join(BASE, 'fonts', 'Roboto-%s.ttf')

def font(w, size): return ImageFont.truetype(F % w, size * S)

def wrap(draw, text, fnt, maxw):
    words, lines, cur = text.replace(' —', '\u00a0—').split(' '), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=fnt) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    return lines

def heart(d, x, y, s, lw):
    pts = []
    for i in range(0, 361, 3):
        t = math.radians(i)
        hx = 16 * math.sin(t) ** 3
        hy = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        pts.append((x + s/2 + hx * s/34, y + s/2 + hy * s/34 + s*0.05))
    d.line(pts + [pts[0]], fill=ICON, width=lw, joint='curve')

def bubble(d, x, y, s, lw):
    r = s * 0.46; cx, cy = x + s/2, y + s/2
    d.arc((cx-r, cy-r, cx+r, cy+r), start=135, end=100, fill=ICON, width=lw)
    a1, a2 = math.radians(100), math.radians(135)
    p1 = (cx + r*math.cos(a1), cy + r*math.sin(a1)); p2 = (cx + r*math.cos(a2), cy + r*math.sin(a2))
    tip = (x + s*0.06, y + s*0.98)
    d.line([p1, tip, p2], fill=ICON, width=lw, joint='curve')

def repost(d, x, y, s, lw):
    r = s * 0.40; cx, cy = x + s/2, y + s/2
    d.arc((cx-r, cy-r, cx+r, cy+r), start=200, end=345, fill=ICON, width=lw)
    d.arc((cx-r, cy-r, cx+r, cy+r), start=20, end=165, fill=ICON, width=lw)
    a = s * 0.16
    for ang, dirn in ((345, 1), (165, -1)):
        t = math.radians(ang); px, py = cx + r*math.cos(t), cy + r*math.sin(t)
        d.line([(px - a*dirn, py), (px, py), (px, py - a*dirn)], fill=ICON, width=lw, joint='curve')

def send(d, x, y, s, lw):
    p = [(x+s*0.08, y+s*0.08), (x+s*0.95, y+s*0.5), (x+s*0.08, y+s*0.92), (x+s*0.24, y+s*0.5)]
    d.line(p + [p[0]], fill=ICON, width=lw, joint='curve')
    d.line([(x+s*0.24, y+s*0.5), (x+s*0.6, y+s*0.5)], fill=ICON, width=lw)

def badge(d, cx, cy, r):
    pts = []
    for i in range(0, 360, 2):
        t = math.radians(i); rr = r * (0.9 + 0.1 * math.cos(8 * t))
        pts.append((cx + rr*math.cos(t), cy + rr*math.sin(t)))
    d.polygon(pts, fill=(0, 149, 246))
    d.line([(cx - r*0.42, cy + r*0.02), (cx - r*0.1, cy + r*0.34), (cx + r*0.45, cy - r*0.3)],
           fill=(255, 255, 255), width=int(r*0.26), joint='curve')

def render(quote, out):
    img = Image.new('RGB', (W*S, H*S), BG); d = ImageDraw.Draw(img)
    body = font('400', 42); name_f = font('600', 36); time_f = font('400', 34)
    left = 76*S; maxw = (W - 2*76)*S
    lines = wrap(d, quote, body, maxw)
    lh = 64*S; av = 112*S; gap1 = 34*S; gap2 = 44*S; icon = 46*S
    total = av + gap1 + lh*len(lines) + gap2 + icon
    top = (H*S - total)//2
    # avatar
    a = Image.open(os.path.join(BASE, 'avatar.png')).resize((av, av), Image.LANCZOS)
    m = Image.new('L', (av, av), 0); ImageDraw.Draw(m).ellipse((0, 0, av-1, av-1), fill=255)
    ax = 52*S; img.paste(a, (ax, top), m)
    d.ellipse((ax, top, ax+av, top+av), outline=(51, 51, 51), width=2*S)
    # name row
    nx = ax + av + 22*S; ny = top + av//2
    d.text((nx, ny), 'dr.eurojunior', font=name_f, fill=FG, anchor='lm')
    nw = d.textlength('dr.eurojunior', font=name_f)
    badge(d, nx + nw + 22*S, ny, 15*S)
    d.text((nx + nw + 48*S, ny), 'now', font=time_f, fill=GRAY, anchor='lm')
    # body
    y = top + av + gap1
    for ln in lines:
        d.text((left, y + lh//2), ln, font=body, fill=FG, anchor='lm'); y += lh
    # icons
    y += gap2 - 10*S; lw = int(3.2*S); x = left
    for fn in (heart, bubble, repost, send):
        fn(d, x, y, icon, lw); x += 132*S
    img.resize((W, H), Image.LANCZOS).convert('RGB').save(out, quality=95)

if __name__ == '__main__':
    # uso: python3 render.py lotes/AAAA-MM-DD   (pasta com posts.json)
    d = sys.argv[1]
    posts = json.load(open(os.path.join(d, 'posts.json')))
    for i, p in enumerate(posts, 1):
        render(p['quote'], os.path.join(d, f'post_{i:02d}.jpg'))
    print(len(posts))
