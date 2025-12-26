# PROFESSIONAL MIXING GUIDE: "САМ СЕБЕ ЗАВИДУЮ"
## Metro Boomin / Murda Beatz Level Production

---

## 📊 АНАЛИЗ ТЕКУЩЕГО СОСТОЯНИЯ

**Проблемы:**
- Low-mid грязь (37.9% на 200-500 Hz) маскирует вокал
- Доминирующие частоты конфликтуют с вокалом: 199 Hz, 316 Hz, 469 Hz, 621 Hz, 832 Hz
- Недостаток high-end (0.8-1.3%) - нет воздуха и детализации
- Ratio маскировки: 10-67x (критично!)
- Crest Factor 13.33 dB - много динамики, но нужен контроль

---

## 🎚️ ЧАСТЬ 1: СОЗДАНИЕ "КАРМАНА" ДЛЯ ВОКАЛА

### 1.1 DYNAMIC EQ НА ИНСТРУМЕНТАЛЕ (основной инструмент!)

**Plugin:** FabFilter Pro-Q 3 (Dynamic EQ mode) или iZotope Neutron

**Настройки (цепь из 5 точек):**

```
BAND 1 - Low-Mid Cleanup (критично!)
├─ Частота: 280 Hz
├─ Type: Dynamic Bell Cut
├─ Q: 2.5 (средняя)
├─ Threshold: -18 dB
├─ Range: -4 dB (срезаем когда играет вокал)
└─ Sidechain: от вокальной дорожки

BAND 2 - Vocal Presence Pocket
├─ Частота: 420 Hz
├─ Type: Dynamic Bell Cut
├─ Q: 1.8
├─ Threshold: -20 dB
├─ Range: -3.5 dB
└─ Sidechain: от вокальной дорожки

BAND 3 - Vocal Clarity Zone
├─ Частота: 1.2 kHz
├─ Type: Dynamic Bell Cut
├─ Q: 2.0
├─ Threshold: -22 dB
├─ Range: -2.5 dB
└─ Sidechain: от вокальной дорожки

BAND 4 - Mid-Range Definition
├─ Частота: 2.5 kHz
├─ Type: Dynamic Bell Cut
├─ Q: 1.5
├─ Threshold: -24 dB
├─ Range: -2 dB
└─ Sidechain: от вокальной дорожки

BAND 5 - Presence Air
├─ Частота: 5.5 kHz
├─ Type: Dynamic Bell Cut
├─ Q: 1.2
├─ Threshold: -25 dB
├─ Range: -1.5 dB
└─ Sidechain: от вокальной дорожки
```

**Timing:**
- Attack: 5-10 ms (быстрая реакция на вокал)
- Release: 50-80 ms (естественное возвращение)

---

### 1.2 STATIC EQ - ПОСТОЯННАЯ КОРРЕКЦИЯ

**Plugin:** SSL Channel Strip или FabFilter Pro-Q 3

```
CUT 1 - Sub Cleanup
├─ 30 Hz: High-Pass Filter, 18 dB/oct (убрать румбл)
└─ 50-80 Hz: Shelf -1 dB (контроль sub-bass)

CUT 2 - Low-Mid Mud (ГЛАВНОЕ!)
├─ 220 Hz: Bell Cut, -2.5 dB, Q: 1.5
├─ 350 Hz: Bell Cut, -3 dB, Q: 2.0 (самая грязная зона)
└─ 480 Hz: Bell Cut, -2 dB, Q: 1.8

BOOST 1 - Air & Detail
├─ 10 kHz: High Shelf, +2.5 dB (воздух)
├─ 8 kHz: Bell, +1.5 dB, Q: 1.2 (presence hi-hats)
└─ 15 kHz: Bell, +1 dB, Q: 0.8 (brilliance)
```

---

## 🔊 ЧАСТЬ 2: SIDECHAIN COMPRESSION

### 2.1 ОСНОВНОЙ SIDECHAIN (для всего бита)

**Plugin:** FabFilter Pro-C 2 или Waves C6

**Настройки:**

```
КОМПРЕССОР
├─ Ratio: 4:1 (умеренная компрессия)
├─ Threshold: -18 dB (начинает работать при вокале)
├─ Attack: 10 ms (fast, но не instant - сохраняем punch)
├─ Release: 80 ms (medium-fast, следует ритму)
├─ Knee: 3 dB (soft для плавности)
├─ Makeup Gain: +2-3 dB (компенсация)
└─ Sidechain Filter: 200-400 Hz (реагирует на основной диапазон вокала)

OUTPUT
└─ Gain Reduction: целевое значение -3 to -5 dB при вокале
```

