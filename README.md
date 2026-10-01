# VectoraLab

**Edge-assisted condition monitoring for industrial machinery**

VectoraLab is an industrial condition-monitoring system designed to analyze vibration data from rotating machinery such as motors and bearings.

The system combines **vibration sensing, edge processing, digital signal processing, and software-based health assessment** to help identify abnormal machine behavior.

[Website](https://vectoralab.site/) · [Documentation](docs/) · [Latest Release](https://github.com/vectoralab/vectoralab-public/releases/latest)

---

## System Overview

VectoraLab follows a two-level analysis architecture: selected processing is performed close to the machine, while deeper analysis and visualization remain available at the software layer.

```text
Industrial Machine
       │
       ▼
   IIS3DWB
 Vibration Sensor
       │
       ▼
   STM32H750
  Edge Processing
       │
       ▼
 Signal Processing
       │
       ├── Time-domain features
       ├── Frequency-domain analysis
       └── Statistical features
       │
       ▼
   Health Score
       │
       ▼
 VectoraLab Software
```

The current sensing design uses the **IIS3DWB** vibration sensor with a **5 kHz sampling rate**. The STM32H750 is being developed as the on-machine processing platform.

---

## Current Development Status

| Component                           | Status                  |
| ----------------------------------- | ----------------------- |
| Vibration analysis software         | Implemented             |
| Health Score                        | Implemented in software |
| IIS3DWB hardware integration        | Under construction      |
| STM32H750 hardware platform         | Under construction      |
| Embedded signal-processing pipeline | In development          |
| INT8 TinyML inference on STM32      | In development          |
| Hardware prototype / PCB            | Under construction      |

The project is transitioning from a software-focused prototype toward an integrated hardware and software condition-monitoring system.

---

## Core Technologies

### Hardware

* **MCU:** STM32H750
* **Vibration Sensor:** IIS3DWB
* **Sampling Rate:** 5 kHz
* **Target:** Rotating industrial machinery

### Signal Processing

The current analysis examples demonstrate vibration-signal processing techniques including:

* RMS
* Peak amplitude
* Crest factor
* Kurtosis
* FFT
* Frequency-domain analysis
* Spectrogram / STFT

See the [signal-processing documentation](docs/signal-processing/) for more details.

---

## Health Score

VectoraLab includes a software-based **Health Score** intended to provide a compact representation of machine condition.

The current implementation uses vibration-related characteristics to help distinguish normal machine behavior from potentially abnormal conditions.

The software Health Score is implemented. Its embedded integration is part of the ongoing STM32-based development.

---

## Vibration Analysis Example

The repository includes a Python-based vibration analyzer and synthetic vibration datasets for demonstration and development.

Example datasets include:

* `normal.csv`
* `noisy.csv`
* `impulse.csv`

The analyzer demonstrates:

* Time-domain feature extraction
* FFT-based frequency analysis
* Dominant-frequency detection
* Basic vibration-signal visualization

Example:

```bash
cd examples/vibration-analyzer

python analyzer.py ../../sample-data/vibration/normal.csv
```

The included datasets are **synthetic** and are not measurements from a specific industrial machine.

See [`examples/vibration-analyzer/README.md`](examples/vibration-analyzer/README.md).

---

## Architecture

### Edge Layer

The STM32H750 is being developed to process vibration data close to the machine.

The intended role of the edge layer includes:

* Signal preprocessing
* Feature extraction
* Selected statistical calculations
* Future embedded ML inference

### Software Layer

The software layer provides deeper analysis, visualization, monitoring, and health assessment.

This separation allows selected processing to move closer to the machine while retaining more computationally intensive analysis at the software level.

See the [system architecture documentation](docs/system-architecture.md).

---

## Documentation

| Topic               | Documentation                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| Product overview    | [`docs/product-overview.md`](docs/product-overview.md)                                         |
| System architecture | [`docs/system-architecture.md`](docs/system-architecture.md)                                   |
| Hardware            | [`docs/hardware.md`](docs/hardware.md)                                                         |
| Vibration analysis  | [`docs/signal-processing/vibration-analysis.md`](docs/signal-processing/vibration-analysis.md) |
| FFT                 | [`docs/signal-processing/fft.md`](docs/signal-processing/fft.md)                               |
| Spectrogram / STFT  | [`docs/signal-processing/spectrogram.md`](docs/signal-processing/spectrogram.md)               |

---

## Repository Structure

```text
vectoralab-public/
├── docs/
│   ├── hardware.md
│   ├── product-overview.md
│   ├── system-architecture.md
│   └── signal-processing/
│       ├── fft.md
│       ├── spectrogram.md
│       └── vibration-analysis.md
│
├── examples/
│   └── vibration-analyzer/
│       ├── analyzer.py
│       └── README.md
│
├── sample-data/
│   └── vibration/
│       ├── generate_data.py
│       ├── normal.csv
│       ├── noisy.csv
│       └── impulse.csv
│
└── README.md
```

---

## Development Roadmap

Current development is focused on:

* Completing the STM32H750 hardware prototype
* Integrating the IIS3DWB sensor
* Implementing the embedded vibration-processing pipeline
* Developing INT8 TinyML inference on the MCU
* Connecting the embedded system to the VectoraLab software
* Testing the complete machine-to-software data path
* Validating the analysis pipeline using real machine vibration data

---

## Repository Scope

This repository is a **public technical showcase** for VectoraLab.

It contains selected documentation, examples, signal-processing demonstrations, synthetic sample data, and technical material related to the project.

The production application source code, authentication system, administration panel, billing infrastructure, private configuration, deployment configuration, and other proprietary components are intentionally not included.

---

## Project Status

**Status: Active development**

VectoraLab is currently moving from a software-focused prototype toward an integrated hardware and software condition-monitoring system.

---

## About

VectoraLab is an industrial technology project focused on practical machine-condition monitoring using embedded systems, digital signal processing, and machine learning.

**Website:** https://vectoralab.site/
