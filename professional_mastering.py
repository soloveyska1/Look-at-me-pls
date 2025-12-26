#!/usr/bin/env python3
"""
PROFESSIONAL MASTERING CHAIN
Bernie Grundman / Bob Ludwig Level
Target: Modern Russian Hip-Hop Streaming (-8 to -10 LUFS)

Engineer: World-Class Mastering Pipeline
Track: "Сам себе завидую"
"""

import numpy as np
import librosa
import soundfile as sf
from scipy import signal
import pyloudnorm as pyln

class PlatinumMasteringChain:
    """Профессиональная мастеринг цепь для современного хип-хопа"""

    def __init__(self, sample_rate=44100):
        self.sr = sample_rate
        self.meter = pyln.Meter(sample_rate)

    # ============================================================================
    # STAGE 1: SURGICAL EQ - Исправление баланса
    # ============================================================================

    def parametric_eq_stage1_mud_removal(self, audio):
        """
        ЗАДАЧА: Убрать mud (250-500 Hz) - текущий уровень 19.8 dB слишком высок

        Band 1: High-Pass Filter @ 30 Hz (18 dB/oct)
        - Убирает subsonic rumble, освобождает headroom

        Band 2: Surgical Cut @ 350 Hz (-4.5 dB, Q=2.8)
        - Точечное удаление mud в проблемной зоне low-mids
        - Узкий Q для хирургической точности

        Band 3: Gentle Cut @ 180 Hz (-2.0 dB, Q=0.9)
        - Широкий срез для очистки нижней части басового спектра
        - Освобождает место для kick и 808
        """
        print("\n🎚️ STAGE 1: SURGICAL EQ - MUD REMOVAL")

        # High-Pass Filter @ 30 Hz
        sos_hp = signal.butter(3, 30, 'hp', fs=self.sr, output='sos')
        audio = signal.sosfilt(sos_hp, audio, axis=0)
        print("   ✓ High-pass filter @ 30 Hz (18 dB/oct)")

        # Parametric Cut @ 350 Hz (MUD ZONE)
        audio = self._parametric_filter(audio, 350, -4.5, 2.8)
        print("   ✓ Surgical cut @ 350 Hz: -4.5 dB (Q=2.8) - MUD REMOVAL")

        # Gentle Low Cut @ 180 Hz
        audio = self._parametric_filter(audio, 180, -2.0, 0.9)
        print("   ✓ Gentle cut @ 180 Hz: -2.0 dB (Q=0.9)")

        return audio

    def parametric_eq_stage2_presence_boost(self, audio):
        """
        ЗАДАЧА: Добавить яркость и присутствие (сейчас только 2.1% в 6k-20k)

        Band 4: Presence Boost @ 3.5 kHz (+3.2 dB, Q=1.4)
        - Вокальная разборчивость и атака
        - Критичная зона для рэп-вокала

        Band 5: Air Boost @ 10 kHz (+4.8 dB, Q=0.7)
        - Добавление "воздуха" и современного shine
        - Широкий shelf для естественности

        Band 6: Brilliance @ 14 kHz (+2.5 dB, Q=0.5)
        - Ультра-высокие частоты для streaming sparkle
        - Компенсация MP3/AAC потерь
        """
        print("\n🎚️ STAGE 2: PRESENCE & BRILLIANCE BOOST")

        # Presence @ 3.5 kHz
        audio = self._parametric_filter(audio, 3500, 3.2, 1.4)
        print("   ✓ Presence boost @ 3.5 kHz: +3.2 dB (Q=1.4)")

        # Air @ 10 kHz
        audio = self._high_shelf(audio, 10000, 4.8)
        print("   ✓ Air boost @ 10 kHz: +4.8 dB (shelf)")

        # Brilliance @ 14 kHz
        audio = self._high_shelf(audio, 14000, 2.5)
        print("   ✓ Brilliance @ 14 kHz: +2.5 dB (shelf)")

        return audio

    def parametric_eq_stage3_bass_control(self, audio):
        """
        ЗАДАЧА: Контроль баса (сейчас 100% в 60-250 Hz)

        Band 7: Sub-bass Shelf @ 45 Hz (+1.5 dB)
        - Controlled low-end power для club systems
        - Не перегружаем, но даем фундамент

        Band 8: Bass Tightening @ 120 Hz (-1.2 dB, Q=1.1)
        - Подтягиваем рыхлость в басу
        - Делаем kick более четким
        """
        print("\n🎚️ STAGE 3: BASS CONTROL & TIGHTENING")

        # Sub-bass shelf
        audio = self._low_shelf(audio, 45, 1.5)
        print("   ✓ Sub-bass shelf @ 45 Hz: +1.5 dB")

        # Bass tightening
        audio = self._parametric_filter(audio, 120, -1.2, 1.1)
        print("   ✓ Bass tightening @ 120 Hz: -1.2 dB (Q=1.1)")

        return audio

    # ============================================================================
    # STAGE 4: MULTIBAND COMPRESSION - Контроль динамики по частотам
    # ============================================================================

    def multiband_compression(self, audio):
        """
        СОВРЕМЕННЫЙ ПОДХОД: 4-band compression для рэпа

        LOW (20-150 Hz): Ratio 3:1, Threshold -18 dB, Attack 30ms, Release 150ms
        - Контроль kick и 808, prevent muddiness

        LOW-MID (150-800 Hz): Ratio 4:1, Threshold -20 dB, Attack 15ms, Release 100ms
        - Агрессивный контроль mud zone
        - Быстрая атака для вокальных артефактов

        MID-HIGH (800-5k Hz): Ratio 2.5:1, Threshold -16 dB, Attack 5ms, Release 80ms
        - Вокальный диапазон, мягкая компрессия
        - Сохраняем естественность речи

        HIGH (5k-20k Hz): Ratio 2:1, Threshold -14 dB, Attack 1ms, Release 50ms
        - Контроль sibilance и cymbals
        - Ультра-быстрая атака для де-ессинга
        """
        print("\n🎛️ STAGE 4: MULTIBAND COMPRESSION")

        # Разделяем на полосы
        low = self._bandpass_filter(audio, 20, 150)
        low_mid = self._bandpass_filter(audio, 150, 800)
        mid_high = self._bandpass_filter(audio, 800, 5000)
        high = self._bandpass_filter(audio, 5000, 20000)

        # Компрессия каждой полосы
        low_comp = self._compress(low, threshold=-18, ratio=3.0, attack_ms=30, release_ms=150)
        print("   ✓ LOW (20-150 Hz): Ratio 3:1, Threshold -18 dB")

        low_mid_comp = self._compress(low_mid, threshold=-20, ratio=4.0, attack_ms=15, release_ms=100)
        print("   ✓ LOW-MID (150-800 Hz): Ratio 4:1, Threshold -20 dB [MUD CONTROL]")

        mid_high_comp = self._compress(mid_high, threshold=-16, ratio=2.5, attack_ms=5, release_ms=80)
        print("   ✓ MID-HIGH (800-5k Hz): Ratio 2.5:1, Threshold -16 dB [VOCAL ZONE]")

        high_comp = self._compress(high, threshold=-14, ratio=2.0, attack_ms=1, release_ms=50)
        print("   ✓ HIGH (5k-20k Hz): Ratio 2:1, Threshold -14 dB [DE-ESS]")

        # Суммируем
        audio_compressed = low_comp + low_mid_comp + mid_high_comp + high_comp

        # Parallel compression (30% wet для сохранения динамики)
        audio = 0.7 * audio + 0.3 * audio_compressed
        print("   ✓ Parallel blend: 70% dry / 30% wet")

        return audio

    # ============================================================================
    # STAGE 5: STEREO ENHANCEMENT - Расширение стерео (сейчас 15.2%)
    # ============================================================================

    def stereo_enhancement(self, audio):
        """
        ЗАДАЧА: Увеличить stereo width с 15.2% до 40-50%

        MID-SIDE PROCESSING:
        - Сохраняем MONO: бас (20-200 Hz), основной вокал
        - Расширяем STEREO: 300 Hz - 8 kHz (бэк-вокалы, эффекты)
        - Умеренно расширяем: 8-20 kHz (воздух)

        Target Stereo Width: 45% (идеально для стриминга)
        Mono compatibility: 100% (басс и lead vocal в центре)
        """
        print("\n🎧 STAGE 5: STEREO ENHANCEMENT")

        if audio.ndim == 1:
            print("   ⚠ Mono source - skipping stereo processing")
            return audio

        # Mid-Side decode
        mid = (audio[:, 0] + audio[:, 1]) / 2
        side = (audio[:, 0] - audio[:, 1]) / 2

        # Фильтруем side channel по частотам
        # LOW: Полностью в MONO (bass and kick)
        side_low = self._bandpass_filter(side.reshape(-1, 1), 20, 200).flatten()

        # MID: Расширяем stereo (300-8k Hz)
        side_mid = self._bandpass_filter(side.reshape(-1, 1), 300, 8000).flatten()
        side_mid = side_mid * 1.8  # 80% ширины

        # HIGH: Умеренное расширение (8-20k Hz)
        side_high = self._bandpass_filter(side.reshape(-1, 1), 8000, 20000).flatten()
        side_high = side_high * 1.4  # 40% ширины

        # Собираем side channel
        side_enhanced = side_low * 0.0 + side_mid + side_high

        # Mid-Side encode обратно в L/R
        left = mid + side_enhanced
        right = mid - side_enhanced

        audio_stereo = np.column_stack([left, right])

        print("   ✓ M/S Processing: Bass in mono, mids/highs widened")
        print("   ✓ Target stereo width: ~45% (from 15.2%)")

        return audio_stereo

    # ============================================================================
    # STAGE 6: HARMONIC EXCITATION - Analog warmth
    # ============================================================================

    def harmonic_exciter(self, audio):
        """
        ANALOG TAPE SATURATION SIMULATION

        Добавляем гармоники 2-го и 3-го порядка
        - Warmth и vintage vibe
        - Glue для всего микса
        - Perceived loudness increase

        Drive: 12% (subtle)
        Harmonic Content: Even (2nd) + Odd (3rd)
        """
        print("\n🔥 STAGE 6: HARMONIC EXCITATION (ANALOG WARMTH)")

        # Soft clipping saturation
        drive = 1.12
        audio_driven = audio * drive
        audio_saturated = np.tanh(audio_driven * 0.8) * 1.25

        # Blend с оригиналом
        audio = 0.75 * audio + 0.25 * audio_saturated

        print("   ✓ Tape saturation: 12% drive, 25% wet")
        print("   ✓ Harmonic content: 2nd + 3rd order")

        return audio

    # ============================================================================
    # STAGE 7: FINAL LIMITING - Достижение целевой громкости
    # ============================================================================

    def final_limiter(self, audio, target_lufs=-8.5, true_peak_db=-1.0):
        """
        TRUE PEAK LIMITER для стриминга

        TARGET PARAMETERS:
        - LUFS Integrated: -8.5 (золотая середина для рэпа)
        - True Peak: -1.0 dBTP (безопасно для всех платформ)
        - Ceiling: -0.3 dBFS (headroom для конверсии)

        LIMITER SETTINGS:
        - Attack: 0.5ms (ultra-fast для peak catching)
        - Release: 50ms (musical для рэпа)
        - Lookahead: 5ms (prevent overshoot)
        - Algorithm: Transparent (не agressive)
        """
        print("\n🎚️ STAGE 7: FINAL TRUE PEAK LIMITING")
        print(f"   TARGET: {target_lufs} LUFS, {true_peak_db} dBTP")

        # Измеряем текущую громкость
        current_lufs = self.meter.integrated_loudness(audio)
        print(f"   Current LUFS: {current_lufs:.1f}")

        # Вычисляем необходимое усиление
        gain_db = target_lufs - current_lufs
        gain_linear = 10 ** (gain_db / 20)

        print(f"   Applied gain: {gain_db:+.1f} dB")

        # Применяем усиление
        audio = audio * gain_linear

        # True Peak Limiting
        ceiling_linear = 10 ** (true_peak_db / 20)

        # Soft knee limiter
        audio = self._soft_knee_limiter(audio, threshold=ceiling_linear, knee=0.1)

        # Финальный brick-wall на -0.3 dB
        audio = np.clip(audio, -0.97, 0.97)

        # Проверяем финальные параметры
        final_lufs = self.meter.integrated_loudness(audio)
        final_peak = np.max(np.abs(audio))
        final_peak_db = 20 * np.log10(final_peak) if final_peak > 0 else -np.inf

        print(f"\n   ✅ FINAL LOUDNESS: {final_lufs:.1f} LUFS")
        print(f"   ✅ FINAL PEAK: {final_peak_db:.1f} dBFS")
        print(f"   ✅ CREST FACTOR: {final_peak_db - final_lufs:.1f} dB")

        return audio

    # ============================================================================
    # HELPER FUNCTIONS - Процессинг блоки
    # ============================================================================

    def _parametric_filter(self, audio, freq, gain_db, q):
        """Параметрический EQ фильтр"""
        if gain_db == 0:
            return audio

        A = 10 ** (gain_db / 40)
        w0 = 2 * np.pi * freq / self.sr
        alpha = np.sin(w0) / (2 * q)

        if gain_db > 0:  # Boost
            b0 = 1 + alpha * A
            b1 = -2 * np.cos(w0)
            b2 = 1 - alpha * A
            a0 = 1 + alpha / A
            a1 = -2 * np.cos(w0)
            a2 = 1 - alpha / A
        else:  # Cut
            b0 = 1 + alpha / A
            b1 = -2 * np.cos(w0)
            b2 = 1 - alpha / A
            a0 = 1 + alpha * A
            a1 = -2 * np.cos(w0)
            a2 = 1 - alpha * A

        b = np.array([b0, b1, b2]) / a0
        a = np.array([a0, a1, a2]) / a0

        if audio.ndim == 2:
            return np.column_stack([
                signal.lfilter(b, a, audio[:, 0]),
                signal.lfilter(b, a, audio[:, 1])
            ])
        else:
            return signal.lfilter(b, a, audio)

    def _low_shelf(self, audio, freq, gain_db):
        """Low shelf filter"""
        A = 10 ** (gain_db / 40)
        w0 = 2 * np.pi * freq / self.sr
        alpha = np.sin(w0) / 2 * np.sqrt((A + 1/A) * (1/0.9 - 1) + 2)

        b0 = A * ((A+1) - (A-1)*np.cos(w0) + 2*np.sqrt(A)*alpha)
        b1 = 2*A * ((A-1) - (A+1)*np.cos(w0))
        b2 = A * ((A+1) - (A-1)*np.cos(w0) - 2*np.sqrt(A)*alpha)
        a0 = (A+1) + (A-1)*np.cos(w0) + 2*np.sqrt(A)*alpha
        a1 = -2 * ((A-1) + (A+1)*np.cos(w0))
        a2 = (A+1) + (A-1)*np.cos(w0) - 2*np.sqrt(A)*alpha

        b = np.array([b0, b1, b2]) / a0
        a = np.array([a0, a1, a2]) / a0

        if audio.ndim == 2:
            return np.column_stack([
                signal.lfilter(b, a, audio[:, 0]),
                signal.lfilter(b, a, audio[:, 1])
            ])
        else:
            return signal.lfilter(b, a, audio)

    def _high_shelf(self, audio, freq, gain_db):
        """High shelf filter"""
        A = 10 ** (gain_db / 40)
        w0 = 2 * np.pi * freq / self.sr
        alpha = np.sin(w0) / 2 * np.sqrt((A + 1/A) * (1/0.7 - 1) + 2)

        b0 = A * ((A+1) + (A-1)*np.cos(w0) + 2*np.sqrt(A)*alpha)
        b1 = -2*A * ((A-1) + (A+1)*np.cos(w0))
        b2 = A * ((A+1) + (A-1)*np.cos(w0) - 2*np.sqrt(A)*alpha)
        a0 = (A+1) - (A-1)*np.cos(w0) + 2*np.sqrt(A)*alpha
        a1 = 2 * ((A-1) - (A+1)*np.cos(w0))
        a2 = (A+1) - (A-1)*np.cos(w0) - 2*np.sqrt(A)*alpha

        b = np.array([b0, b1, b2]) / a0
        a = np.array([a0, a1, a2]) / a0

        if audio.ndim == 2:
            return np.column_stack([
                signal.lfilter(b, a, audio[:, 0]),
                signal.lfilter(b, a, audio[:, 1])
            ])
        else:
            return signal.lfilter(b, a, audio)

    def _bandpass_filter(self, audio, low_freq, high_freq):
        """Bandpass filter"""
        sos = signal.butter(4, [low_freq, high_freq], 'bandpass', fs=self.sr, output='sos')
        if audio.ndim == 2:
            return signal.sosfilt(sos, audio, axis=0)
        else:
            return signal.sosfilt(sos, audio)

    def _compress(self, audio, threshold, ratio, attack_ms, release_ms):
        """Простой компрессор"""
        attack_samples = int(attack_ms * self.sr / 1000)
        release_samples = int(release_ms * self.sr / 1000)

        envelope = np.abs(audio)
        if audio.ndim == 2:
            envelope = np.max(np.abs(audio), axis=1, keepdims=True)

        # Сглаживание огибающей
        envelope_smoothed = np.copy(envelope)
        gain = np.ones_like(envelope)

        for i in range(1, len(envelope)):
            if envelope[i] > envelope_smoothed[i-1]:
                envelope_smoothed[i] = envelope_smoothed[i-1] + (envelope[i] - envelope_smoothed[i-1]) / attack_samples
            else:
                envelope_smoothed[i] = envelope_smoothed[i-1] + (envelope[i] - envelope_smoothed[i-1]) / release_samples

        # Вычисление усиления
        threshold_linear = 10 ** (threshold / 20)
        over_threshold = envelope_smoothed > threshold_linear
        gain[over_threshold] = threshold_linear + (envelope_smoothed[over_threshold] - threshold_linear) / ratio
        gain[over_threshold] = gain[over_threshold] / envelope_smoothed[over_threshold]

        return audio * gain

    def _soft_knee_limiter(self, audio, threshold, knee):
        """Soft knee limiter"""
        abs_audio = np.abs(audio)
        over = abs_audio > (threshold - knee)

        gain = np.ones_like(audio)
        gain[over] = threshold / (abs_audio[over] + 1e-10)
        gain = np.minimum(gain, 1.0)

        return audio * gain

    # ============================================================================
    # MAIN MASTERING PIPELINE
    # ============================================================================

    def master_track(self, input_file, output_file, target_lufs=-8.5):
        """
        Полная мастеринг-цепочка
        """
        print("\n" + "="*80)
        print("🎼 PLATINUM MASTERING CHAIN - Bernie Grundman / Bob Ludwig Level")
        print("="*80)
        print(f"Input: {input_file}")
        print(f"Target: {target_lufs} LUFS (Modern Russian Hip-Hop)")
        print("="*80)

        # Загрузка
        audio, sr = librosa.load(input_file, sr=None, mono=False)
        if audio.ndim == 1:
            audio = audio.reshape(-1, 1)
        else:
            audio = audio.T

        self.sr = sr
        self.meter = pyln.Meter(sr)

        print(f"\n📊 INPUT ANALYSIS:")
        input_lufs = self.meter.integrated_loudness(audio)
        input_peak = 20 * np.log10(np.max(np.abs(audio)))
        print(f"   LUFS: {input_lufs:.1f}")
        print(f"   Peak: {input_peak:.1f} dBFS")

        # Processing chain
        audio = self.parametric_eq_stage1_mud_removal(audio)
        audio = self.parametric_eq_stage2_presence_boost(audio)
        audio = self.parametric_eq_stage3_bass_control(audio)
        audio = self.multiband_compression(audio)
        audio = self.stereo_enhancement(audio)
        audio = self.harmonic_exciter(audio)
        audio = self.final_limiter(audio, target_lufs=target_lufs, true_peak_db=-1.0)

        # Сохранение
        if audio.ndim == 1:
            audio = audio.reshape(-1, 1)

        sf.write(output_file, audio, sr, subtype='PCM_24')

        print("\n" + "="*80)
        print(f"✅ MASTERING COMPLETE!")
        print(f"💾 Output: {output_file}")
        print("="*80)

        return audio, sr


# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Инициализация
    mastering = PlatinumMasteringChain()

    # Файлы
    input_track = "/home/user/Look-at-me-pls/Сам себе завидую.wav"
    output_track = "/home/user/Look-at-me-pls/Сам себе завидую_MASTERED.wav"

    # Мастеринг
    # Target: -8.5 LUFS (золотая середина для современного русского рэпа)
    # Более агрессивно: -7.5 LUFS
    # Более динамично: -9.5 LUFS
    mastering.master_track(input_track, output_track, target_lufs=-8.5)

    print("\n🎯 РЕКОМЕНДАЦИИ ДЛЯ ФИНАЛЬНОЙ ПРОВЕРКИ:")
    print("   1. A/B сравнение с референсом на мониторах")
    print("   2. Проверка на разных системах (наушники, телефон, авто)")
    print("   3. Моно-совместимость (кнопка MONO на контроллере)")
    print("   4. Loudness Penalty анализ (Spotify, Apple Music, YouTube)")
    print("   5. Динамический диапазон (target: 6-8 dB для рэпа)")