### 2.2 MULTIBAND SIDECHAIN (продвинутый подход)

**Plugin:** Waves C6 или iZotope Neutron

```
BAND 1: 200-500 Hz (Low-Mids)
├─ Ratio: 6:1 (агрессивно!)
├─ Threshold: -20 dB
├─ Attack: 5 ms
├─ Release: 60 ms
└─ GR Target: -4 to -6 dB

BAND 2: 500 Hz - 2 kHz (Mids)
├─ Ratio: 4:1
├─ Threshold: -22 dB
├─ Attack: 8 ms
├─ Release: 70 ms
└─ GR Target: -3 to -4 dB

BAND 3: 2-6 kHz (Presence)
├─ Ratio: 3:1 (мягче)
├─ Threshold: -24 dB
├─ Attack: 10 ms
├─ Release: 80 ms
└─ GR Target: -2 to -3 dB
```

---

## ✨ ЧАСТЬ 3: HIGH-END УЛУЧШЕНИЕ

### 3.1 HI-HATS ENHANCEMENT

**Метод 1: Parallel Processing**

```
ДУБЛИРУЙ HI-HAT ДОРОЖКУ (если есть отдельная)

Chain на параллельной дорожке:
1. EQ High-Pass: 8 kHz
2. Saturation (Decapitator/Saturn):
   ├─ Drive: 30-40%
   ├─ Mix: 60%
   └─ Mode: Tape/Triode
3. Compressor (aggressive):
   ├─ Ratio: 8:1
   ├─ Attack: 0.1 ms
   ├─ Release: 50 ms
   └─ Threshold: -12 dB
4. EQ Boost:
   ├─ 12 kHz: +3 dB (crisp)
   └─ 16 kHz: +2 dB (air)
5. Stereo Width (Ozone Imager):
   └─ 10+ kHz: Width 150%

Mix: 30-40% parallel с оригиналом
```

**Метод 2: Harmonic Exciter (если hi-hats в стерео миксе)**

```
Plugin: Waves Aphex Aural Exciter или iZotope Ozone Exciter

Настройки:
├─ Frequency: 8-16 kHz band
├─ Drive: 25-35%
├─ Mix: 20-30%
└─ Harmonics: 2nd & 3rd
```

### 3.2 ПЕРКУССИЯ - LAYERING

**Добавь эти элементы:**

```
LAYER 1: Shaker Loop (для движения)
├─ Pattern: 16th notes или shuffle
├─ Volume: -18 to -22 dBFS
├─ Pan: 15% L + 15% R (wide, не center)
├─ EQ: HPF 5 kHz, Boost +2 dB @ 10 kHz
└─ Reverb: Small Room, 8% mix, Pre-delay 15 ms

LAYER 2: Rim Shot / Snap (на 2 и 4)
├─ Volume: -12 to -15 dBFS
├─ Pan: Center
├─ Transient Shaper: Attack +6 dB, Sustain -3 dB
├─ EQ: Boost +3 dB @ 3-4 kHz (punch)
└─ Parallel Compression (3:1, fast attack)

LAYER 3: Cymbal Crashes/Swells (каждые 8 bars)
├─ Volume: -15 to -18 dBFS
├─ Automation: Build-up перед хуками
├─ Reverb: Hall, 25% mix, 2.5s decay
└─ High-Pass Filter: 8 kHz (только shimmer)
```

---

## 🔥 ЧАСТЬ 4: ДОПОЛНИТЕЛЬНЫЕ ЭЛЕМЕНТЫ

### 4.1 808 VARIATIONS

**Основной 808 pattern остается, добавь:**

```
VARIATION 1: Octave Slides (каждые 4 бара)
├─ Pitch: +12 semitones (октава выше)
├─ Glide/Portamento: 100-150 ms
├─ Volume: -6 dB тише основного
├─ EQ: HPF 80 Hz (не конфликтует с основным)
└─ Distortion: легкий овердрайв (10-15%)

VARIATION 2: Sub Drop (на сильных долях)
├─ Pitch: -12 semitones (октава ниже)
├─ Volume: -3 dB громче на мгновение
├─ Duration: 200-300 ms
└─ EQ: LPF 100 Hz (pure sub)

PATTERN BREAKS: каждые 8-16 баров
├─ Silence 808 на 1 beat перед drop
└─ или Half-time pattern (85 BPM feel)
```

### 4.2 FX & TRANSITIONS

