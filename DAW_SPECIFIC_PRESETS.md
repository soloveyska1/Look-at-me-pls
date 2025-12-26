# 🎛️ DAW-СПЕЦИФИЧНЫЕ НАСТРОЙКИ
## Готовые пресеты для FL Studio, Ableton, Logic Pro

---

## 🍊 FL STUDIO 21+ НАСТРОЙКИ

### MIXER TRACK SETUP (Инструментал)

```
SLOT 1: Fruity Parametric EQ 2 (Static EQ - Cleanup)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Band 1 (High-Pass):
  └─ 30 Hz, Type: High Pass, Order: 8

Band 2 (Low-Mid Cut 1):
  ├─ Freq: 220 Hz
  ├─ Gain: -2.5 dB
  ├─ Q: 1.5
  └─ Type: Peaking

Band 3 (Low-Mid Cut 2 - ГЛАВНАЯ!):
  ├─ Freq: 350 Hz
  ├─ Gain: -3 dB
  ├─ Q: 2.0
  └─ Type: Peaking

Band 4 (Low-Mid Cut 3):
  ├─ Freq: 480 Hz
  ├─ Gain: -2 dB
  ├─ Q: 1.8
  └─ Type: Peaking

Band 5 (High Shelf - Air):
  ├─ Freq: 10 kHz
  ├─ Gain: +2.5 dB
  ├─ Q: 0.7
  └─ Type: High Shelf


SLOT 2: Maximus (Multiband Sidechain)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOW BAND (до 200 Hz):
  Comp Tab:
  ├─ Ratio: 1:1 (bypass compression)
  ├─ Knee: 0
  └─ Attack/Release: Fast

MID BAND (200 Hz - 2 kHz) - ОСНОВНОЙ SIDECHAIN:
  Comp Tab:
  ├─ Threshold: -18 dB
  ├─ Ratio: 6:1
  ├─ Knee: 3
  ├─ Attack: 10 ms
  ├─ Release: 80 ms
  ├─ Gain: +2 dB (makeup)
  └─ SIDECHAIN: включить, Route от вокальной дорожки

HIGH BAND (2 kHz+):
  Comp Tab:
  ├─ Threshold: -22 dB
  ├─ Ratio: 3:1
  ├─ Knee: 2
  ├─ Attack: 10 ms
  ├─ Release: 80 ms
  └─ SIDECHAIN: включить, Route от вокальной дорожки

Master:
  └─ Output Gain: -1 dB (headroom)


SLOT 3: Fruity Limiter (Sidechain Компрессор)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMP Tab:
├─ Threshold: -18 dB
├─ Ratio: 4.0
├─ Knee: 0.3
├─ Attack: 10 ms
├─ Release: 80 ms
├─ Gain: +3 dB
└─ SIDECHAIN: Right-click → "Sidechain to this track"
             Select: Вокальная дорожка

MISC Tab:
└─ Band Filter: Band-Pass 200-400 Hz (sidechain filter)


SLOT 4: Fruity Stereo Shaper
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Low (до 200 Hz):
  └─ Stereo Sep: 0% (MONO)

Mid (200 Hz - 2 kHz):
  └─ Stereo Sep: 85%

High (2 kHz - 8 kHz):
  └─ Stereo Sep: 120%

Top (8 kHz+):
  └─ Stereo Sep: 150%

Phase:
  └─ Offset: 0%
  └─ Invert: OFF


SLOT 5: Vintage Chorus/Phaser (для ширины - опционально)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Только на Hi-hats/Percs:
├─ Rate: 0.15 Hz
├─ Depth: 15%
├─ Mix: 20%
└─ Stereo: 100%


SLOT 6: Fruity Fast Distortion (Saturation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pre-Band:
  ├─ Frequency: 100 Hz (HPF для saturation)
  └─ Band: 8 kHz (LPF для saturation)

Mix:
  └─ 25% (parallel saturation)

Threshold:
  └─ 35%

Post:
  └─ +0 dB


SLOT 7: SSL Comp (или Vintage Compressor - если есть)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ratio: 2:1
Threshold: -8 dB
Attack: 10 ms
Release: Auto (или 250 ms)
Makeup: +2 dB
Target GR: -1 to -3 dB


SLOT 8: Fruity Limiter (Safety Limiter - НЕ ДАВИТЬ!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ceiling: -1 dB
Threshold: -6 dB (soft limiting)
Release: 10 ms
ATT (Saturation): 0
```

