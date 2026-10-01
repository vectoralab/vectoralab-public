# VectoraLab

**Edge-assisted condition monitoring for industrial machinery**

VectoraLab is an industrial condition-monitoring system designed to analyze vibration data from rotating machinery such as motors and bearings.

The system combines **vibration sensing, edge processing, signal analysis, and software-based health assessment** to help identify abnormal machine behavior.

---

## System Overview

The current system architecture is based on:

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

The sensor captures machine vibration at a **5 kHz sampling rate**. The STM32H750 is intended to perform on-machine processing before sending processed data to the software layer.

---

## Current Development Status

| Component                           | Status                  |
| ----------------------------------- | ----------------------- |
| Vibration analysis software         | Implemented             |
| Health Score                        | Implemented in software |
| IIS3DWB sensor integration          | Hardware development    |
| STM32H750 platform                  | Hardware development    |
| Embedded signal-processing pipeline | In development          |
| INT8 TinyML inference on STM32      | In development          |
| Hardware prototype / PCB            | Under construction      |

The project is currently transitioning from software development toward hardware prototyping and embedded implementation.

---

## Core Technologies

### Hardware

* **MCU:** STM32H750
* **Vibration Sensor:** IIS3DWB
* **Sampling Rate:** 5 kHz
* **Target Application:** Rotating industrial machinery

### Signal Processing

The software analysis pipeline can work with vibration signals and extract characteristics such as:

* RMS
* Peak amplitude
* Crest factor
* Kurtosis
* Frequency-domain characteristics
* FFT-based spectral information

Additional signal-processing and machine-learning components are being developed as the embedded system progresses.

---

## Health Score

VectoraLab includes a software-based **Health Score** intended to provide a compact representation of machine condition.

The score is derived from vibration-related characteristics and is intended to help distinguish normal machine behavior from potentially abnormal conditions.

The current Health Score implementation is part of the software platform. Its embedded implementation is part of the ongoing development of the STM32-based edge system.

---

## Vibration Analysis Example

This repository includes simplified examples demonstrating vibration-signal analysis.

The examples are intended for:

* Understanding vibration signals
* Exploring time-domain characteristics
* Visualizing frequency-domain behavior
* Experimenting with basic signal-processing concepts

They are educational and demonstrative examples rather than the complete VectoraLab production software.

---

## Project Architecture

VectoraLab follows a two-level analysis concept:

### 1. Edge Layer

The STM32H750 is responsible for processing vibration data close to the machine.

The goal is to reduce unnecessary data transfer and enable low-latency machine-condition assessment.

### 2. Software Layer

The software provides deeper analysis, visualization, monitoring, and health assessment.

This separation allows computationally intensive analysis to remain available at the software level while selected processing can be moved closer to the machine.

---

## Repository Scope

This repository is a **public technical showcase** for VectoraLab.

It contains selected documentation, examples, signal-processing demonstrations, sample data, and technical material related to the project.

The production application source code, authentication system, administration panel, billing infrastructure, private configuration, deployment configuration, and other proprietary components are intentionally not included.

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

## Project Status

**Status: Active development**

VectoraLab is currently moving from a software-focused prototype toward an integrated hardware and software condition-monitoring system.

---

## About

VectoraLab is being developed as an industrial technology project focused on practical machine-condition monitoring using embedded systems, digital signal processing, and machine learning.

Website: https://vectoralab.site/
