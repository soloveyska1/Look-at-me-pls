# QUICK REFERENCE - MASTERING SETTINGS
## "Сам себе завидую" - Russian Hip-Hop

**ПРОСТО СКОПИРУЙ ЭТИ НАСТРОЙКИ В СВОЙ DAW**

---

## 🎚️ EQ SETTINGS (Linear Phase EQ)

### PLUGIN: FabFilter Pro-Q 3 / Waves SSL G-EQ / UAD Pultec

```
Band 1 - High-Pass:
├─ Type: High-Pass (18 dB/oct)
├─ Freq: 30 Hz
└─ Slope: Steep (Butterworth)

Band 2 - MUD CUT (ГЛАВНОЕ!):
├─ Type: Bell
├─ Freq: 350 Hz
├─ Gain: -4.5 dB
└─ Q: 2.8

Band 3 - Bass Clean:
├─ Type: Bell
├─ Freq: 180 Hz
├─ Gain: -2.0 dB
└─ Q: 0.9

Band 4 - Presence:
├─ Type: Bell
├─ Freq: 3500 Hz
├─ Gain: +3.2 dB
└─ Q: 1.4

Band 5 - Air:
├─ Type: High Shelf
├─ Freq: 10000 Hz
├─ Gain: +4.8 dB
└─ Slope: Gentle

Band 6 - Brilliance:
├─ Type: High Shelf
├─ Freq: 14000 Hz
├─ Gain: +2.5 dB
└─ Slope: Gentle

Band 7 - Sub Control:
├─ Type: Low Shelf
├─ Freq: 45 Hz
├─ Gain: +1.5 dB
└─ Slope: Gentle

Band 8 - Bass Tight:
├─ Type: Bell
├─ Freq: 120 Hz
├─ Gain: -1.2 dB
└─ Q: 1.1
```

---

## 🎛️ MULTIBAND COMPRESSOR

### PLUGIN: FabFilter Pro-MB / Waves C6 / iZotope Ozone

```
BAND 1 - LOW (20-150 Hz):
├─ Threshold: -18 dB
├─ Ratio: 3:1
├─ Attack: 30 ms
├─ Release: 150 ms
├─ Knee: Medium
└─ Output Gain: 0 dB

BAND 2 - LOW-MID (150-800 Hz) ⚠️ MUD:
├─ Threshold: -20 dB
├─ Ratio: 4:1 (агрессивно!)
├─ Attack: 15 ms
├─ Release: 100 ms
├─ Knee: Hard
└─ Output Gain: 0 dB

BAND 3 - MID-HIGH (800-5000 Hz):
├─ Threshold: -16 dB
├─ Ratio: 2.5:1
├─ Attack: 5 ms
├─ Release: 80 ms
├─ Knee: Soft
└─ Output Gain: 0 dB

BAND 4 - HIGH (5000-20000 Hz):
├─ Threshold: -14 dB
├─ Ratio: 2:1
├─ Attack: 1 ms
├─ Release: 50 ms
├─ Knee: Soft
└─ Output Gain: 0 dB

MIX:
├─ Dry: 70%
└─ Wet: 30% (parallel compression)
```

---

## 🎧 STEREO IMAGER (M/S Processing)

### PLUGIN: iZotope Ozone Imager / Waves S1 / FabFilter Pro-Q 3 (M/S mode)

```
LOW BAND (20-200 Hz):
├─ Stereo Width: 0% (MONO)
└─ Why: Bass punch & mono compatibility

MID BAND (200-8000 Hz):
├─ Stereo Width: 180%
└─ Why: Space for vocals & effects

HIGH BAND (8000-20000 Hz):
├─ Stereo Width: 140%
└─ Why: Air & sparkle

OVERALL:
└─ Target Width: 45%
```

---

## 🔥 SATURATION

### PLUGIN: FabFilter Saturn 2 / Soundtoys Decapitator / Waves J37

```
Type: Tape / Tube
├─ Drive: 12%
├─ Mix: 25% wet / 75% dry
├─ Color: Warm (даже harmonics)
├─ HF Rolloff: 16 kHz (-3 dB)
└─ Output: 0 dB
```

---

## 🎚️ LIMITER (FINAL STAGE)

### PLUGIN: FabFilter Pro-L 2 / Waves L2 / iZotope Ozone Maximizer

```
TARGET LOUDNESS:
├─ LUFS Integrated: -8.5 LUFS
├─ True Peak: -1.0 dBTP
└─ Ceiling: -0.3 dBFS (safety)

LIMITER SETTINGS:
├─ Attack: 0.5 ms
├─ Release: 50 ms
├─ Lookahead: 5.0 ms
├─ Algorithm: Transparent / Modern
├─ Oversampling: 4x
├─ True Peak Mode: ON
├─ Dither: TPDF (24-bit)
└─ Auto-Gain: ON (to -8.5 LUFS)
```

---

## 📊 ИЗМЕРЕНИЯ (METERS)

### PLUGIN: Youlean Loudness Meter / Waves WLM Plus / iZotope Insight

```
BEFORE MASTERING:
├─ LUFS: -24.37
├─ Peak: -3.37 dBFS
└─ Crest: 20.99 dB

TARGET AFTER:
├─ LUFS: -8.5 ± 0.3
├─ True Peak: -1.0 dBTP
├─ Crest: 6.5-8.0 dB
├─ Dynamic Range: 7-9 dB
└─ Stereo Width: 45%
```