---

### FL STUDIO - LAYERING HI-HATS

```
CHANNEL RACK:
┌─────────────────────────────────────────────┐
│ Hi-Hat Main (original)                      │
│   └─ Volume: 80%                            │
│   └─ Pan: Center                            │
│                                             │
│ Hi-Hat Layer 1 (FPC/DirectWave)             │
│   └─ Sample: Crisp closed hat               │
│   └─ Volume: 60%                            │
│   └─ Pan: -10% (left)                       │
│   └─ Pitch: +200 cents (ярче)               │
│                                             │
│ Hi-Hat Layer 2 (FPC/DirectWave)             │
│   └─ Sample: Shaker или open hat            │
│   └─ Volume: 40%                            │
│   └─ Pan: +15% (right)                      │
│   └─ Pattern: 16th notes shuffle            │
└─────────────────────────────────────────────┘

MIXER ROUTING:
All Hi-Hats → Track 15 "Hi-Hats Group"

Track 15 Effects:
├─ Slot 1: EQ - High-Pass 5 kHz, Boost +3 dB @ 10 kHz
├─ Slot 2: Compressor - 8:1, Attack 0.1ms, Release 50ms
├─ Slot 3: Stereo Shaper - 150% на 8+ kHz
└─ Slot 4: Reverb - Room, Size 20%, Damping 70%, Mix 8%
```

---

### FL STUDIO - 808 SLIDES SETUP

```
CHANNEL RACK - 808 Bass:
┌─────────────────────────────────────────────┐
│ Main 808 Pattern (ROOT notes)               │
│   └─ В Piano Roll: обычный паттерн          │
│                                             │
│ 808 Slide Pattern (каждые 4 бара)          │
│   └─ Piano Roll Settings:                   │
│       ├─ Pitch: +12 semitones                │
│       ├─ Slide: включить (porta icon)       │
│       ├─ Slide Time: 100-150 ms             │
│       └─ Velocity: 80%                       │
└─────────────────────────────────────────────┘

MIXER - 808 Track:
Slot 1: Fruity Parametric EQ 2
  ├─ Low-Pass: 5 kHz (убрать высокие щелчки)
  ├─ Boost: +2 dB @ 80-100 Hz
  └─ Cut: -1 dB @ 200-300 Hz (чистота)

Slot 2: Fruity Fast Dist (опционально)
  └─ Mix: 10-15%, Threshold: 40%
```

---

## 🎹 ABLETON LIVE 12 НАСТРОЙКИ

### AUDIO EFFECT RACK (Инструментал Track)

