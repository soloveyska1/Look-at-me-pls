#!/usr/bin/env python3
"""
АНАЛИЗ АУДИО ТРЕКА - Профессиональные метрики
Для оценки качества мастеринга
"""

import numpy as np
import librosa
import matplotlib.pyplot as plt
from scipy import signal
import pyloudnorm as pyln

def analyze_track(file_path):
    """
    Полный анализ аудио трека с профессиональными метриками
    """
    print("\n" + "="*80)
    print(f"🎼 АНАЛИЗ ТРЕКА: {file_path}")
    print("="*80)

    # Загрузка
    audio, sr = librosa.load(file_path, sr=None, mono=False)
    if audio.ndim == 1:
        audio = audio.reshape(-1, 1)
        is_mono = True
    else:
        audio = audio.T
        is_mono = False

    duration = len(audio) / sr

    print(f"\n📊 БАЗОВАЯ ИНФОРМАЦИЯ:")
    print(f"   Sample Rate: {sr} Hz")
    print(f"   Duration: {duration:.2f} seconds")
    print(f"   Channels: {'Mono' if is_mono else 'Stereo'}")
    print(f"   Samples: {len(audio):,}")

    # LOUDNESS ANALYSIS
    print(f"\n🔊 LOUDNESS MEASUREMENTS:")
    meter = pyln.Meter(sr)

    if audio.ndim == 1:
        audio_for_meter = audio.reshape(-1, 1)
    else:
        audio_for_meter = audio

    lufs_integrated = meter.integrated_loudness(audio_for_meter)

    # RMS
    rms = np.sqrt(np.mean(audio**2))
    rms_db = 20 * np.log10(rms) if rms > 0 else -np.inf

    # Peak
    peak = np.max(np.abs(audio))
    peak_db = 20 * np.log10(peak) if peak > 0 else -np.inf

    # Crest Factor
    crest_factor = peak_db - rms_db

    print(f"   LUFS Integrated: {lufs_integrated:.2f} LUFS")
    print(f"   RMS Level: {rms_db:.2f} dBFS")
    print(f"   Peak Level: {peak_db:.2f} dBFS")
    print(f"   Crest Factor: {crest_factor:.2f} dB")
    print(f"   Headroom: {-peak_db:.2f} dB")

    # Оценка громкости
    if lufs_integrated < -14:
        status = "⚠️ СЛИШКОМ ТИХО для стриминга"
    elif lufs_integrated < -10:
        status = "✅ ОТЛИЧНО для стриминга (динамично)"
    elif lufs_integrated < -7:
        status = "✅ ОТЛИЧНО для рэпа/поп"
    else:
        status = "⚠️ Может быть слишком громко (риск искажений)"
    print(f"   Оценка: {status}")

    # STEREO ANALYSIS
    if not is_mono:
        print(f"\n🎧 STEREO ANALYSIS:")

        # Stereo width
        left = audio[:, 0]
        right = audio[:, 1]

        mid = (left + right) / 2
        side = (left - right) / 2

        mid_energy = np.sum(mid**2)
        side_energy = np.sum(side**2)
        total_energy = mid_energy + side_energy

        if total_energy > 0:
            stereo_width = (side_energy / total_energy) * 100
        else:
            stereo_width = 0

        print(f"   Stereo Width: {stereo_width:.1f}%")

        # Correlation
        correlation = np.corrcoef(left, right)[0, 1]
        print(f"   L/R Correlation: {correlation:.3f}")

        # Stereo оценка
        if stereo_width < 20:
            stereo_status = "⚠️ Очень узкое (почти MONO)"
        elif stereo_width < 35:
            stereo_status = "⚠️ Узкое"
        elif stereo_width < 55:
            stereo_status = "✅ ОТЛИЧНО"
        else:
            stereo_status = "⚠️ Слишком широкое (риск mono problems)"
        print(f"   Оценка: {stereo_status}")

    # SPECTRAL ANALYSIS
    print(f"\n🎚️ ЧАСТОТНЫЙ БАЛАНС:")

    # Mono for spectral analysis
    if audio.ndim == 2:
        audio_mono = np.mean(audio, axis=1)
    else:
        audio_mono = audio.flatten()

    # FFT
    fft = np.fft.rfft(audio_mono)
    freqs = np.fft.rfftfreq(len(audio_mono), 1/sr)
    magnitude = np.abs(fft)

    # Частотные диапазоны
    bands = {
        'Sub-bass (20-60 Hz)': (20, 60),
        'Bass (60-250 Hz)': (60, 250),
        'Low-mids (250-500 Hz)': (250, 500),
        'Mids (500-2k Hz)': (500, 2000),
        'Upper-mids (2k-4k Hz)': (2000, 4000),
        'Presence (4k-6k Hz)': (4000, 6000),
        'Brilliance (6k-20k Hz)': (6000, 20000),
    }

    band_energies = {}
    for band_name, (low, high) in bands.items():
        mask = (freqs >= low) & (freqs <= high)
        energy = np.sum(magnitude[mask]**2)
        band_energies[band_name] = energy

    # Нормализация
    max_energy = max(band_energies.values())
    for band_name, energy in band_energies.items():
        percentage = (energy / max_energy) * 100 if max_energy > 0 else 0
        bar = '█' * int(percentage / 5)
        print(f"   {band_name:30s} {percentage:5.1f}% {bar}")

    # MUD RATIO (проблемная зона)
    low_mid_energy = band_energies['Low-mids (250-500 Hz)']
    upper_mid_energy = band_energies['Upper-mids (2k-4k Hz)']

    if upper_mid_energy > 0:
        mud_ratio = 10 * np.log10(low_mid_energy / upper_mid_energy)
    else:
        mud_ratio = np.inf

    print(f"\n   Mud Ratio (250-500 Hz / 2-4 kHz): {mud_ratio:.1f} dB")
    if mud_ratio > 15:
        print(f"   ⚠️ КРИТИЧНО: Слишком много энергии в low-mids (грязь)")
    elif mud_ratio > 10:
        print(f"   ⚠️ Много энергии в low-mids")
    else:
        print(f"   ✅ Хороший баланс low-mids/upper-mids")

    # SPECTRAL CENTROID (где сосредоточена энергия)
    spectral_centroid = librosa.feature.spectral_centroid(y=audio_mono, sr=sr)[0]
    avg_centroid = np.mean(spectral_centroid)

    print(f"\n   Spectral Centroid: {avg_centroid:.0f} Hz")
    if avg_centroid < 2000:
        print(f"   ⚠️ Темный, bass-heavy звук")
    elif avg_centroid < 3000:
        print(f"   ✅ Сбалансированный звук")
    else:
        print(f"   ✅ Яркий звук")

    # DYNAMIC RANGE
    print(f"\n📈 ДИНАМИЧЕСКИЙ ДИАПАЗОН:")

    # Peak vs RMS
    peak_to_rms = crest_factor
    print(f"   Peak-to-RMS: {peak_to_rms:.1f} dB")

    if peak_to_rms > 15:
        dynamic_status = "⚠️ Слишком динамично (нужна компрессия)"
    elif peak_to_rms > 10:
        dynamic_status = "✅ Хороший диапазон (естественно)"
    elif peak_to_rms > 6:
        dynamic_status = "✅ ОТЛИЧНО для стриминга"
    else:
        dynamic_status = "⚠️ Чрезмерная компрессия (brick wall)"
    print(f"   Оценка: {dynamic_status}")

    # STREAMING PLATFORM COMPATIBILITY
    print(f"\n📱 СОВМЕСТИМОСТЬ СО СТРИМИНГОМ:")

    platforms = {
        'Spotify': -14,
        'Apple Music': -16,
        'YouTube': -13,
        'Яндекс.Музыка': -14,
        'Deezer': -14,
        'Tidal': -14,
    }

    print(f"   Ваш трек: {lufs_integrated:.1f} LUFS\n")
    for platform, target in platforms.items():
        diff = lufs_integrated - target
        if diff > 0:
            status = f"✅ Не будет понижен"
            penalty = 0
        else:
            status = f"⚠️ Будет понижен на {abs(diff):.1f} dB"
            penalty = abs(diff)

        print(f"   {platform:20s} (target {target} LUFS): {status}")

    # RECOMMENDATIONS
    print(f"\n🎯 РЕКОМЕНДАЦИИ:")

    recommendations = []

    if lufs_integrated < -12:
        recommendations.append(f"• Увеличить громкость до -8 to -10 LUFS (сейчас {lufs_integrated:.1f})")

    if mud_ratio > 12:
        recommendations.append(f"• Убрать mud @ 250-500 Hz (сейчас {mud_ratio:.1f} dB соотношение)")

    if not is_mono and stereo_width < 30:
        recommendations.append(f"• Расширить стерео-базу (сейчас {stereo_width:.1f}%)")

    brilliance_pct = (band_energies['Brilliance (6k-20k Hz)'] / max_energy) * 100
    if brilliance_pct < 10:
        recommendations.append(f"• Добавить яркость @ 6-20 kHz (сейчас {brilliance_pct:.1f}%)")

    if peak_to_rms > 12:
        recommendations.append(f"• Применить компрессию/лимитинг (crest {peak_to_rms:.1f} dB)")

    if peak_db > -1.0:
        recommendations.append(f"• Оставить headroom для True Peak (сейчас {peak_db:.1f} dBFS)")

    if recommendations:
        for rec in recommendations:
            print(f"   {rec}")
    else:
        print(f"   ✅ Трек звучит отлично! Минимальные корректировки.")

    print("\n" + "="*80)

    return {
        'lufs': lufs_integrated,
        'rms_db': rms_db,
        'peak_db': peak_db,
        'crest_factor': crest_factor,
        'stereo_width': stereo_width if not is_mono else 0,
        'mud_ratio': mud_ratio,
        'spectral_centroid': avg_centroid,
        'band_energies': band_energies,
    }