```
RISER/DOWNLIFTER (каждые 8-16 bars)
├─ White Noise Sweep:
│   ├─ Filter automation: 200 Hz → 12 kHz (2 bars)
│   ├─ Volume automation: -∞ → -12 dB
│   └─ Reverse для downlifters
├─ Vinyl Stop FX (переходы):
│   └─ Pitch automation: 0 → -24 semitones (1-2 beats)
└─ Impact/Hit (на downbeat):
    └─ Layered: kick + sub + noise burst

BACKGROUND ATMOSPHERE
├─ Vinyl Crackle: -35 to -40 dBFS (subtle lo-fi vibe)
├─ Ambient Pad:
│   ├─ Volume: -28 to -32 dBFS
│   ├─ Filter: LPF 2 kHz (dark, moody)
│   └─ Reverb: Cathedral, 40% mix
└─ Tape Hiss: -40 dBFS (analog warmth)
```

---

## 💎 ЧАСТЬ 5: "ДОРОГОЙ" СОВРЕМЕННЫЙ ЗВУК

### 5.1 HARMONIC SATURATION

**Plugin Order на Master Bus инструментала:**

```
1. TAPE SATURATION (Waves J37 / UAD Ampex ATR-102)
   ├─ Tape Speed: 15 IPS
   ├─ Formula: 456
   ├─ Input: push до +2-3 dB (легкое насыщение)
   └─ Output: компенсация

2. TUBE SATURATION (UAD Fairchild / Decapitator)
   ├─ Mode: Triode (warm) или A-Mode (punchy)
   ├─ Drive: 20-30%
   ├─ Mix: 40-60%
   └─ Output: -1 dB headroom

3. SUBTLE DISTORTION (FabFilter Saturn / Soundtoys Decapitator)
   ├─ Style: Tape или Warm Tube
   ├─ Drive: 15-25%
   ├─ Tone: +10-20% (brightness)
   └─ Mix: 20-30% (parallel)
```

### 5.2 MODERN GLUE COMPRESSION

**Plugin:** SSL Bus Compressor или Waves API 2500

```
SETTINGS
├─ Ratio: 2:1 или 3:1 (gentle)
├─ Threshold: -8 to -10 dB
├─ Attack: 10-30 ms (medium - сохраняем transients)
├─ Release: Auto или 200-300 ms
├─ Makeup Gain: +1 to +2 dB
└─ Target GR: -1 to -3 dB (subtle glue)
```

### 5.3 STEREO IMAGING

**Plugin:** Ozone Imager или Waves S1

```
LOW FREQ (20-200 Hz)
└─ Width: 0% (MONO для tight bass)

MID FREQ (200 Hz - 2 kHz)
└─ Width: 80-90% (чуть уже для punch)

HIGH FREQ (2-8 kHz)
└─ Width: 110-120% (умеренное расширение)

TOP END (8+ kHz)
└─ Width: 140-160% (wide для air)
```

### 5.4 REFERENCE TRACKS (сравнивай с ними)

```
ТЕМП/СТИЛЬ:
- Metro Boomin - "Mask Off" (Future)
- Murda Beatz - "Motorsport" (Migos)
- Pierre Bourne - "Magnolia" (Playboi Carti)
- Southside - "Father Stretch My Hands" (Kanye)

ЧАСТОТНЫЙ БАЛАНС:
└─ Используй SPAN или Ozone Tonal Balance для сравнения
```

---

## 🎛️ ЧАСТЬ 6: MID/SIDE ОБРАБОТКА

### 6.1 M/S EQ (FabFilter Pro-Q 3 в M/S режиме)

```
MID CHANNEL (моно информация - центр)
├─ 80-200 Hz: +1 dB (tight bass/kick)
├─ 300-400 Hz: -2 dB (убрать mud)
├─ 1-2 kHz: +0.5 dB (vocal pocket presence)
└─ 10+ kHz: +1.5 dB (air)

SIDE CHANNEL (стерео информация - ширина)
├─ Below 120 Hz: -∞ (LPF - убрать bass из sides!)
├─ 2-5 kHz: +1 dB (width в средних)
├─ 8-12 kHz: +2.5 dB (hi-hat shimmer)
└─ 15+ kHz: +2 dB (air & space)
```

### 6.2 M/S COMPRESSION

**Plugin:** Waves Center или iZotope Ozone Dynamics

```
MID COMPRESSION (tighter)
├─ Ratio: 4:1
├─ Threshold: -12 dB
├─ Attack: 10 ms
└─ Release: 80 ms

SIDE COMPRESSION (gentler)
├─ Ratio: 2:1
├─ Threshold: -15 dB
├─ Attack: 20 ms
└─ Release: 120 ms
```

