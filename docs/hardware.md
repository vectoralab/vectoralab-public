# VectoraLab — Hardware

## Overview

The VectoraLab hardware platform is being developed to acquire vibration data from rotating industrial machinery and perform selected processing close to the machine.

The current hardware architecture is centered around:

* **Vibration sensor:** IIS3DWB
* **Microcontroller:** STM32H750
* **Sampling rate:** 5 kHz
* **Application:** Industrial machinery condition monitoring

The physical prototype is currently under construction.

---

## Hardware Architecture

The intended hardware data path is:

```text
┌─────────────────────┐
│ Industrial Machine  │
│ Motor / Bearing     │
└──────────┬──────────┘
           │
           │ Mechanical Vibration
           ▼
┌─────────────────────┐
│      IIS3DWB        │
│  3-Axis Accelerometer│
└──────────┬──────────┘
           │
           │ Digital Data
           ▼
┌─────────────────────┐
│     STM32H750       │
│    Edge MCU         │
└──────────┬──────────┘
           │
           │ Processed Data
           ▼
┌─────────────────────┐
│ VectoraLab Software │
└─────────────────────┘
```

---

## IIS3DWB Vibration Sensor

The IIS3DWB is used as the primary vibration sensing component.

It is a digital three-axis accelerometer designed for vibration-monitoring applications.

Within VectoraLab, the sensor is intended to capture machine vibration and provide digital acceleration measurements to the embedded processing platform.

### Role in VectoraLab

The sensor is responsible for:

* Measuring vibration along three axes
* Providing digital acceleration samples
* Feeding vibration data into the STM32H750
* Supporting time-domain and frequency-domain analysis

### Current Configuration

| Parameter          | Current Design               |
| ------------------ | ---------------------------- |
| Sensor             | IIS3DWB                      |
| Measurement        | 3-axis acceleration          |
| Sampling rate      | 5 kHz                        |
| Application        | Machine vibration monitoring |
| Integration status | In development               |

The final mechanical mounting, electrical implementation, and field performance will be validated during hardware testing.

---

## STM32H750

The STM32H750 is the selected microcontroller for the VectoraLab edge-processing platform.

Its purpose is to provide a computational layer between the vibration sensor and the higher-level software.

### Intended Responsibilities

The MCU is being developed to handle:

1. Sensor communication
2. Vibration data acquisition
3. Data buffering
4. Signal preprocessing
5. Feature extraction
6. Selected signal-processing operations
7. Communication with the software layer
8. Future embedded ML inference

The STM32H750 implementation is currently under development.

---

## Sampling

The current VectoraLab design uses a:

**5 kHz vibration sampling rate**

At this sampling rate, the system can theoretically represent frequency components below the Nyquist frequency:

```text
Sampling Rate = 5000 Hz

Nyquist Frequency = 5000 / 2

                 = 2500 Hz
```

Therefore, for a conventional sampled signal, frequency components above approximately **2.5 kHz** require appropriate filtering and sampling considerations to avoid aliasing.

The final acquisition and anti-aliasing implementation will be validated during hardware development.

---

## Sensor-to-MCU Interface

The IIS3DWB provides digital sensor data to the embedded platform.

The intended connection is between the vibration sensor and the STM32H750, with the MCU responsible for acquiring and buffering the samples.

A simplified interface model is:

```text
IIS3DWB
   │
   │ Digital Interface
   ▼
STM32H750
   │
   ├── Sample Buffer
   ├── Signal Processing
   ├── Feature Extraction
   └── Communication
```

The exact electrical implementation and final PCB routing are part of the ongoing hardware development.

---

## Edge Processing

One of the main design goals of VectoraLab is to perform selected processing close to the monitored machine.

Instead of treating the embedded device only as a data acquisition interface, the STM32H750 is intended to become an active processing node.

Potential operations include:

* Signal conditioning
* Windowing
* FFT processing
* Statistical feature extraction
* Data reduction
* Machine-learning inference

The exact distribution of processing between the MCU and software will be determined through implementation and testing.

---

## Embedded Machine Learning

An INT8 TinyML inference pipeline is currently under development for the STM32H750.

The objective is to investigate whether machine-condition assessment can be performed directly on the edge device.

The current development status is:

```text
Model development
       ↓
Quantization / INT8
       ↓
STM32 deployment
       ↓
Embedded inference
       ↓
Validation
```

This pipeline should be considered **in development**, not a completed production feature.

---

## Hardware Prototype

The physical VectoraLab hardware prototype is currently being assembled.

The current development stage includes:

* Component selection
* Hardware architecture
* Sensor integration planning
* MCU integration planning
* PCB development / assembly
* Preparation for real-machine testing

The prototype will be used to validate the complete data path under real operating conditions.

---

## Validation Plan

Hardware validation will be performed incrementally.

### Stage 1 — Sensor Validation

Verify:

* Sensor communication
* Sample acquisition
* Axis readings
* Sampling stability

### Stage 2 — MCU Acquisition

Verify:

* Continuous sampling
* Buffering
* Timing
* Data integrity
* Communication

### Stage 3 — Signal Processing

Verify:

* Time-domain calculations
* FFT results
* Feature extraction
* Processing performance

### Stage 4 — Software Integration

Verify:

* Machine-to-software data transfer
* Signal visualization
* Feature monitoring
* Health Score behavior

### Stage 5 — Real Machine Testing

Test the system using vibration data collected from actual rotating machinery.

This stage will be used to evaluate the behavior of the complete hardware/software system under real operating conditions.

---

## Current Hardware Status

| Component               | Status             |
| ----------------------- | ------------------ |
| IIS3DWB selection       | Selected           |
| STM32H750 selection     | Selected           |
| Sampling design         | 5 kHz              |
| Sensor integration      | In development     |
| Embedded processing     | In development     |
| TinyML inference        | In development     |
| PCB / prototype         | Under construction |
| Real-machine validation | Not completed      |

---

## Important Note

The specifications and architecture documented here describe the **current development design**.

Performance characteristics such as processing latency, power consumption, model accuracy, vibration-detection accuracy, and long-term reliability have not been presented as final specifications unless they have been experimentally validated.

The hardware documentation will be updated as the prototype moves through implementation and testing.
