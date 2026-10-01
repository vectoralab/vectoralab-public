import csv
import math
import random
from pathlib import Path


SAMPLE_RATE = 5000
DURATION = 1.0
RPM = 1500

FREQUENCY = RPM / 60.0
N_SAMPLES = int(SAMPLE_RATE * DURATION)

OUTPUT_DIR = Path(__file__).parent


def generate_signal(condition):
    signal = []

    for i in range(N_SAMPLES):
        t = i / SAMPLE_RATE

        # Fundamental rotational component
        value = math.sin(2 * math.pi * FREQUENCY * t)

        # Second harmonic
        value += 0.25 * math.sin(
            2 * math.pi * 2 * FREQUENCY * t
        )

        if condition == "normal":
            noise = random.gauss(0, 0.05)
            value += noise

        elif condition == "noisy":
            noise = random.gauss(0, 0.25)
            value += noise

        elif condition == "impulse":
            noise = random.gauss(0, 0.05)
            value += noise

            # Periodic transient impulses
            impulse_period = int(SAMPLE_RATE / FREQUENCY)

            if i % impulse_period < 8:
                decay = math.exp(-(i % impulse_period) / 2.0)
                value += 2.5 * decay

        signal.append(value)

    return signal


def save_csv(filename, signal):
    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["time_s", "acceleration"])

        for i, value in enumerate(signal):
            time = i / SAMPLE_RATE
            writer.writerow([
                f"{time:.6f}",
                f"{value:.6f}"
            ])

    print(f"Created: {filepath}")


def main():
    random.seed(42)

    save_csv(
        "normal.csv",
        generate_signal("normal")
    )

    save_csv(
        "noisy.csv",
        generate_signal("noisy")
    )

    save_csv(
        "impulse.csv",
        generate_signal("impulse")
    )


if __name__ == "__main__":
    main()