```
DEVICE 1: EQ Eight (Static Cleanup)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Band 1 (High-Pass):
  ├─ 30 Hz, Slope: 48 dB/oct
  └─ Type: High-Cut (активировать)

Band 2:
  ├─ Freq: 220 Hz
  ├─ Gain: -2.5 dB
  ├─ Q: 1.5
  └─ Type: Bell

Band 3:
  ├─ Freq: 350 Hz
  ├─ Gain: -3 dB
  ├─ Q: 2.0
  └─ Type: Bell

Band 4:
  ├─ Freq: 480 Hz
  ├─ Gain: -2 dB
  ├─ Q: 1.8
  └─ Type: Bell

Band 8 (High Shelf):
  ├─ Freq: 10 kHz
  ├─ Gain: +2.5 dB
  └─ Type: High Shelf


DEVICE 2: Compressor (Sidechain от вокала)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Main:
├─ Ratio: 4:1
├─ Threshold: -18 dB
├─ Attack: 10 ms
├─ Release: 80 ms
├─ Knee: 3 dB
└─ Makeup: +3 dB (Auto-Gain OFF)

Sidechain:
├─ Enable: ON
├─ Audio From: Vocal Track
├─ EQ Mode: Frequency
├─ Filter: Band-Pass
├─ Freq Lo: 200 Hz
└─ Freq Hi: 400 Hz


DEVICE 3: Multiband Dynamics (Продвинутый Sidechain)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Low Band (до 200 Hz):
  └─ Bypass компрессию (или легкая 2:1)

Mid Band (200 Hz - 2 kHz):
  ├─ Threshold: -20 dB
  ├─ Ratio: 6:1
  ├─ Attack: 5 ms
  ├─ Release: 60 ms
  ├─ Makeup: +2 dB
  └─ Sidechain: ON, от вокала

High Band (2 kHz+):
  ├─ Threshold: -24 dB
  ├─ Ratio: 3:1
  ├─ Attack: 10 ms
  ├─ Release: 80 ms
  └─ Sidechain: ON, от вокала


DEVICE 4: Utility (Stereo Control)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Width: 110% (или используй M/S processing)


DEVICE 5: Saturator (Warmth)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: Warm Tube
Drive: 3-5 dB
Dry/Wet: 40%
Output: -2 dB


DEVICE 6: Glue Compressor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Attack: Fast (10 ms)
Release: Auto
Ratio: 2:1
Threshold: -8 dB
Makeup: +2 dB
Range: 0 to -3 dB
Dry/Wet: 100%


DEVICE 7: Limiter (Safety)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ceiling: -1 dB
Gain: 0 dB (не пуши!)
Release: 10 ms
```

---

### ABLETON - HI-HAT ENHANCEMENT RACK

```
RETURN TRACK "Hi-Hat Parallel"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. EQ Eight:
   └─ High-Pass: 8 kHz, 48 dB/oct

2. Saturator:
   ├─ Type: Tube
   ├─ Drive: +8 dB
   └─ Dry/Wet: 60%

3. Compressor:
   ├─ Ratio: 8:1
   ├─ Attack: 0.1 ms
   ├─ Release: 50 ms
   └─ Threshold: -12 dB

4. EQ Eight:
   ├─ Boost: +3 dB @ 12 kHz, Q: 1.2
   └─ Boost: +2 dB @ 16 kHz, Q: 0.8

5. Utility:
   └─ Width: 150% (только 10+ kHz с помощью EQ)

Send Level от Hi-Hat дорожки: 30-40%
```

---

### ABLETON - AUTOMATION CLIPS

```
AUTOMATION 1: Hi-Hat Volume (каждые 8 баров)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pattern:
Bar 1-4:   0 dB (normal)
Bar 5-7:   +1 dB (build)
Bar 8:     +2 dB (peak)
Bar 9:     0 dB (drop)


AUTOMATION 2: HPF Sweep (перед хуками)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
На EQ Eight - Band 1 Frequency:
Bar -2:     30 Hz (start)
Bar -1:     200 Hz (building)
Last Beat:  500 Hz (tension peak)
Drop:       30 Hz (instant drop)


AUTOMATION 3: Reverb Send (эффект на переходах)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Normal:     10% send
Transition: 30% send (1 beat spike)
After:      10% send (fade back)
```

---

## 🍎 LOGIC PRO X НАСТРОЙКИ

### CHANNEL STRIP (Инструментал)

