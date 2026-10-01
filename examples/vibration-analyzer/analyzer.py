import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


SAMPLE_RATE = 5000


def load_csv(filepath):
    """Load time and acceleration data from a CSV file."""

    times = []
    signal = []

    with open(filepath, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            times.append(float(row["time_s"]))
            signal.append(float(row["acceleration"]))

    return np.array(times), np.array(signal)


def calculate_features(signal):
    """Calculate basic time-domain vibration features."""

    rms = np.sqrt(np.mean(signal ** 2))
    peak = np.max(np.abs(signal))
    crest_factor = peak / rms

    mean = np.mean(signal)
    std = np.std(signal)

    kurtosis = np.mean((signal - mean) ** 4) / (std ** 4)

    return {
        "rms": rms,
        "peak": peak,
        "crest_factor": crest_factor,
        "kurtosis": kurtosis,
    }


def calculate_fft(signal):
    """Calculate the single-sided FFT spectrum."""

    signal = signal - np.mean(signal)

    window = np.hanning(len(signal))
    windowed_signal = signal * window

    spectrum = np.fft.rfft(windowed_signal)
    frequencies = np.fft.rfftfreq(
        len(signal),
        d=1 / SAMPLE_RATE,
    )

    magnitude = np.abs(spectrum)

    return frequencies, magnitude


def print_report(filepath, signal, frequencies, magnitude, features):
    """Print analysis results."""

    dominant_index = np.argmax(magnitude[1:]) + 1
    dominant_frequency = frequencies[dominant_index]

    duration = len(signal) / SAMPLE_RATE
    nyquist = SAMPLE_RATE / 2

    print("=" * 65)
    print("VectoraLab - Vibration Analyzer")
    print("=" * 65)

    print(f"Input file          : {filepath}")
    print(f"Sample rate         : {SAMPLE_RATE} Hz")
    print(f"Samples             : {len(signal)}")
    print(f"Duration            : {duration:.3f} s")
    print(f"Nyquist frequency   : {nyquist:.0f} Hz")

    print()
    print("Time-domain features:")
    print("-" * 65)

    print(f"RMS                 : {features['rms']:.4f}")
    print(f"Peak                : {features['peak']:.4f}")
    print(f"Crest Factor        : {features['crest_factor']:.4f}")
    print(f"Kurtosis            : {features['kurtosis']:.4f}")

    print()
    print(f"Dominant frequency  : {dominant_frequency:.2f} Hz")
    print("=" * 65)


def plot_results(times, signal, frequencies, magnitude, filepath):
    """Plot waveform and FFT spectrum."""

    fig, axes = plt.subplots(2, 1, figsize=(10, 7))

    axes[0].plot(times, signal)
    axes[0].set_title("Vibration Waveform")
    axes[0].set_xlabel("Time (s)")
    axes[0].set_ylabel("Acceleration")
    axes[0].grid(True)

    axes[1].plot(frequencies, magnitude)
    axes[1].set_title("Frequency Spectrum")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Magnitude")
    axes[1].set_xlim(0, min(500, SAMPLE_RATE / 2))
    axes[1].grid(True)

    fig.suptitle(
        f"VectoraLab Vibration Analysis - {Path(filepath).name}"
    )

    plt.tight_layout()
    plt.show()


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python analyzer.py <csv_file>")
        print()
        print("Example:")
        print("  python analyzer.py ../../sample-data/vibration/normal.csv")
        sys.exit(1)

    filepath = sys.argv[1]

    if not Path(filepath).exists():
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    times, signal = load_csv(filepath)

    features = calculate_features(signal)

    frequencies, magnitude = calculate_fft(signal)

    print_report(
        filepath,
        signal,
        frequencies,
        magnitude,
        features,
    )

    plot_results(
        times,
        signal,
        frequencies,
        magnitude,
        filepath,
    )


if __name__ == "__main__":
    main()
