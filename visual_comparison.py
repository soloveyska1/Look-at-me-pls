#!/usr/bin/env python3
"""
Визуализация мастеринг-цепи и сравнение до/после
"""

import matplotlib.pyplot as plt
import numpy as np

def create_mastering_visualization():
    """
    Создает визуальные графики для понимания мастеринга
    """

    # Настройка стиля
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(16, 12))

    # 1. ЧАСТОТНЫЙ БАЛАНС: ДО vs ПОСЛЕ
    ax1 = plt.subplot(3, 2, 1)

    bands = ['Sub\n20-60', 'Bass\n60-250', 'Low-Mid\n250-500', 'Mids\n500-2k',
             'Upper-Mid\n2k-4k', 'Presence\n4k-6k', 'Brilliance\n6k-20k']

    # ДО (текущий мастер)
    before = [41.8, 90.9, 45.0, 100.0, 12.6, 8.0, 18.3]

    # ПОСЛЕ (целевой)
    after = [75, 80, 25, 95, 70, 55, 80]

    x = np.arange(len(bands))
    width = 0.35

    bars1 = ax1.bar(x - width/2, before, width, label='ДО', color='#ff4444', alpha=0.8)
    bars2 = ax1.bar(x + width/2, after, width, label='ПОСЛЕ', color='#44ff44', alpha=0.8)

    ax1.set_ylabel('Относительная энергия (%)', fontsize=12, fontweight='bold')
    ax1.set_title('ЧАСТОТНЫЙ БАЛАНС: До vs После Мастеринга', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(bands, fontsize=10)
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 110)

    # Добавляем проблемные зоны
    ax1.axhspan(0, 30, alpha=0.1, color='red')
    ax1.text(6, 5, 'Проблема: нет яркости', fontsize=9, color='red')

    # 2. LOUDNESS COMPARISON
    ax2 = plt.subplot(3, 2, 2)

    metrics = ['LUFS', 'RMS\n(dBFS)', 'Peak\n(dBFS)', 'Crest\nFactor']
    before_loudness = [-20.75, -23.65, -2.37, 21.28]
    after_loudness = [-8.5, -9.5, -1.0, 7.5]

    x2 = np.arange(len(metrics))
    bars3 = ax2.bar(x2 - width/2, before_loudness, width, label='ДО', color='#ff4444', alpha=0.8)
    bars4 = ax2.bar(x2 + width/2, after_loudness, width, label='ПОСЛЕ', color='#44ff44', alpha=0.8)

    ax2.set_ylabel('dB / LUFS', fontsize=12, fontweight='bold')
    ax2.set_title('ГРОМКОСТЬ И ДИНАМИКА', fontsize=14, fontweight='bold')
    ax2.set_xticks(x2)
    ax2.set_xticklabels(metrics, fontsize=10)
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='white', linestyle='--', alpha=0.5)

    # 3. EQ CURVE (МАСТЕРИНГ)
    ax3 = plt.subplot(3, 2, 3)

    freqs = np.array([30, 45, 120, 180, 350, 500, 1000, 2000, 3500, 6000, 10000, 14000, 20000])
    gains = np.array([0, 1.5, -1.2, -2.0, -4.5, 0, 0, 0, 3.2, 4.0, 4.8, 2.5, 2.5])

    ax3.semilogx(freqs, gains, 'o-', linewidth=3, markersize=8, color='#44ffff')
    ax3.fill_between(freqs, 0, gains, alpha=0.3, color='#44ffff')
    ax3.set_xlabel('Частота (Hz)', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Усиление (dB)', fontsize=12, fontweight='bold')
    ax3.set_title('МАСТЕРИНГ EQ КРИВАЯ', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3, which='both')
    ax3.axhline(y=0, color='white', linestyle='--', linewidth=2)

    # Аннотации ключевых точек
    ax3.annotate('MUD CUT\n-4.5 dB', xy=(350, -4.5), xytext=(200, -7),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=10, color='red', fontweight='bold')

    ax3.annotate('PRESENCE\n+3.2 dB', xy=(3500, 3.2), xytext=(5000, 5),
                arrowprops=dict(arrowstyle='->', color='lime', lw=2),
                fontsize=10, color='lime', fontweight='bold')

    ax3.annotate('AIR\n+4.8 dB', xy=(10000, 4.8), xytext=(6000, 7),
                arrowprops=dict(arrowstyle='->', color='cyan', lw=2),
                fontsize=10, color='cyan', fontweight='bold')

    ax3.set_xlim(20, 20000)
    ax3.set_ylim(-6, 8)

    # 4. STEREO WIDTH
    ax4 = plt.subplot(3, 2, 4)

    freq_bands_stereo = ['20-200\nHz', '200-2k\nHz', '2k-8k\nHz', '8k-20k\nHz', 'Overall']
    before_width = [0, 15, 15, 15, 15.2]
    after_width = [0, 30, 60, 40, 45]

    x4 = np.arange(len(freq_bands_stereo))
    bars5 = ax4.bar(x4 - width/2, before_width, width, label='ДО', color='#ff4444', alpha=0.8)
    bars6 = ax4.bar(x4 + width/2, after_width, width, label='ПОСЛЕ', color='#44ff44', alpha=0.8)

    ax4.set_ylabel('Stereo Width (%)', fontsize=12, fontweight='bold')
    ax4.set_title('STEREO ШИРИНА ПО ЧАСТОТАМ (M/S Processing)', fontsize=14, fontweight='bold')
    ax4.set_xticks(x4)
    ax4.set_xticklabels(freq_bands_stereo, fontsize=10)
    ax4.legend(fontsize=11)
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim(0, 70)

    # Целевая зона
    ax4.axhspan(40, 55, alpha=0.2, color='green')
    ax4.text(3.5, 48, 'Target Zone', fontsize=9, color='lime')

    # 5. STREAMING PLATFORM LOUDNESS
    ax5 = plt.subplot(3, 2, 5)

    platforms = ['Spotify\n-14', 'Apple\n-16', 'YouTube\n-13', 'Яндекс\n-14', 'ВАШ\nМАСТЕР']
    platform_lufs = [-14, -16, -13, -14, -8.5]
    colors_platform = ['#1DB954', '#FC3C44', '#FF0000', '#FFDB4D', '#00FF00']

    bars7 = ax5.bar(platforms, platform_lufs, color=colors_platform, alpha=0.8, edgecolor='white', linewidth=2)
    ax5.set_ylabel('LUFS', fontsize=12, fontweight='bold')
    ax5.set_title('СОВМЕСТИМОСТЬ СО СТРИМИНГОМ', fontsize=14, fontweight='bold')
    ax5.grid(True, alpha=0.3, axis='y')
    ax5.axhline(y=-8.5, color='lime', linestyle='--', linewidth=2, label='Ваш мастер')

    # Аннотация
    ax5.text(4, -6, 'Громче всех targets!\nНе будет понижен',
             fontsize=11, color='lime', fontweight='bold',
             ha='center', bbox=dict(boxstyle='round', facecolor='black', alpha=0.8))

    ax5.set_ylim(-18, 0)
    ax5.legend(fontsize=10)

    # 6. MULTIBAND COMPRESSION RATIOS
    ax6 = plt.subplot(3, 2, 6)

    mb_bands = ['LOW\n20-150 Hz', 'LOW-MID\n150-800 Hz\n(MUD)', 'MID-HIGH\n800-5k Hz\n(VOCAL)', 'HIGH\n5k-20k Hz']
    ratios = [3.0, 4.0, 2.5, 2.0]
    thresholds = [-18, -20, -16, -14]

    x6 = np.arange(len(mb_bands))

    # Ratios
    ax6_ratio = ax6
    bars8 = ax6_ratio.bar(x6, ratios, color=['#4477ff', '#ff4444', '#44ff44', '#ffaa44'],
                          alpha=0.8, edgecolor='white', linewidth=2)
    ax6_ratio.set_ylabel('Compression Ratio', fontsize=12, fontweight='bold', color='cyan')
    ax6_ratio.set_title('MULTIBAND COMPRESSION НАСТРОЙКИ', fontsize=14, fontweight='bold')
    ax6_ratio.set_xticks(x6)
    ax6_ratio.set_xticklabels(mb_bands, fontsize=9)
    ax6_ratio.tick_params(axis='y', labelcolor='cyan')
    ax6_ratio.set_ylim(0, 5)
    ax6_ratio.grid(True, alpha=0.3, axis='y')

    # Thresholds (вторая ось)
    ax6_thresh = ax6_ratio.twinx()
    line = ax6_thresh.plot(x6, thresholds, 'o-', color='orange', linewidth=3,
                           markersize=10, label='Threshold (dB)')
    ax6_thresh.set_ylabel('Threshold (dB)', fontsize=12, fontweight='bold', color='orange')
    ax6_thresh.tick_params(axis='y', labelcolor='orange')
    ax6_thresh.set_ylim(-25, -10)

    # Добавляем текст на барах
    for i, (bar, ratio, thresh) in enumerate(zip(bars8, ratios, thresholds)):
        height = bar.get_height()
        ax6_ratio.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                      f'{ratio}:1', ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig('/home/user/Look-at-me-pls/mastering_visualization.png', dpi=150, bbox_inches='tight')
    print("✅ Визуализация сохранена: mastering_visualization.png")

    return fig


def create_signal_flow_diagram():
    """
    Текстовая диаграмма signal flow
    """
    print("\n" + "="*80)
    print("VISUAL SIGNAL FLOW - MASTERING CHAIN")
    print("="*80)

    print("""
    ┌──────────────────────────────────────────────────────────────────┐
    │                      INPUT AUDIO                                 │
    │          "Сам себе завидую.wav"                                  │
    │     -20.75 LUFS | 15.2% width | Muddy | No brilliance            │
    └──────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
    ╔══════════════════════════════════════════════════════════════════╗
    ║  STAGE 1: SURGICAL EQ - MUD REMOVAL                              ║
    ╟──────────────────────────────────────────────────────────────────╢
    ║  [HPF @ 30 Hz] → [CUT @ 350 Hz: -4.5 dB] → [CUT @ 180 Hz: -2 dB] ║
    ╚══════════════════════════════════════════════════════════════════╝
                                 │
                                 ▼
    ╔══════════════════════════════════════════════════════════════════╗
    ║  STAGE 2: PRESENCE & BRILLIANCE                                  ║
    ╟──────────────────────────────────────────────────────────────────╢
    ║  [3.5k: +3.2] → [10k: +4.8] → [14k: +2.5]                        ║
    ╚══════════════════════════════════════════════════════════════════╝
                                 │
                                 ▼
    ╔══════════════════════════════════════════════════════════════════╗
    ║  STAGE 3: BASS CONTROL                                           ║
    ╟──────────────────────────────────────────────────────────────────╢
    ║  [45 Hz: +1.5] → [120 Hz: -1.2]                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
                                 │
                                 ▼
    ╔══════════════════════════════════════════════════════════════════╗
    ║  STAGE 4: MULTIBAND COMPRESSION                                  ║
    ╟──────────────────────────────────────────────────────────────────╢
    ║  LOW: 3:1 │ LOW-MID: 4:1 │ MID: 2.5:1 │ HIGH: 2:1                ║
    ║  Parallel: 70% dry + 30% wet                                     ║
    ╚══════════════════════════════════════════════════════════════════╝
                                 │
                                 ▼
    ╔══════════════════════════════════════════════════════════════════╗
    ║  STAGE 5: STEREO ENHANCEMENT (M/S)                               ║
    ╟──────────────────────────────────────────────────────────────────╢
    ║  Bass: MONO │ Mids: 180% │ Highs: 140% → Total: 45%              ║
    ╚══════════════════════════════════════════════════════════════════╝
                                 │
                                 ▼
    ╔══════════════════════════════════════════════════════════════════╗
    ║  STAGE 6: HARMONIC EXCITATION                                    ║
    ╟──────────────────────────────────────────────────────────────────╢
    ║  Tape Saturation: 12% drive, 25% wet (2nd + 3rd harmonics)       ║
    ╚══════════════════════════════════════════════════════════════════╝
                                 │
                                 ▼
    ╔══════════════════════════════════════════════════════════════════╗
    ║  STAGE 7: TRUE PEAK LIMITING                                     ║
    ╟──────────────────────────────────────────────────────────────────╢
    ║  Target: -8.5 LUFS │ True Peak: -1.0 dBTP │ Transparent          ║
    ╚══════════════════════════════════════════════════════════════════╝
                                 │
                                 ▼
    ┌──────────────────────────────────────────────────────────────────┐
    │                    OUTPUT MASTERED AUDIO                         │
    │           "Сам себе завидую_MASTERED.wav"                        │
    │      -8.5 LUFS | 45% width | Clean | Brilliant | STREAMING-READY │
    └──────────────────────────────────────────────────────────────────┘
    """)

    print("="*80 + "\n")


if __name__ == "__main__":
    # Создаем визуализацию
    print("🎨 Создание визуализаций мастеринг-процесса...\n")

    # Signal flow diagram
    create_signal_flow_diagram()

    # Графики
    try:
        create_mastering_visualization()
        print("\n✅ Все визуализации созданы успешно!")
        print("📊 Файл: mastering_visualization.png")
    except Exception as e:
        print(f"⚠️ Ошибка при создании графиков: {e}")
        print("Возможно, нет дисплея для matplotlib. Используй текстовую диаграмму выше.")
