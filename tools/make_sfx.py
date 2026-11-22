# makes the sound effects
# needs numpy + ffmpeg, run from project root: python3 tools/make_sfx.py
import subprocess
from pathlib import Path

import numpy as np

OUT = Path(__file__).resolve().parent.parent / "game" / "audio" / "sfx"
SR = 44100
rng = np.random.default_rng(420)


def t(secs):
    return np.arange(int(SR * secs)) / SR


def sweep(freq):
    return np.sin(2 * np.pi * np.cumsum(freq) / SR)


def noise(n, lo, hi):
    spec = np.fft.rfft(rng.standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR)
    spec[(f < lo) | (f > hi)] = 0
    out = np.fft.irfft(spec, n)
    return out / np.abs(out).max()


def vowel(pitch, formants):
    phase = np.cumsum(pitch) / SR
    out = np.zeros(len(pitch))
    for h in range(1, 28):
        f = h * pitch
        amp = sum(np.exp(-((f - c) / w) ** 2) for c, w in formants) + 0.04
        out += amp / h ** 0.4 * np.sin(2 * np.pi * h * phase)
    return out / np.abs(out).max()


def gap(secs):
    return np.zeros(int(SR * secs))


def error():
    x = t(0.17)
    beep = lambda f: np.sign(np.sin(2 * np.pi * f * x)) * np.minimum(1, (0.17 - x) * 40)
    return np.concatenate([beep(392), gap(0.05), beep(262), beep(262)])


def phone_ring():
    x = t(0.42)
    burst = (np.sin(2 * np.pi * 880 * x) + np.sin(2 * np.pi * 1100 * x)) * (np.sin(2 * np.pi * 22 * x) > 0)
    burst *= np.minimum(1, np.minimum(x, 0.42 - x) * 80)
    return np.concatenate([burst, gap(0.2), burst])


def zip_():
    x = t(0.65)
    teeth = (np.cumsum(35 + 190 * x) / SR) % 1
    return noise(len(x), 1300, 9000) * np.exp(-teeth * 5) * np.sin(np.pi * x / 0.65) ** 0.4


def thud():
    x = t(0.4)
    return sweep(45 + 110 * np.exp(-x * 22)) * np.exp(-x * 11) + 0.5 * noise(len(x), 80, 1400) * np.exp(-x * 45)


def thuds():
    one = thud()
    return np.concatenate([one, gap(0.05), one * 0.8, gap(0.05), one])


def sneeze():
    a = t(0.38)
    ah = vowel(170 + 220 * a, [(730, 170), (1150, 200), (2500, 300)]) * (a / 0.38) ** 1.5 * 0.6
    c = t(0.13)
    ch = noise(len(c), 2200, 9000) * np.exp(-c * 9)
    o = t(0.3)
    oo = vowel(330 - 420 * o, [(330, 130), (870, 170)]) * np.exp(-o * 9)
    oo += 0.35 * noise(len(o), 500, 5000) * np.exp(-o * 14)
    return np.concatenate([ah, gap(0.06), ch, oo])


def impact():
    x = t(1.3)
    boom = sweep(38 + 120 * np.exp(-x * 9)) * np.exp(-x * 3.5)
    crash = noise(len(x), 1500, 12000) * np.exp(-x * 6)
    chord = sum(2 * ((f * x) % 1) - 1 for f in (110, 164.8, 220, 277.2)) / 4 * np.exp(-x * 4)
    return boom + 0.45 * crash + 0.6 * chord


def scratch():
    x = t(0.6)
    move = np.abs(np.sin(2 * np.pi * 2.6 * x))
    grit = noise(len(x), 400, 5000) * move
    tone = sweep(250 + 1300 * move) * move
    return (grit + 0.5 * tone) * np.minimum(1, (0.6 - x) * 15)


def bounce():
    x = t(0.38)
    f = 170 + 520 * x + 40 * np.sin(2 * np.pi * 17 * x)
    return sweep(f) * np.exp(-x * 8) * np.minimum(1, x * 300)


SOUNDS = {
    "error": (error, 0.3),
    "phone_ring": (phone_ring, 0.35),
    "zip": (zip_, 0.6),
    "thud": (thud, 0.85),
    "thuds": (thuds, 0.85),
    "sneeze": (sneeze, 0.8),
    "impact": (impact, 0.85),
    "scratch": (scratch, 0.6),
    "bounce": (bounce, 0.6),
}

OUT.mkdir(parents=True, exist_ok=True)
for name, (make, vol) in SOUNDS.items():
    wave = make()
    wave[-660:] *= np.linspace(1, 0, 660)  # no click at the end
    wave = np.concatenate([gap(0.01), wave / np.abs(wave).max() * vol, gap(0.05)])
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-",
         "-b:a", "96k", str(OUT / f"{name}.mp3")],
        input=(wave * 32767).astype("<i2").tobytes(),
        check=True,
    )
    print("wrote", name)
