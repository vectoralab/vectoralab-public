# VectoraLab — System Architecture

## Overview

VectoraLab is designed as a layered condition-monitoring system in which vibration data moves from the physical machine through sensing and embedded processing before reaching the software analysis layer.

The architecture separates the system into several functional stages:

```text
┌─────────────────────────┐
│    Industrial Machine   │
│   Motor / Bearing /     │
│   Rotating Equipment    │
└────────────┬────────────┘
             │
             │ Mechanical Vibration
             ▼
┌─────────────────────────┐
│       IIS3DWB           │
│   3-Axis Accelerometer  │
└────────────┬────────────┘
             │
             │ Digital Vibration Data
             │ 5 kHz Sampling
             ▼
┌─────────────────────────┐
│      STM32H750          │
│    Edge Processing      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Signal Processing     │
│                         │
│ • Time-domain features  │
│ • Frequency analysis    │
│ • FFT                   │
│ • Statistical features  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     Health Assessment   │
│                         │
│      Health Score       │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   VectoraLab Software   │
│                         │
│ • Visualization         │
│ • Analysis              │
│ • Monitoring            │
└─────────────────────────┘
```

---

## 1. Machine Layer

The first layer is the physical machine being monitored.

The primary target is rotating industrial machinery where vibration characteristics can provide information about mechanical behavior.

Typical examples include:

* Electric motors
* Bearings
* Rotating assemblies
* Production-line machinery

Mechanical vibration is measured as the machine operates.

---

## 2. Sensing Layer

### IIS3DWB

VectoraLab uses the **IIS3DWB** digital three-axis accelerometer as the vibration sensing component.

The sensor provides digital acceleration measurements along three axes.

The current system design uses a:

**5 kHz sampling rate**

The sensor is intended to capture vibration close to the monitored mechanical system and provide the raw measurement used by subsequent processing stages.

```text
Machine
   │
   │ Vibration
   ▼
IIS3DWB
   │
   ├── X-axis
   ├── Y-axis
   └── Z-axis
```

---

## 3. Edge Processing Layer

### STM32H750

The STM32H750 is the planned embedded processing platform for VectoraLab.

Its role is to perform selected processing operations directly near the monitored machine.

The embedded layer is currently under development.

The intended responsibilities include:

* Sensor data acquisition
* Data buffering
* Signal preprocessing
* Feature extraction
* Communication with the software layer
* Future embedded machine-learning inference

The physical hardware prototype is currently under construction.

---

## 4. Signal Processing Layer

Vibration data can contain useful information in both the time and frequency domains.

VectoraLab's software analysis layer currently works with several vibration characteristics.

### Time-Domain Analysis

Examples include:

* RMS
* Peak amplitude
* Crest factor
* Kurtosis

These characteristics can describe signal amplitude, impulsiveness, and statistical behavior.

### Frequency-Domain Analysis

Frequency-domain analysis can reveal periodic components and changes in the spectral distribution of vibration.

FFT-based analysis is used to transform vibration data from the time domain into a frequency-domain representation.

```text
Time-domain signal
        │
        ▼
     Windowing
        │
        ▼
       FFT
        │
        ▼
Frequency spectrum
```

---

## 5. Feature Layer

Different signal characteristics provide different information about machine vibration.

A simplified feature-processing path is:

```text
Raw Vibration
      │
      ├───────────────┐
      ▼               ▼
Time Domain      Frequency Domain
      │               │
      ├─ RMS           ├─ FFT
      ├─ Peak          ├─ Spectral features
      ├─ Crest         └─ Frequency components
      └─ Kurtosis
              │
              ▼
       Feature Set
```

The feature set can then be used by the health-assessment layer.

---

## 6. Health Assessment

VectoraLab currently implements a software-based **Health Score**.

The purpose of the Health Score is to provide a compact representation of the analyzed vibration condition.

A simplified conceptual pipeline is:

```text
Vibration Data
      │
      ▼
Signal Processing
      │
      ▼
Feature Extraction
      │
      ▼
Feature Evaluation
      │
      ▼
Health Score
```

The current Health Score is implemented in the software layer.

The complete embedded implementation is not yet considered finished.

---

## 7. Embedded Machine Learning

An INT8 TinyML inference pipeline for the STM32H750 is currently under development.

The intended architecture is:

```text
Vibration Data
      │
      ▼
Preprocessing
      │
      ▼
Feature / Model Input
      │
      ▼
INT8 ML Inference
      │
      ▼
Machine Condition Assessment
```

The objective is to investigate machine-learning inference directly on the edge device.

The public repository does not claim that this embedded inference pipeline is complete.

---

## 8. Software Layer

The VectoraLab software acts as the higher-level analysis and monitoring environment.

Its responsibilities include:

* Processing vibration data
* Visualizing signals
* Frequency-domain analysis
* Feature analysis
* Health assessment
* Monitoring machine behavior

The software layer is currently ahead of the embedded hardware implementation in terms of development maturity.

---

## 9. Data Flow

The intended end-to-end data path is:

```text
┌──────────┐
│ Machine  │
└────┬─────┘
     │
     │ Vibration
     ▼
┌──────────┐
│ IIS3DWB  │
└────┬─────┘
     │
     │ Digital Samples
     ▼
┌──────────┐
│ STM32H750│
└────┬─────┘
     │
     │ Processed / Selected Data
     ▼
┌───────────────┐
│ VectoraLab    │
│ Software      │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│ Visualization │
│ + Analysis    │
│ + Health      │
│   Assessment  │
└───────────────┘
```

This architecture is being implemented incrementally.

---

## 10. Development Boundaries

The system currently has three different maturity levels:

### Implemented

* Software vibration analysis
* FFT-based visualization
* Statistical vibration features
* Software Health Score

### Under Development

* STM32H750 embedded processing
* IIS3DWB hardware integration
* Embedded signal-processing pipeline
* INT8 TinyML inference
* Embedded-to-software communication

### Under Construction

* Physical hardware prototype
* PCB assembly
* Integrated machine-side testing

Keeping these stages separate is important because the public documentation should reflect the actual development state of the project.

---

## 11. Future Integration

The architecture is designed so that additional processing can gradually move from the software environment toward the edge device.

A future integrated system is expected to follow this general path:

```text
Machine
   ↓
IIS3DWB
   ↓
STM32H750
   ↓
Edge Signal Processing
   ↓
Embedded ML / Health Assessment
   ↓
Communication
   ↓
VectoraLab Software
   ↓
Monitoring & Visualization
```

The exact embedded processing pipeline and communication architecture will be finalized and validated during hardware development.

---

## Architecture Status

**Status: Active development**

The software analysis layer is operational. The STM32H750-based edge-processing and physical hardware layers are currently being developed and assembled.
