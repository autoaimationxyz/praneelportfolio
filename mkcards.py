# Builds the home-page card images so each creative shows in full.
import sys
from PIL import Image, ImageDraw, ImageFilter
root = sys.argv[1] if len(sys.argv) > 1 else '.'
W, H = 1280, 720
def rounded(im, r):
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.size[0]-1, im.size[1]-1), r, fill=255)
    out = Image.new('RGBA', im.size); out.paste(im, (0, 0), m); return out
def compose(srcs, dst, tint):
    ims = [Image.open(f'{root}/{s}').convert('RGB') for s in srcs]
    # background: blurred, darkened centre creative
    bg = ims[len(ims)//2].resize((W, int(W * ims[1].size[1] / ims[1].size[0])), Image.LANCZOS)
    top = (bg.size[1] - H) // 2; bg = bg.crop((0, top, W, top + H)).filter(ImageFilter.GaussianBlur(40))
    bg = Image.blend(bg, Image.new('RGB', (W, H), tint), .72).convert('RGBA')
    h = 620; gap = 28
    tiles = [rounded(im.resize((round(im.size[0] * h / im.size[1]), h), Image.LANCZOS), 22) for im in ims]
    tw = sum(t.size[0] for t in tiles) + gap * (len(tiles) - 1); x = (W - tw) // 2; y = (H - h) // 2
    for i, t in enumerate(tiles):
        sh = Image.new('RGBA', (t.size[0] + 60, t.size[1] + 60), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((30, 40, 30 + t.size[0], 40 + t.size[1]), 22, fill=(0, 0, 0, 150))
        sh = sh.filter(ImageFilter.GaussianBlur(14)); bg.alpha_composite(sh, (x - 30, y - 30))
        bg.alpha_composite(t, (x, y)); x += t.size[0] + gap
    bg.convert('RGB').save(f'{root}/{dst}', 'WEBP', quality=80, method=6)
def tall(vid):
    src = Image.open(f'{root}/assets/posters/{vid}.webp').convert('RGB')
    w, h = 720, 1280
    bg = src.resize((h, h), Image.LANCZOS).crop(((h - w) // 2, 0, (h - w) // 2 + w, h)).filter(ImageFilter.GaussianBlur(36))
    bg = Image.blend(bg, Image.new('RGB', (w, h), (6, 7, 14)), .45)
    fg = src.resize((w, round(src.size[1] * w / src.size[0])), Image.LANCZOS)
    bg.paste(fg, (0, (h - fg.size[1]) // 2))
    bg.save(f'{root}/assets/posters/{vid}-tall.webp', 'WEBP', quality=80, method=6)
for v in ['VAG4z1-SOzk', 'VAG4zysH5bw']:
    tall(v)
compose(['assets/creatives/IMG_8289.webp', 'assets/creatives/IMG_8299.webp', 'assets/creatives/IMG_8301.webp'], 'assets/card-signature-global.webp', (12, 18, 40))
compose(['assets/posters/VAG4z-OmH3o.webp', 'assets/posters/VAG4zvDab8s.webp', 'assets/posters/VAGmtyAPNbM.webp'], 'assets/card-creator-edits.webp', (14, 12, 10))
