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
    """Quebra automática + respeita quebras manuais. '\n' = nova linha,
    '\n\n' = parágrafo (vira '' na lista e ganha meio espaço extra)."""
    out = []
    for pi, para in enumerate(text.split('\n\n')):
        if pi: out.append('')
        for raw in para.split('\n'):
            words, cur = raw.replace(' —', ' —').split(' '), ''
            for w in words:
                t = (cur + ' ' + w).strip()
                if draw.textlength(t, font=fnt) <= maxw: cur = t
                else: out.append(cur); cur = w
            out.append(cur)
    return out

def text_height(lines, lh):
    return sum(lh if ln else int(lh * 0.6) for ln in lines)

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

# ── Layout (regras do Euro, 22/11/2026) ─────────────────────────────
# Canvas 1080x1350 (4:5). Tudo que é essencial fica dentro da SAFE AREA
# central 1080x1080 (y 135–1215), porque o Explorar corta para 1:1.
# Nome, texto e ícones compartilham a MESMA margem esquerda (COL_X);
# o avatar fica à esquerda dessa coluna. Bloco centralizado na vertical.
SAFE_TOP, SAFE_BOT = (H - 1080) // 2, (H + 1080) // 2
PAD = 70                      # respiro interno dentro da safe area
AV = 132                      # avatar com presença
AV_X = 56
COL_X = AV_X + AV + 26        # margem única de nome/texto/ícones
COL_W = W - COL_X - 64
LH_RATIO = 1.45               # entrelinha confortável
REF_MIN_CHARS = 170           # frase de referência mínima para o auto-fit
MAX_FONT, MIN_FONT = 62, 40

def layout(d, quote, size):
    body = font('400', size)
    lines = wrap(d, quote, body, COL_W * S)
    lh = int(size * LH_RATIO)
    name_h = AV // 2 + 18
    gap1, gap2, icon = int(size * 0.55), int(size * 0.9), 48
    total = name_h + gap1 + text_height(lines, lh) + gap2 + icon
    total = max(total, AV)
    return body, lines, lh, gap1, gap2, icon, total

def fit_size(d, quotes):
    ref = max(quotes, key=len)
    if len(ref) < REF_MIN_CHARS:
        ref = (ref + ' ') * (REF_MIN_CHARS // max(len(ref), 1) + 1)
        ref = ref[:REF_MIN_CHARS]
    # mede a referência E todas as frases: parágrafos (\n\n) ocupam altura
    # extra, então a frase mais longa em caracteres nem sempre é a mais alta
    for size in range(MAX_FONT, MIN_FONT - 1, -1):
        total = max(layout(d, q, size)[-1] for q in [ref] + list(quotes))
        if total <= (SAFE_BOT - SAFE_TOP) - 2 * PAD:
            return size
    return MIN_FONT

def render(quote, out, size):
    img = Image.new('RGB', (W*S, H*S), BG); d = ImageDraw.Draw(img)
    body, lines, lh, gap1, gap2, icon, total = layout(d, quote, size)
    name_f = font('600', 38); time_f = font('400', 36)
    top = (H - total) // 2
    assert top >= SAFE_TOP + PAD - 1 and top + total <= SAFE_BOT - PAD + 1, 'fora da safe area'
    av = AV * S
    a = Image.open(os.path.join(BASE, 'avatar.png')).resize((av, av), Image.LANCZOS)
    m = Image.new('L', (av, av), 0); ImageDraw.Draw(m).ellipse((0, 0, av-1, av-1), fill=255)
    ax, ay = AV_X * S, top * S
    img.paste(a, (ax, ay), m)
    d.ellipse((ax, ay, ax+av, ay+av), outline=(51, 51, 51), width=2*S)
    cx = COL_X * S
    ny = ay + 38 * S
    d.text((cx, ny), 'dr.eurojunior', font=name_f, fill=FG, anchor='lm')
    nw = d.textlength('dr.eurojunior', font=name_f)
    badge(d, cx + nw + 24*S, ny, 16*S)
    d.text((cx + nw + 52*S, ny), 'now', font=time_f, fill=GRAY, anchor='lm')
    y = ay + (AV // 2 + 18 + gap1) * S
    for ln in lines:
        if not ln: y += int(lh * 0.6) * S; continue
        d.text((cx, y + lh*S//2), ln, font=body, fill=FG, anchor='lm'); y += lh*S
    y += (gap2 - 6) * S; lw = int(3.3*S); x = cx; ic = icon * S
    for fn in (heart, bubble, repost, send):
        fn(d, x, y, ic, lw); x += 128*S
    img.resize((W, H), Image.LANCZOS).convert('RGB').save(out, quality=95)

def history_quotes():
    import glob
    qs = []
    for f in glob.glob(os.path.join(BASE, 'lotes', '*', 'posts.json')):
        qs += [p['quote'] for p in json.load(open(f))]
    return qs

if __name__ == '__main__':
    # uso: python3 render.py lotes/AAAA-MM-DD   (pasta com posts.json)
    folder = sys.argv[1]
    posts = json.load(open(os.path.join(folder, 'posts.json')))
    probe = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    size = fit_size(probe, history_quotes() + [p['quote'] for p in posts])
    for i, p in enumerate(posts, 1):
        render(p['quote'], os.path.join(folder, f'post_{i:02d}.jpg'), size)
    print(f'{len(posts)} artes, fonte {size}px')
