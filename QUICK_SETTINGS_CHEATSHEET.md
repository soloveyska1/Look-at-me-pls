# ⚡ БЫСТРАЯ ШПАРГАЛКА - ТОЧНЫЕ НАСТРОЙКИ

## 🎯 TOP 5 КРИТИЧНЫХ ДЕЙСТВИЙ (В ПОРЯДКЕ ПРИОРИТЕТА)

### 1️⃣ ВЫРЕЗАТЬ ГРЯЗЬ (STATIC EQ)
```
220 Hz: -2.5 dB, Q: 1.5
350 Hz: -3 dB, Q: 2.0    ← САМОЕ ВАЖНОЕ!
480 Hz: -2 dB, Q: 1.8
```

### 2️⃣ SIDECHAIN ОТ ВОКАЛА (Compressor)
```
Ratio: 4:1
Threshold: -18 dB
Attack: 10 ms
Release: 80 ms
Sidechain Filter: 200-400 Hz
Target GR: -3 to -5 dB
```

### 3️⃣ DYNAMIC EQ - ВОКАЛЬНЫЙ КАРМАН
```
280 Hz: -4 dB range, Threshold: -18 dB, Q: 2.5
420 Hz: -3.5 dB range, Threshold: -20 dB, Q: 1.8
1.2 kHz: -2.5 dB range, Threshold: -22 dB, Q: 2.0
Все с sidechain от вокала!
```

### 4️⃣ HIGH-END BOOST
```
8 kHz: +1.5 dB, Q: 1.2
10 kHz: +2.5 dB (High Shelf)
15 kHz: +1 dB, Q: 0.8
```

### 5️⃣ STEREO WIDTH
```
20-200 Hz: 0% (MONO)
8+ kHz: 140-160% (WIDE)
```

---

## 📊 ЧАСТОТНАЯ КАРТА КОНФЛИКТОВ

```
ПРОБЛЕМНЫЕ ЧАСТОТЫ БИТА:
199 Hz  ━━━━━━━━ CUT: -2 to -3 dB
316 Hz  ━━━━━━━━ CUT: -3 to -4 dB (динамически)
469 Hz  ━━━━━━━━ CUT: -2 to -3 dB (динамически)
621 Hz  ━━━━━━━━ CUT: -2 dB (динамически)
832 Hz  ━━━━━━━━ CUT: -1.5 dB (динамически)

BOOST ДЛЯ БАЛАНСА:
80-100 Hz  ━━━━━ +0.5 dB (sub control)
3-4 kHz    ━━━━━ +1 dB (presence - если нужно)
8-12 kHz   ━━━━━ +2 to +3 dB (air & detail)
```

---

## 🔊 SIDECHAIN MULTIBAND (для продвинутых)

```
LOW-MIDS (200-500 Hz): 6:1, -20 dB threshold, GR: -4/-6 dB
MIDS (500 Hz-2 kHz):   4:1, -22 dB threshold, GR: -3/-4 dB
HIGHS (2-6 kHz):       3:1, -24 dB threshold, GR: -2/-3 dB
```

---

## ✨ ДОБАВИТЬ В БИТ (элементы)

```
SHAKER:
- Pattern: 16th notes
- Volume: -18 to -22 dBFS
- Pan: Wide (±15%)
- HPF: 5 kHz

RIM/SNAP:
- On beats 2 & 4
- Volume: -12 to -15 dBFS
- Boost @ 3-4 kHz: +3 dB

808 SLIDE (variation):
- +12 semitones (октава выше)
- Glide: 100-150 ms
- Volume: -6 dB тише
- Каждые 4 бара

WHITE NOISE RISER:
- Filter sweep: 200 Hz → 12 kHz
- Length: 2 bars
- Volume: -∞ → -12 dB
```

---

## 💎 "ДОРОГОЙ ЗВУК" - 3 ПЛАГИНА

```
1. TAPE SATURATION
   Input: +2 to +3 dB
   Mix: 40-60%

2. SSL COMPRESSOR
   Ratio: 2:1
   Threshold: -8 dB
   Attack: 10-30 ms
   GR: -1 to -3 dB

3. STEREO IMAGER
   Low: 0% (mono)
   Top: 140-160% (wide)
```

---

## 🎛️ M/S EQ НАСТРОЙКИ

```
MID CHANNEL:
300-400 Hz: -2 dB (mud)
1-2 kHz: +0.5 dB
10+ kHz: +1.5 dB

SIDE CHANNEL:
Below 120 Hz: -∞ (убрать!)
8-12 kHz: +2.5 dB
15+ kHz: +2 dB
```

---

## 📏 ЦЕЛЕВЫЕ ПАРАМЕТРЫ

```
Peak Level:    -3 to -1 dBFS
RMS:          -10 to -8 dBFS (после обработки)
LUFS:         -10 to -8 LUFS
Crest Factor:  8-11 dB (после обработки)
Dynamic Range: DR7-DR9
```

---

## ⚠️ КРИТИЧНЫЕ ПРОВЕРКИ

✓ Вокал слышен чётко на всех частотах?
✓ Низ в моно (проверка корреляции)?
✓ Hi-hats детализированы (8-16 kHz есть)?
✓ Sidechain работает (-3/-5 dB GR при вокале)?
✓ Mono compatibility (ничего не пропадает)?
✓ Звучит как референс треки?

---

## 🎵 РЕФЕРЕНСЫ ДЛЯ СРАВНЕНИЯ

1. Metro Boomin - "Mask Off" (Future)
2. Murda Beatz - "Motorsport" (Migos)
3. Pierre Bourne - "Magnolia" (Playboi Carti)
4. Southside - "Father Stretch My Hands Pt. 1" (Kanye West)

**Используй SPAN или Ozone Tonal Balance для A/B сравнения частот!**

---

## 🚀 ПОРЯДОК ПРИМЕНЕНИЯ (Step-by-Step)

```
STEP 1: Static EQ (убрать mud @ 220, 350, 480 Hz)
STEP 2: Dynamic EQ с sidechain (5 bands)
STEP 3: Multiband Sidechain Compressor
STEP 4: High-end boost (8-15 kHz)
STEP 5: Добавить shaker + rim/snap
STEP 6: M/S EQ обработка
STEP 7: Saturation (tape/tube)
STEP 8: SSL Glue Compressor
STEP 9: Stereo Imager
STEP 10: Safety Limiter (-1 dBFS ceiling)
```

---

**ВРЕМЯ ВЫПОЛНЕНИЯ: 30-45 минут**
**РЕЗУЛЬТАТ: Профессиональный микс уровня Metro Boomin**