```
INSERT 1: Channel EQ (Static Cleanup)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Band 1 (High-Pass):
  ├─ 30 Hz, Slope: 24 dB/oct
  └─ Enable: ON

Band 2 (Low-Mid 1):
  ├─ Freq: 220 Hz
  ├─ Gain: -2.5 dB
  ├─ Q: 1.5
  └─ Shape: Parametric

Band 3 (Low-Mid 2):
  ├─ Freq: 350 Hz
  ├─ Gain: -3 dB
  ├─ Q: 2.0
  └─ Shape: Parametric

Band 4 (Low-Mid 3):
  ├─ Freq: 480 Hz
  ├─ Gain: -2 dB
  ├─ Q: 1.8
  └─ Shape: Parametric

Band 8 (High Shelf):
  ├─ Freq: 10 kHz
  ├─ Gain: +2.5 dB
  └─ Q: 0.7


INSERT 2: Compressor (Sidechain)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Circuit Type: Platinum
Ratio: 4:1
Threshold: -18 dB
Attack: 10 ms
Release: 80 ms
Knee: 3
Gain: +3 dB
Auto Gain: OFF

Sidechain:
├─ Enable: ON
├─ Input: Vocal Track
├─ Filter: ON
├─ Mode: Band Pass
├─ Freq: 300 Hz (center)
└─ Q: 1.0


INSERT 3: Multipressor (Multiband Sidechain)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Crossovers:
├─ Low/Low-Mid: 200 Hz
├─ Low-Mid/High-Mid: 2 kHz
└─ High-Mid/High: 8 kHz

Low Band (до 200 Hz):
  └─ Bypass или Ratio: 1.5:1

Low-Mid Band (200 Hz - 2 kHz):
  ├─ Threshold: -20 dB
  ├─ Ratio: 6:1
  ├─ Attack: 5 ms
  ├─ Release: 60 ms
  ├─ Makeup: +2 dB
  └─ Sidechain: ON (от вокала)

High-Mid Band (2-8 kHz):
  ├─ Threshold: -24 dB
  ├─ Ratio: 3:1
  ├─ Attack: 10 ms
  ├─ Release: 80 ms
  └─ Sidechain: ON (от вокала)

High Band (8+ kHz):
  └─ Bypass


INSERT 4: Direction Mixer (Stereo Width)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mode: LR (Left/Right)
Spread: 110-120%
LFE: OFF


INSERT 5: Exciter (Top-End Enhancement)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Frequency: 8 kHz
Harmonics: 25-35%
Mix: 25%


INSERT 6: Vintage Console EQ (Saturation + EQ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Model: US (SSL style)
Drive: 2.5 (moderate saturation)
Output: -1 dB


INSERT 7: Compressor (SSL-style Glue)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Circuit Type: Platinum или VCA
Ratio: 2:1
Threshold: -8 dB
Attack: 10-30 ms
Release: Auto
Knee: 0
Gain: +2 dB
Mix: 100%
Target GR: -1 to -3 dB


INSERT 8: Adaptive Limiter (Safety)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mode: Optimize
Out Ceiling: -1.0 dB
Gain: 0 dB (не пуши сильно!)
Release: 10 ms
```

---

### LOGIC PRO - HI-HAT LAYERING

```
SUMMING STACK "Hi-Hats"
┌─────────────────────────────────────────────┐
│ Track 1: Main Hi-Hat                        │
│   └─ Volume: 0 dB                           │
│                                             │
│ Track 2: Crispy Layer (Ultrabeat/EXS24)    │
│   └─ Sample: Bright closed hat              │
│   └─ Volume: -6 dB                          │
│   └─ Pan: -12°                              │
│   └─ Transpose: +200 cents                  │
│                                             │
│ Track 3: Shaker (Ultrabeat)                │
│   └─ Pattern: 16th shuffle                  │
│   └─ Volume: -12 dB                         │
│   └─ Pan: +15°                              │
└─────────────────────────────────────────────┘

Summing Stack Output Insert:
├─ Channel EQ: HPF 5 kHz, +3 dB @ 10 kHz
├─ Compressor: 8:1, 0.1ms attack, -12 dB threshold
├─ Stereo Spread: 140%
└─ Space Designer: Small Room, 8% mix
```

---

### LOGIC PRO - SMART CONTROLS MAPPING

