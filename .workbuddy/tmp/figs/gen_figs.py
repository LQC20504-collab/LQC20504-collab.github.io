"""Generate figures for the cellular-automata blog post.

Run with the Geo_New interpreter:
    /d/Users/20504/miniconda3/envs/Geo_New/python.exe gen_figs.py [name ...]

Only two exact colours are used for the CA rasters so the PNGs stay tiny.
Figure text is English/symbols only -- the zh and en posts share these files.
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
from PIL import Image, ImageDraw, ImageFont

ROOT = r"D:\Develop\github.io"
OUT = os.path.join(ROOT, "static", "images", "cellular-automata")
os.makedirs(OUT, exist_ok=True)

BG = "#F7F7F8"
FRAME = "#E9EBEE"
FG = "#1F2328"
GRAY = "#9AA0A6"
ACC_A = "#B4472E"
ACC_B = "#2F6F8F"

FONT_DIR = os.path.join(matplotlib.get_data_path(), "fonts", "ttf")
F_SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
F_SANS_B = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
F_MONO = os.path.join(FONT_DIR, "DejaVuSansMono.ttf")

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
    "text.color": FG,
})


# --------------------------------------------------------------------------- #
# rule engine
# --------------------------------------------------------------------------- #
def elementary(rule, steps, width, init="single", seed=7):
    """Space-time history of an elementary CA as uint8 array (steps x width)."""
    table = np.array([(rule >> k) & 1 for k in range(8)], dtype=np.uint8)
    cells = np.zeros(width, dtype=np.uint8)
    if init == "single":
        cells[width // 2] = 1
    else:
        rng = np.random.default_rng(seed)
        cells = rng.integers(0, 2, width).astype(np.uint8)
    hist = np.empty((steps, width), dtype=np.uint8)
    hist[0] = cells
    for t in range(1, steps):
        idx = (np.roll(cells, 1).astype(np.int64) << 2) \
              | (cells.astype(np.int64) << 1) | np.roll(cells, -1)
        cells = table[idx]
        hist[t] = cells
    return hist


def hist_to_img(hist, scale):
    """Two-colour nearest-neighbour upscale, stays crisp at any zoom."""
    palette = np.array([[0xF7, 0xF7, 0xF8], [0x1F, 0x23, 0x28]], dtype=np.uint8)
    rgb = palette[hist]
    small = Image.fromarray(rgb, "RGB")
    return small.resize((hist.shape[1] * scale, hist.shape[0] * scale),
                        Image.NEAREST)


def framed(img, pad=16):
    w, h = img.size
    canvas = Image.new("RGB", (w + 2 * pad, h + 2 * pad), FRAME)
    inner = Image.new("RGB", (w + 4, h + 4), BG)
    canvas.paste(inner, (pad - 2, pad - 2))
    canvas.paste(img, (pad, pad))
    return canvas


def save_pil(img, name):
    path = os.path.join(OUT, name)
    img.convert("P", palette=Image.ADAPTIVE, colors=32).save(path, optimize=True)
    print(f"  {name:22s} {img.size[0]}x{img.size[1]}  {os.path.getsize(path)/1024:6.1f} KB")


def save_mpl(fig, name, w, h):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor=BG)
    plt.close(fig)
    print(f"  {name:22s} {w}x{h}  {os.path.getsize(path)/1024:6.1f} KB")


def new_canvas(w, h):
    fig = plt.figure(figsize=(w / 100, h / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(h, 0)          # y grows downwards, like a screen
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), w, h, facecolor=BG, edgecolor="none", zorder=-10))
    ax.add_patch(Rectangle((8, 8), w - 16, h - 16, facecolor="none",
                           edgecolor=FRAME, linewidth=3, zorder=-5))
    return fig, ax


def bit_cell(ax, x, y, s, on, edge=FG, lw=1.6, z=2):
    ax.add_patch(Rectangle((x, y), s, s,
                           facecolor=FG if on else BG,
                           edgecolor=edge, linewidth=lw, zorder=z,
                           joinstyle="miter"))


# --------------------------------------------------------------------------- #
# 1. rule30.png
# --------------------------------------------------------------------------- #
def fig_rule30():
    hist = elementary(30, 100, 201)
    save_pil(framed(hist_to_img(hist, 7)), "rule30.png")


# --------------------------------------------------------------------------- #
# 2. four-classes.png
# --------------------------------------------------------------------------- #
def fig_four_classes():
    panels = [
        (234, "Class 1", "Rule 234"),
        (4, "Class 2", "Rule 4"),
        (90, "Class 3", "Rule 90"),
        (110, "Class 4", "Rule 110"),
    ]
    cols, rows = 240, 130
    scale = 3
    pw, ph = cols * scale, rows * scale
    gutter, margin, label_h = 24, 24, 44
    W = margin * 2 + pw * 2 + gutter
    H = margin * 2 + (label_h + ph) * 2 + 24

    canvas = Image.new("RGB", (W, H), FRAME)
    canvas.paste(Image.new("RGB", (W - 20, H - 20), BG), (10, 10))
    draw = ImageDraw.Draw(canvas)
    f_label = ImageFont.truetype(F_SANS_B, 20)
    f_rule = ImageFont.truetype(F_MONO, 20)

    for i, (rule, cls, rname) in enumerate(panels):
        cx = margin + (i % 2) * (pw + gutter)
        cy = margin + (i // 2) * (label_h + ph + 24)
        hist = elementary(rule, rows, cols, init="random", seed=11)
        canvas.paste(hist_to_img(hist, scale), (cx, cy + label_h))
        draw.text((cx, cy + 6), cls, font=f_label, fill=FG)
        draw.text((cx + 110, cy + 8), "\u00b7 " + rname, font=f_rule, fill=GRAY)
    save_pil(canvas, "four-classes.png")


# --------------------------------------------------------------------------- #
# 3. life-glider.png
# --------------------------------------------------------------------------- #
GLIDER = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]


def life_step(alive):
    counts = {}
    for (x, y) in alive:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                p = (x + dx, y + dy)
                counts[p] = counts.get(p, 0) + 1
    return {p for p, n in counts.items() if n == 3 or (n == 2 and p in alive)}


def fig_life_glider():
    n, cell = 8, 28
    pw = n * cell                 # 224
    gap = 54                      # space reserved for the arrow
    step = pw + gap               # 278
    n_panels = 5
    x0 = 52
    strip_w = (n_panels - 1) * step + pw
    W = x0 * 2 + strip_w
    y_top = 104
    H = y_top + pw + 104
    fig, ax = new_canvas(W, H)

    panels, alive = [], set(GLIDER)
    for gen in range(n_panels):
        panels.append((gen, set(alive)))
        alive = life_step(alive)

    for idx, (gen, state) in enumerate(panels):
        px = x0 + idx * step
        ax.text(px + pw / 2, 76, f"gen {gen}", ha="center", va="center",
                fontsize=13, color=FG if idx == 0 else GRAY,
                family="DejaVu Sans Mono")
        for r in range(n + 1):
            ax.plot([px, px + pw], [y_top + r * cell] * 2,
                    color="#D9DBDE", linewidth=1, zorder=1)
            ax.plot([px + r * cell] * 2, [y_top, y_top + pw],
                    color="#D9DBDE", linewidth=1, zorder=1)
        ax.add_patch(Rectangle((px, y_top), pw, pw, facecolor="none",
                               edgecolor=GRAY, linewidth=1.5, zorder=2))
        for (cx_, cy_) in state:
            ax.add_patch(Rectangle((px + cx_ * cell, y_top + cy_ * cell),
                                   cell, cell, facecolor=FG,
                                   edgecolor=FG, linewidth=1, zorder=3))
        if idx == 0:
            ax.add_patch(Rectangle((px - 6, y_top - 6), pw + 12, pw + 12,
                                   facecolor="none", edgecolor=ACC_A,
                                   linewidth=2, linestyle=(0, (5, 3)), zorder=5))
        if idx < n_panels - 1:
            ax.add_patch(FancyArrowPatch((px + pw + 12, y_top + pw / 2),
                                         (px + pw + gap - 10, y_top + pw / 2),
                                         arrowstyle="-|>", mutation_scale=15,
                                         color=GRAY, linewidth=2, zorder=6))

    ax.text(x0 + 4 * step + pw / 2, y_top + pw + 40,
            "same five cells, shifted (1, 1)", ha="center", va="center",
            fontsize=13, color=ACC_A)
    ax.text(W / 2, y_top + pw + 78,
            "B3/S23   \u00b7   a glider returns to its own shape every 4 generations, "
            "one cell further along the diagonal",
            ha="center", va="center", fontsize=12, color=GRAY,
            family="DejaVu Sans Mono")
    save_mpl(fig, "life-glider.png", W, H)


# --------------------------------------------------------------------------- #
# 4. lambda.png
# --------------------------------------------------------------------------- #
def fig_lambda():
    W, H = 1440, 640
    fig, ax = new_canvas(W, H)

    ones = np.array([bin(r).count("1") for r in range(256)])
    lam = ones / 8.0
    counts = np.array([int((lam == k / 8).sum()) for k in range(9)])

    left, right = 150, 1290
    top, bottom = 170, 460
    slot = (right - left) / 9
    bw = slot * 0.60
    ymax = counts.max() * 1.42

    def ypos(v):
        return bottom - (v / ymax) * (bottom - top)

    ax.text(left - 30, 96,
            "how many of the 256 elementary rules have each lambda",
            ha="left", va="center", fontsize=14, color=FG)

    for k in range(9):
        cx = left + (k + 0.5) * slot
        v = counts[k]
        ax.add_patch(Rectangle((cx - bw / 2, ypos(v)), bw, bottom - ypos(v),
                               facecolor=ACC_A if k == 4 else "#C9CDD2",
                               edgecolor="none", zorder=3))
        ax.text(cx, ypos(v) - 12, str(v), ha="center", va="bottom",
                fontsize=13, color=ACC_A if k == 4 else GRAY,
                family="DejaVu Sans Mono")
        ax.text(cx, bottom + 26, f"{k}/8", ha="center", va="center",
                fontsize=13, color=FG if k == 4 else GRAY,
                family="DejaVu Sans Mono")

    ax.plot([left - 20, right + 20], [bottom, bottom], color=GRAY, linewidth=2)
    ax.text((left + right) / 2, bottom + 66, "lambda", ha="center", va="center",
            fontsize=14, color=FG, family="DejaVu Sans Mono")

    cx4 = left + 4.5 * slot
    ax.text(cx4, ypos(counts[4]) - 46,
            "70 of 256 rules share this single value",
            ha="center", va="bottom", fontsize=13, color=ACC_A)

    ax.text(W / 2, H - 46,
            "Rule 30 (class 3)  \u00b7  Rule 90 (class 3)  \u00b7  Rule 54 (class 4)"
            "   \u2014   one bucket, several different fates",
            ha="center", va="center", fontsize=12, color=GRAY,
            family="DejaVu Sans Mono")
    save_mpl(fig, "lambda.png", W, H)


# --------------------------------------------------------------------------- #
# 5. ca-anatomy.png
# --------------------------------------------------------------------------- #
def fig_anatomy():
    W, H = 1440, 620
    fig, ax = new_canvas(W, H)

    rule = 30
    table = [(rule >> k) & 1 for k in range(8)]

    # ---- left: time t and t+1 -------------------------------------------
    cell, gap = 56, 10
    x0 = 46
    t_state = [0, 0, 0, 1, 0, 0, 0]
    t1_state = [0, 0, 1, 1, 1, 0, 0]

    ax.text(x0, 60, "time t", fontsize=13, color=GRAY, family="DejaVu Sans Mono")
    for i, v in enumerate(t_state):
        bit_cell(ax, x0 + i * (cell + gap), 84, cell, v)
    ax.add_patch(Rectangle((x0 + 2 * (cell + gap) - 7, 84 - 7),
                           3 * cell + 2 * gap + 14, cell + 14,
                           facecolor="none", edgecolor=ACC_A, linewidth=2.4,
                           linestyle=(0, (5, 3)), zorder=6))
    for i, lab in [(2, "i\u22121"), (3, "i"), (4, "i+1")]:
        ax.text(x0 + i * (cell + gap) + cell / 2, 166, lab,
                ha="center", va="center", fontsize=13, color=ACC_A,
                family="DejaVu Sans Mono")

    bx1 = x0 + 2 * (cell + gap) - 7
    bx2 = x0 + 5 * (cell + gap) - gap + 7
    ax.plot([bx1, bx2], [188, 188], color=ACC_A, linewidth=2)
    ax.plot([(bx1 + bx2) / 2] * 2, [188, 206], color=ACC_A, linewidth=2)
    ax.text(x0, 232, "three cells decide one", fontsize=13, color=FG)
    ax.text(x0, 258, "there is no other input", fontsize=13, color=GRAY)

    ax.text(x0, 306, "time t + 1", fontsize=13, color=GRAY,
            family="DejaVu Sans Mono")
    for i, v in enumerate(t1_state):
        bit_cell(ax, x0 + i * (cell + gap), 330, cell, v,
                 edge=ACC_A if 2 <= i <= 4 else FG,
                 lw=2.4 if 2 <= i <= 4 else 1.6)
    ax.text(x0, 424, "one cell in, three cells out", fontsize=13, color=FG)
    ax.text(x0, 450, "the rule is applied to every", fontsize=13, color=GRAY)
    ax.text(x0, 476, "cell at the same time, every step", fontsize=13, color=GRAY)

    # ---- arrow into the rule table --------------------------------------
    ax.add_patch(FancyArrowPatch((x0 + 7 * (cell + gap) - gap + 16, 112),
                                 (640 - 40, 112),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=GRAY, linewidth=2.2))

    # ---- right: the 8-row rule table ------------------------------------
    tx = 640
    rh, s = 46, 34
    y0 = 96
    ax.text(tx, 64, "neighbourhood", fontsize=12, color=GRAY)
    ax.text(tx + 222, 64, "next", fontsize=12, color=GRAY)

    for k in range(7, -1, -1):
        row = 7 - k
        y = y0 + row * rh
        bits = [(k >> 2) & 1, (k >> 1) & 1, k & 1]
        ax.text(tx, y + s / 2, "".join(str(b) for b in bits), va="center",
                fontsize=12, color=GRAY, family="DejaVu Sans Mono")
        for j, b in enumerate(bits):
            bit_cell(ax, tx + 62 + j * (s + 6), y, s, b)
        ax.text(tx + 194, y + s / 2, "\u2192", va="center", fontsize=14,
                color=GRAY)
        out = table[k]
        ax.add_patch(Rectangle((tx + 222, y), s, s,
                               facecolor=ACC_A if out else BG,
                               edgecolor=ACC_A if out else FG,
                               linewidth=2.4 if out else 1.6, zorder=2))

    # the rule number, spelled out
    ax.text(tx, y0 + 8 * rh + 34, "outputs, read from 111 down to 000",
            fontsize=12, color=GRAY)
    ax.text(tx, y0 + 8 * rh + 74, "00011110  =  30", fontsize=24, color=ACC_A,
            family="DejaVu Sans Mono")
    ax.text(tx, y0 + 8 * rh + 112, "eight bits, one byte, one rule",
            fontsize=12, color=GRAY)

    save_mpl(fig, "ca-anatomy.png", W, H)


FIGS = {
    "rule30": fig_rule30,
    "four-classes": fig_four_classes,
    "life-glider": fig_life_glider,
    "lambda": fig_lambda,
    "ca-anatomy": fig_anatomy,
}

if __name__ == "__main__":
    wanted = sys.argv[1:] or list(FIGS)
    for key in wanted:
        print(f"[{key}]")
        FIGS[key]()
    print("done ->", OUT)