---

## 🎯 DAW ROUTING (Ableton / Logic / FL Studio)

```
TRACK "Сам себе завидую.wav"
    ↓
[1] Linear Phase EQ (8 bands) ← MASTERING_EQ.preset
    ↓
[2] Multiband Compressor (4 bands) ← MASTERING_MB.preset
    ↓
[3] M/S Stereo Imager ← MASTERING_STEREO.preset
    ↓
[4] Tape Saturation (subtle) ← MASTERING_SAT.preset
    ↓
[5] True Peak Limiter ← MASTERING_LIMITER.preset
    ↓
[6] Loudness Meter (для проверки)
    ↓
MASTER OUT → Export 24-bit WAV
```

---

## ⏱️ PROCESSING TIME ESTIMATES

```
По плагинам (manual):     20-30 минут настройки
По скрипту Python:        30-60 секунд обработки
```

---

## 🔧 АЛЬТЕРНАТИВНЫЕ ЦЕЛЕВЫЕ LOUDNESS

```
Консервативно:   -9.5 LUFS  (больше динамики)
Рекомендуемое:   -8.5 LUFS  (золотая середина) ✅
Агрессивно:      -7.5 LUFS  (максимальная громкость)
Экстремально:    -6.5 LUFS  (radio/club only)
```

---

## 📱 ПРОВЕРКА НА СИСТЕМАХ

```
✅ Studio Monitors (near-field):
   - Частотный баланс
   - Stereo image
   - Динамика

✅ Headphones (Sony MDR-7506 / ATH-M50x):
   - Вокальная разборчивость
   - Bass control
   - De-essing

✅ Phone Speaker (iPhone / Samsung):
   - Mono compatibility
   - Overall loudness
   - Vocal intelligibility

✅ Car Audio (Bluetooth):
   - Bass punch
   - Road noise masking
   - Overall presence

✅ Laptop Speakers:
   - Тонкие динамики test
   - Критичный тест для стриминга
```

---

## 🎼 PLUGIN ALTERNATIVES (Бюджетные варианты)

```
Linear Phase EQ:
├─ Pro: FabFilter Pro-Q 3 ($179)
├─ Mid: TDR Nova (FREE!)
└─ Budget: Voxengo Marvel GEQ (FREE)

Multiband Comp:
├─ Pro: FabFilter Pro-MB ($169)
├─ Mid: TDR Multiband (FREE!)
└─ Budget: OTT by Xfer (FREE)

Limiter:
├─ Pro: FabFilter Pro-L 2 ($199)
├─ Mid: LoudMax by Thomas Mundt (FREE!)
└─ Budget: Youlean Loudness Meter (FREE metering)

Saturation:
├─ Pro: FabFilter Saturn 2 ($139)
├─ Mid: Saturation Knob by Softube (FREE!)
└─ Budget: Camel Crusher (FREE)

Stereo Imager:
├─ Pro: iZotope Ozone Imager ($0 - FREE!)
├─ Mid: Waves S1 (часто в bundles)
└─ Budget: A1StereoControl (FREE)
```

---

## 🚨 ЧАСТЫЕ ОШИБКИ - НЕ ДЕЛАЙ ТАК!

```
❌ Лимитинг без EQ → Грязный, громкий мусор
❌ Over-compression → Pumping, безжизненность
❌ Слишком широкое stereo в басу → Phase issues
❌ Забыл True Peak mode → Clipping на стриминге
❌ Нет dither при export 16-bit → Quantization noise
❌ Не проверил в mono → Vocal disappears
```

---

## ✅ ФИНАЛЬНЫЙ ЧЕКЛИСТ

```
[ ] Загрузил трек в DAW
[ ] Вставил все плагины по порядку
[ ] Настроил EQ (8 bands)
[ ] Настроил Multiband Comp (4 bands)
[ ] Настроил Stereo Imager (M/S)
[ ] Добавил Saturation (12% drive)
[ ] Настроил Limiter (-8.5 LUFS target)
[ ] Проверил meters (LUFS, True Peak)
[ ] A/B сравнение с оригиналом
[ ] Проверил на 3+ системах
[ ] Проверил в mono
[ ] Export: 24-bit WAV, 44.1 kHz, TPDF dither
```

---

**Время обработки**: ~30 минут (manual) или 60 секунд (Python script)
**Результат**: Commercial-ready master для Spotify, Apple Music, YouTube

---

## 🎓 QUICK TIPS

```
💡 TIP 1: Начни с EQ, потом compression, потом limiting
💡 TIP 2: Больше EQ, меньше compression = более музыкально
💡 TIP 3: True Peak ВСЕГДА должен быть < -1.0 dBTP
💡 TIP 4: Проверь в mono ПЕРЕД финальным экспортом
💡 TIP 5: Dither нужен ТОЛЬКО при конверсии в 16-bit
💡 TIP 6: Оставь -0.3 dB headroom для safety
```

---

**ГОТОВО! Просто следуй настройкам выше.**

Или запусти Python скрипт для автоматической обработки:
```bash
python professional_mastering.py
```