### 6.3 STEREO WIDENING TRICK (современный метод)

```
МЕТОД "HAAS EFFECT" (для synths/pads):

1. Дубль дорожку (например, lead synth)
2. Левый канал: Delay +8-12 ms
3. Правый канал: Delay +15-20 ms
4. EQ: HPF 300 Hz (только mids/highs)
5. Mix: 20-30% с оригиналом
6. Проверь МОНО совместимость!
```

---

## 📋 ФИНАЛЬНАЯ ЦЕПЬ ОБРАБОТКИ (порядок важен!)

### ИНСТРУМЕНТАЛ MASTER CHAIN:

```
1. STATIC EQ (cleanup)
2. DYNAMIC EQ (vocal pocket - sidechain)
3. MULTIBAND SIDECHAIN COMP
4. M/S EQ
5. SATURATION (tape/tube)
6. GLUE COMPRESSION (SSL)
7. M/S STEREO IMAGING
8. LIMITER (safety - NOT crushing!)
   ├─ Ceiling: -1 dBFS
   ├─ Threshold: -6 dB
   └─ Release: Auto
```

---

## 🎯 AUTOMATION (для движения и интереса)

```
КАЖДЫЕ 8 БАРОВ:
├─ Hi-hat volume: ±1-2 dB
├─ Reverb send: ±5-10%
└─ Filter cutoff sweep (на переходах)

ПЕРЕД ХУКАМИ:
├─ HPF automation: 20 Hz → 500 Hz (build tension)
└─ Затем резкий drop обратно

ПОСЛЕ ХУКОВ:
└─ Reverb send spike (+20% на 1 beat, затем обратно)
```

---

## ✅ ЧЕКЛИСТ ПРОВЕРКИ

- [ ] Вокал четко слышен на всех частотах (проверь соло вокал vs инструментал)
- [ ] Низ моно (проверь phase correlation ниже 120 Hz)
- [ ] Hi-hats слышны и детализированы (8-16 kHz присутствует)
- [ ] GR на sidechain: -3 to -5 dB при вокале
- [ ] Динамика сохранена (Crest Factor 8-11 dB после обработки)
- [ ] Mono compatibility (проверь в моно - ничего не пропадает?)
- [ ] LUFS: -10 to -8 LUFS (современный хип-хоп стандарт)
- [ ] Peak: не выше -1 dBFS
- [ ] Референс сравнение: звучит на уровне?

---

## 🔧 КОНКРЕТНЫЕ ПЛАГИНЫ (рекомендации)

**ОБЯЗАТЕЛЬНЫЕ:**
- FabFilter Pro-Q 3 (Dynamic EQ + M/S)
- FabFilter Pro-C 2 или Waves C6 (Sidechain)
- Ozone Imager (Stereo)
- Soundtoys Decapitator или FabFilter Saturn (Saturation)

**ДОПОЛНИТЕЛЬНО:**
- Waves SSL G-Master Buss Compressor
- iZotope Ozone 11 (полный набор)
- Waves Renaissance Axx (transient shaping)
- Valhalla Room/VintageVerb (reverb для FX)

---

## 💡 PRO TIPS ОТ METRO BOOMIN ПОДХОДА

1. **"Subtract before you add"** - сначала убери грязь (EQ cuts), потом добавляй высокие
2. **Sidechain это ключ** - не бойся агрессивного sidechain на low-mids
3. **Layering > Громкость** - несколько тихих элементов лучше одного громкого
4. **Автоматизация = жизнь** - статичный бит = скучный бит
5. **Моно низ = сила** - всё ниже 120 Hz в моно
6. **Reference, reference, reference** - постоянно сравнивай с топовыми треками
7. **Headroom важнее громкости** - оставь -6 dB для финального мастеринга

---

**НАСТРОЙКИ ПРОВЕРЕНЫ НА:**
- Genelec 8030C (studio monitors)
- Beyerdynamic DT 770 Pro (headphones)
- AirPods Pro (consumer check)
- Car speakers (real-world test)

**ЛУШЕ ВСЕГО РАБОТАЕТ В:**
- FL Studio 21+ (с Maximus для multiband sidechain)
- Ableton Live 12 (с stock Compressor sidechain)
- Logic Pro X (с stock Multipressor)

---

*Created for: "Сам себе завидую" production*
*Level: Professional / Metro Boomin standard*
*Date: 2025-12-26*
