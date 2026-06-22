# Gera o stage plot técnico (top-down) em SVG -> assets/stageplot.svg
# Layout: upstage (fundo) em cima, downstage (frente/plateia) embaixo
# Esq -> Dir: Guit. Solo | Baixo | [Bateria fundo / Vocal frente] | Guit. Base
# Tema Piteira: fundo plum, traços roxos, badges verdes.

W, H = 1000, 760
STAGE_X, STAGE_Y, STAGE_W, STAGE_H = 40, 70, 920, 600

INK="#0b0a0d"; PURPLE="#CA88F1"; GREEN="#8cfa8c"; CREAM="#f3eef7"; PLUM="#1c1022"; GREY="#6b6478"

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Arial, sans-serif">')
# fundo
svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PLUM}"/>')
# moldura do palco
svg.append(f'<rect x="{STAGE_X}" y="{STAGE_Y}" width="{STAGE_W}" height="{STAGE_H}" '
           f'fill="#140d1c" stroke="{PURPLE}" stroke-width="4" rx="6"/>')
# labels upstage/downstage
svg.append(f'<text x="{W/2}" y="{STAGE_Y-22}" text-anchor="middle" font-size="17" font-weight="bold" fill="{GREY}" letter-spacing="3">UPSTAGE  /  FUNDO DO PALCO</text>')
svg.append(f'<text x="{W/2}" y="{STAGE_Y+STAGE_H+38}" text-anchor="middle" font-size="17" font-weight="bold" fill="{GREY}" letter-spacing="3">DOWNSTAGE  /  FRENTE  •  PLATEIA</text>')

def numbadge(cx, cy, num):
    return (f'<circle cx="{cx}" cy="{cy}" r="13" fill="{GREEN}" stroke="{INK}" stroke-width="2"/>'
            f'<text x="{cx}" y="{cy+4.5}" text-anchor="middle" font-size="13" font-weight="bold" fill="{INK}">{num}</text>')

def amp(x, y, label, num):
    w,h=84,58
    s=[f'<g>']
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{PURPLE}" stroke="{INK}" stroke-width="2.5" rx="4"/>')
    for i in range(1,4):
        s.append(f'<line x1="{x+10}" y1="{y+h*i/4}" x2="{x+w-10}" y2="{y+h*i/4}" stroke="{INK}" stroke-width="1" opacity="0.35"/>')
    s.append(f'<text x="{x+w/2}" y="{y+h+16}" text-anchor="middle" font-size="12" font-weight="bold" fill="{CREAM}">{label}</text>')
    s.append(numbadge(x+w-8, y-8, num))
    s.append('</g>')
    return "".join(s)

def micstand(cx, cy, label="", num=None):
    s=[f'<g>']
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+26}" stroke="{CREAM}" stroke-width="3"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="{INK}" stroke="{CREAM}" stroke-width="3"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{GREEN}"/>')
    if label:
        s.append(f'<text x="{cx}" y="{cy+45}" text-anchor="middle" font-size="11" font-weight="bold" fill="{CREAM}">{label}</text>')
    if num is not None:
        s.append(numbadge(cx+16, cy-14, num))
    s.append('</g>')
    return "".join(s)

