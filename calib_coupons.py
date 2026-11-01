"""
Calibration coupon generator for LightBurn relief work.

Makes two kinds of test images, both 16-bit grayscale PNGs with DPI set so
LightBurn imports them at true size:

  galvo  - for 3D Sliced mode (MOPA, Q-switched, UV). Ten flat square pads
           stepping from surface to full depth, sized for a dial-gauge tip,
           plus a continuous ramp and a fine-feature strip.
  gantry - for variable-power grayscale (CO2, diode, 1064 gantry). Ten power
           patches, a continuous ramp, and sharp edge bars that show how far
           a slow (glass) tube smears a power change along the scan direction.

Convention (LightBurn 3D Sliced default): darker = deeper. White = untouched
surface, black = full depth / full power.

Also writes a CSV log template for recording measured depths per pad.

Usage:
  python calib_coupons.py                      # defaults
  python calib_coupons.py --steps 12 --pad 6 --dpi 1000
"""
import argparse
import csv
import numpy as np
from PIL import Image, ImageDraw

MAX16 = 65535


def mm2px(mm, dpi):
    return int(round(mm / 25.4 * dpi))


def depth_to_gray(frac):
    """frac 0 = surface (white), 1 = full depth (black)."""
    return int(round((1.0 - frac) * MAX16))


def save16(arr, path, dpi):
    img = Image.fromarray(arr.astype(np.uint16))  # mode I;16
    img.save(path, dpi=(dpi, dpi))


def galvo_coupon(steps, pad_mm, gap_mm, dpi):
    cols = 5
    rows = int(np.ceil(steps / cols))
    pad, gap = mm2px(pad_mm, dpi), mm2px(gap_mm, dpi)
    ramp_h = mm2px(4, dpi)
    fine_h = mm2px(4, dpi)
    w = cols * pad + (cols + 1) * gap
    h = rows * pad + (rows + 1) * gap + ramp_h + gap + fine_h + gap
    a = np.full((h, w), MAX16, dtype=np.uint32)  # white surface

    fracs = [(i + 1) / steps for i in range(steps)]  # first pad already cut
    for i, f in enumerate(fracs):
        r, c = divmod(i, cols)
        y0 = gap + r * (pad + gap)
        x0 = gap + c * (pad + gap)
        a[y0:y0 + pad, x0:x0 + pad] = depth_to_gray(f)

    # continuous ramp, surface -> full depth, left to right
    y0 = gap + rows * (pad + gap)
    ramp = np.linspace(MAX16, 0, w - 2 * gap)
    a[y0:y0 + ramp_h, gap:w - gap] = ramp[None, :]

    # fine features at full depth: lines 0.05..0.5 mm wide, 1 mm apart
    y1 = y0 + ramp_h + gap
    x = gap
    for wmm in [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5]:
        lw = max(1, mm2px(wmm, dpi))
        if x + lw > w - gap:
            break
        a[y1:y1 + fine_h, x:x + lw] = 0
        x += lw + mm2px(1.0, dpi)

    return a, fracs, (w, h)


def gantry_coupon(steps, pad_mm, gap_mm, dpi):
    cols = 5
    rows = int(np.ceil(steps / cols))
    pad, gap = mm2px(pad_mm, dpi), mm2px(gap_mm, dpi)
    ramp_h = mm2px(5, dpi)
    edge_h = mm2px(8, dpi)
    w = cols * pad + (cols + 1) * gap
    h = rows * pad + (rows + 1) * gap + ramp_h + gap + edge_h + gap
    a = np.full((h, w), MAX16, dtype=np.uint32)

    fracs = [(i + 1) / steps for i in range(steps)]  # fraction of max power
    for i, f in enumerate(fracs):
        r, c = divmod(i, cols)
        y0 = gap + r * (pad + gap)
        x0 = gap + c * (pad + gap)
        a[y0:y0 + pad, x0:x0 + pad] = depth_to_gray(f)

    y0 = gap + rows * (pad + gap)
    ramp = np.linspace(MAX16, 0, w - 2 * gap)
    a[y0:y0 + ramp_h, gap:w - gap] = ramp[None, :]

    # edge-response bars: alternating 0% / 100% power bars of shrinking width.
    # Engrave with scan direction left-right; measure how far depth lags each edge.
    y1 = y0 + ramp_h + gap
    x = gap
    for wmm in [4, 3, 2, 1.5, 1, 0.75, 0.5, 0.35, 0.25]:
        bw = mm2px(wmm, dpi)
        if x + 2 * bw > w - gap:
            break
        a[y1:y1 + edge_h, x:x + bw] = 0
        x += 2 * bw

    return a, fracs, (w, h)


def preview(arr, path, title):
    """8-bit preview with pad labels, for viewing only (not for engraving)."""
    img = Image.fromarray((arr >> 8).astype(np.uint8)).convert("RGB")
    d = ImageDraw.Draw(img)
    d.text((6, 4), title, fill=(220, 40, 40))
    img.save(path)


def write_log(path, kind, fracs, machine_hint):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# machine", machine_hint])
        w.writerow(["# material (alloy / glass type+colour / stone)", ""])
        if kind == "galvo":
            w.writerow(["# recipe: power %, speed mm/s, freq kHz, pulse ns, line interval mm, "
                        "passes (slices), cleanup every N, Z step mm", ""])
        else:
            w.writerow(["# recipe: min power %, max power %, speed mm/s, line interval mm, "
                        "scan direction, passes", ""])
        w.writerow([])
        w.writerow(["pad", "target_fraction", "measured_depth_um_1",
                    "measured_depth_um_2", "measured_depth_um_3", "notes"])
        for i, f in enumerate(fracs, 1):
            w.writerow([i, f"{f:.3f}", "", "", "", ""])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps", type=int, default=10)
    ap.add_argument("--pad", type=float, default=5.0, help="pad size mm")
    ap.add_argument("--gap", type=float, default=2.0, help="gap mm")
    ap.add_argument("--dpi", type=int, default=1000)
    a = ap.parse_args()

    g, gf, gsize = galvo_coupon(a.steps, a.pad, a.gap, a.dpi)
    save16(g, "coupon_galvo_3dsliced.png", a.dpi)
    preview(g, "preview_galvo.png", "GALVO 3D Sliced - darker = deeper")
    write_log("log_galvo.csv", "galvo", gf, "MOPA / Q-switch / UV (LightBurn 3D Sliced)")

    t, tf, tsize = gantry_coupon(a.steps, a.pad, a.gap, a.dpi)
    save16(t, "coupon_gantry_grayscale.png", a.dpi)
    preview(t, "preview_gantry.png", "GANTRY grayscale - darker = more power")
    write_log("log_gantry.csv", "gantry", tf, "CO2 / diode / 1064 gantry (LightBurn grayscale)")

    for name, (w, h) in [("galvo", gsize), ("gantry", tsize)]:
        print(f"{name}: {w}x{h}px = {w/a.dpi*25.4:.1f} x {h/a.dpi*25.4:.1f} mm at {a.dpi} DPI")


if __name__ == "__main__":
    main()