```
Для быстрой настройки sidechain и EQ:

SMART CONTROL 1: "Vocal Pocket Depth"
└─ Maps to: Compressor Threshold (-25 to -15 dB range)

SMART CONTROL 2: "Low-Mid Cut"
└─ Maps to: EQ Band 3 Gain (0 to -5 dB)

SMART CONTROL 3: "High-End Air"
└─ Maps to: EQ High Shelf Gain (0 to +4 dB)

SMART CONTROL 4: "Stereo Width"
└─ Maps to: Direction Mixer Spread (80% to 150%)

SMART CONTROL 5: "Saturation"
└─ Maps to: Vintage Console Drive (0 to 5)
```

---

## 🎚️ UNIVERSAL PLUGIN CHAINS (любая DAW)

### FABFILTER PRO-Q 3 - PRESET "VOCAL POCKET DYNAMIC"

```
ТОЧНЫЕ НАСТРОЙКИ (скопируй значения):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Enable: Dynamic EQ Mode

Band 1:
├─ Frequency: 280 Hz
├─ Gain: 0 dB (static)
├─ Q: 2.5
├─ Shape: Bell
├─ Dynamic: ON
├─ Threshold: -18 dB
├─ Range: -4.0 dB
├─ Attack: 10 ms
├─ Release: 60 ms
├─ Sidechain: External → Vocal Track
└─ SC Filter: 200-500 Hz

Band 2:
├─ Frequency: 420 Hz
├─ Q: 1.8
├─ Dynamic: ON
├─ Threshold: -20 dB
├─ Range: -3.5 dB
├─ Attack: 10 ms
├─ Release: 60 ms
└─ Sidechain: External → Vocal Track

Band 3:
├─ Frequency: 1200 Hz
├─ Q: 2.0
├─ Dynamic: ON
├─ Threshold: -22 dB
├─ Range: -2.5 dB
├─ Attack: 10 ms
├─ Release: 70 ms
└─ Sidechain: External → Vocal Track

Band 4:
├─ Frequency: 2500 Hz
├─ Q: 1.5
├─ Dynamic: ON
├─ Threshold: -24 dB
├─ Range: -2.0 dB
├─ Attack: 10 ms
├─ Release: 80 ms
└─ Sidechain: External → Vocal Track

Band 5:
├─ Frequency: 5500 Hz
├─ Q: 1.2
├─ Dynamic: ON
├─ Threshold: -25 dB
├─ Range: -1.5 dB
├─ Attack: 15 ms
├─ Release: 90 ms
└─ Sidechain: External → Vocal Track

Global:
├─ Output Gain: 0 dB
├─ Phase: Linear (для точности)
└─ Auto Gain: OFF
```

---

### WAVES SSL G-MASTER BUSS COMPRESSOR

```
PRESET: "Hip-Hop Glue"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Attack: 10 (medium-fast)
Release: Auto (или 4 = ~250ms)
Ratio: 2:1
Threshold: -8 dB
Makeup Gain: +2 dB

Analog:
└─ Enable: ON (для warmth)

Target:
└─ Gain Reduction: -1 to -3 dB (subtle!)
```

---

### OZONE IMAGER - PRESET "HIP-HOP WIDE"

```
MULTIBAND STEREO WIDTH:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Band 1 (20-120 Hz):
  ├─ Width: 0% (MONO!)
  └─ Stereoize: OFF

Band 2 (120-500 Hz):
  ├─ Width: 70%
  └─ Stereoize: OFF

Band 3 (500 Hz - 2 kHz):
  ├─ Width: 85%
  └─ Stereoize: Light (5-10%)

Band 4 (2-8 kHz):
  ├─ Width: 120%
  └─ Stereoize: Moderate (15%)

Band 5 (8+ kHz):
  ├─ Width: 150%
  └─ Stereoize: Heavy (25%)
```

---

## 🎹 MIDI PROGRAMMING - HI-HAT PATTERNS

### MODERN TRAP HI-HAT PATTERN (для программирования)