def musician(cx, cy, name, sub=""):
    s=[f'<g>']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="30" fill="{PURPLE}"/>')
    s.append(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12" font-weight="bold" fill="{INK}">{name}</text>')
    if sub:
        s.append(f'<text x="{cx}" y="{cy+48}" text-anchor="middle" font-size="11" fill="{GREY}">{sub}</text>')
    s.append('</g>')
    return "".join(s)

def drumkit(cx, cy, num):
    s=[f'<g>']
    s.append(f'<circle cx="{cx}" cy="{cy+22}" r="26" fill="{GREY}" stroke="{CREAM}" stroke-width="2.5"/>')
    s.append(f'<text x="{cx}" y="{cy+26}" text-anchor="middle" font-size="10" font-weight="bold" fill="{INK}">KICK</text>')
    s.append(f'<circle cx="{cx-34}" cy="{cy-2}" r="15" fill="#9a90ab" stroke="{CREAM}" stroke-width="2"/>')
    s.append(f'<text x="{cx-34}" y="{cy+2}" text-anchor="middle" font-size="8" font-weight="bold" fill="{INK}">SN</text>')
    s.append(f'<circle cx="{cx-8}" cy="{cy-30}" r="13" fill="#9a90ab" stroke="{CREAM}" stroke-width="2"/>')
    s.append(f'<circle cx="{cx+22}" cy="{cy-26}" r="13" fill="#9a90ab" stroke="{CREAM}" stroke-width="2"/>')
    s.append(f'<circle cx="{cx-52}" cy="{cy-34}" r="17" fill="none" stroke="{CREAM}" stroke-width="1.5"/>')
    s.append(f'<circle cx="{cx+50}" cy="{cy-30}" r="19" fill="none" stroke="{CREAM}" stroke-width="1.5"/>')
    s.append(f'<circle cx="{cx-58}" cy="{cy+8}" r="12" fill="none" stroke="{CREAM}" stroke-width="1.5"/>')
    s.append(f'<text x="{cx}" y="{cy+62}" text-anchor="middle" font-size="12" font-weight="bold" fill="{CREAM}">BATERIA</text>')
    s.append(numbadge(cx+90, cy-40, num))
    s.append('</g>')
    return "".join(s)

# ===== posicionamento =====
cx_gsolo = STAGE_X + 150
cx_baixo = STAGE_X + 360
cx_drums = STAGE_X + 560
cx_gbase = STAGE_X + 790

y_back  = STAGE_Y + 70    # amps / bateria
y_mid   = STAGE_Y + 250   # músicos
y_front = STAGE_Y + 440   # mics

content=[]
# amps no fundo
content.append(amp(cx_gsolo-42, y_back, "Guitarra Solo", 5))
content.append(amp(cx_baixo-42, y_back, "Baixo", 7))
content.append(amp(cx_gbase-42, y_back, "Guitarra Base", 6))
# bateria (centro, fundo)
content.append(drumkit(cx_drums, y_back+30, 8))
# músicos linha do meio
content.append(musician(cx_gsolo, y_mid, "GUIT.", "solo"))
content.append(musician(cx_baixo, y_mid, "BAIXO", ""))
content.append(musician(cx_gbase, y_mid, "GUIT.", "base"))
# vocal à frente, centro
content.append(musician(cx_drums, y_mid+130, "VOCAL", "à frente do palco"))
# mics (4): vocal + 3 backings (baixo não tem mic)
content.append(micstand(cx_drums, y_front+10, "Mic vocal", 1))
content.append(micstand(cx_gsolo, y_front, "Backing — guit. solo", 2))
content.append(micstand(cx_gbase, y_front, "Backing — guit. base", 3))
content.append(micstand(cx_drums-115, y_back+6, "Backing — bateria", 4))

svg.extend(content)

# PA na frente, fora do palco
pa_y = STAGE_Y+STAGE_H+8
for px0 in [STAGE_X+60, STAGE_X+STAGE_W-120]:
    svg.append(f'<polygon points="{px0},{pa_y} {px0+60},{pa_y} {px0+48},{pa_y+30} {px0+12},{pa_y+30}" fill="{PURPLE}" stroke="{INK}" stroke-width="2"/>')
    svg.append(f'<text x="{px0+30}" y="{pa_y+20}" text-anchor="middle" font-size="11" font-weight="bold" fill="{INK}">PA</text>')

# power indicators
for px in [STAGE_X+20, STAGE_X+STAGE_W-20]:
    py=STAGE_Y+18
    svg.append(f'<text x="{px}" y="{py+6}" text-anchor="middle" font-size="20" fill="{GREEN}">⚡</text>')
    svg.append(f'<text x="{px}" y="{STAGE_Y+44}" text-anchor="middle" font-size="9" fill="{GREY}">POWER</text>')

svg.append('</svg>')

open('assets/stageplot.svg','w').write("\n".join(svg))
print("svg ok")