def compare_before_after(original_file, mastered_file):
    """
    Сравнение оригинала и мастера
    """
    print("\n" + "="*80)
    print("📊 СРАВНЕНИЕ: ДО vs ПОСЛЕ МАСТЕРИНГА")
    print("="*80)

    print("\n🎼 ОРИГИНАЛ:")
    original = analyze_track(original_file)

    print("\n\n🎼 МАСТЕР:")
    mastered = analyze_track(mastered_file)

    # Comparison
    print("\n" + "="*80)
    print("📈 УЛУЧШЕНИЯ:")
    print("="*80)

    improvements = {
        'LUFS': (mastered['lufs'] - original['lufs'], 'dB'),
        'RMS': (mastered['rms_db'] - original['rms_db'], 'dB'),
        'Peak': (mastered['peak_db'] - original['peak_db'], 'dB'),
        'Crest Factor': (mastered['crest_factor'] - original['crest_factor'], 'dB'),
        'Stereo Width': (mastered['stereo_width'] - original['stereo_width'], '%'),
        'Mud Ratio': (mastered['mud_ratio'] - original['mud_ratio'], 'dB'),
    }

    for metric, (change, unit) in improvements.items():
        if change > 0:
            symbol = "↑"
            color = "✅" if metric in ['LUFS', 'RMS', 'Stereo Width'] else "⚠️"
        elif change < 0:
            symbol = "↓"
            color = "✅" if metric in ['Crest Factor', 'Mud Ratio'] else "⚠️"
        else:
            symbol = "→"
            color = "−"

        print(f"   {metric:20s} {symbol} {change:+7.2f} {unit:3s} {color}")

    print("\n" + "="*80)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # Анализ одного файла
        analyze_track(sys.argv[1])
    else:
        # Анализ трека по умолчанию
        original = "/home/user/Look-at-me-pls/Сам себе завидую.wav"
        analyze_track(original)

        # Если есть mastered версия, сравним
        import os
        mastered = "/home/user/Look-at-me-pls/Сам себе завидую_MASTERED.wav"
        if os.path.exists(mastered):
            compare_before_after(original, mastered)