```
BASIC PATTERN (16th notes):
Beat: 1   e   &   a   2   e   &   a   3   e   &   a   4   e   &   a
Note: C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5
Vel:  80  60  70  55  85  60  70  55  80  60  70  55  85  60  75  60
Pan:  C   L5  R3  L2  C   L5  R3  L2  C   L5  R3  L2  C   L5  R3  L2

VARIATION 1 (half-time roll - каждые 4 бара):
Beat: 1   e   &   a   2   e   &   a   3   e   &   a   4   e   &   a
Note: C5  -   C5  C5  C5  C5  C5  C5  C5  -   C5  C5  C5  C5  C5  C5
Vel:  80      70  60  75  65  70  60  85      75  65  80  70  75  65

VARIATION 2 (triplet - для flow change):
Beat: 1       &       2       &       3       &       4       &
Note: C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5  C5
      (triplets - 12 нот на бар вместо 16)
Vel:  85  70  60  85  70  60  90  75  65  85  70  60  90  75  70  65

HUMANIZATION (randomize):
├─ Velocity: ±5-10%
├─ Timing: ±5-15 ticks (swing/shuffle)
└─ Pitch: ±50 cents (на некоторых нотах для органики)
```

---

### 808 SLIDE PROGRAMMING

```
ОСНОВНОЙ ПАТТЕРН (C minor key example):
Bar 1:  C2  -   -   -   |  -   -   -   -   |  Eb2 -   -   -   |  -   -   -   -
Bar 2:  G2  -   -   -   |  -   -   -   -   |  F2  -   -   -   |  -   -   -   -

SLIDE VARIATION (каждые 4 бара):
Bar 3:  C2  -   -   -   |  C3[SLIDE] -  -  |  Eb2 -   -   -   |  -   -   -   -
        └─── Slide Time: 100-150ms ────┘

VELOCITY PROGRAMMING:
Main notes:     Velocity 100-110
Slide notes:    Velocity 85-95 (чуть тише)
Ghost notes:    Velocity 60-70 (для грува)

ARTICULATION MIDI CC:
CC74 (Filter Cutoff): Automate 0-127 на slides для movement
```

---

## 💾 SAVE THESE PRESETS

### FL STUDIO
```
Mixer Preset: Сохрани в:
C:\Users\[YOU]\Documents\Image-Line\FL Studio\Presets\Mixer presets\
Название: "Metro_Vocal_Pocket.fst"
```

### ABLETON
```
Audio Effect Rack: Сохрани в:
~/Music/Ableton/User Library/Presets/Audio Effects/Audio Effect Rack/
Название: "Metro Boomin Vocal Pocket.adg"
```

### LOGIC PRO
```
Channel Strip Setting: Сохрани в:
~/Music/Audio Music Apps/Channel Strip Settings/
Название: "Metro - Instrumental + Sidechain.cst"
```

---

## ⚡ HOTKEYS & WORKFLOW

### FL STUDIO
```
Ctrl + L          = Link to mixer track
F9               = Mixer window
Alt + C          = Clone track (для layering)
Ctrl + B         = Browse samples (для hi-hats)
Alt + R          = Render selection
```

### ABLETON
```
Cmd/Ctrl + G     = Group tracks
Cmd/Ctrl + J     = Consolidate (bounce)
Cmd/Ctrl + E     = Enable/Disable effect
Cmd/Ctrl + M     = MIDI Map (для automation)
0 (zero)         = Activator (bypass all effects)
```

### LOGIC PRO
```
Cmd + D          = Duplicate track
X                = Bypass insert
Opt + Cmd + E    = Environment (routing)
Cmd + K          = Smart Controls (quick access)
Ctrl + Cmd + N   = Normalize
```

---

**ВАЖНО:** Сохрани все эти пресеты в своей DAW для быстрого применения!

*Время настройки: 10-15 минут с готовыми пресетами*
*Совместимость: FL Studio 21+, Ableton Live 11+, Logic Pro X 10.7+*
