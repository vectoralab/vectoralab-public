# VectoraLab — Product Overview

## Overview

VectoraLab is an industrial condition-monitoring system focused on detecting abnormal behavior in rotating machinery through vibration analysis.

The system is designed around a simple data path:

```text
Machine
   ↓
Vibration Sensor
   ↓
Embedded Processing
   ↓
Signal Analysis
   ↓
Health Assessment
   ↓
VectoraLab Software
```

The goal is to connect physical machine behavior with software-based analysis and provide a practical way to monitor machine condition.

---

## Target Applications

VectoraLab is primarily designed for rotating industrial equipment such as:

* Electric motors
* Rotating machinery
* Bearings
* Production-line equipment
* Other vibration-sensitive mechanical systems

The same signal-processing concepts can potentially be adapted to other machinery where vibration is a useful indicator of mechanical condition.

---

## How It Works

### 1. Vibration Acquisition

An **IIS3DWB three-axis digital accelerometer** is used to capture vibration from the monitored machine.

The current system design uses a **5 kHz sampling rate** for vibration acquisition.

The sensor is intended to be mounted close to the monitored mechanical system so that its measurements represent the machine's physical vibration behavior.

### 2. Embedded Processing

An **STM32H750** microcontroller is being developed as the edge-processing platform.

The purpose of the embedded layer is to move selected signal-processing operations closer to the machine.

This can reduce unnecessary raw-data transmission and provide a foundation for near-real-time condition assessment.

### 3. Signal Processing

Vibration signals can be analyzed in both the time and frequency domains.

Current software analysis includes characteristics such as:

* RMS
* Peak amplitude
* Crest factor
* Kurtosis
* FFT-based spectral analysis
* Frequency-domain characteristics

These features provide different views of the measured vibration signal.

### 4. Health Assessment

VectoraLab currently includes a software-based **Health Score**.

The Health Score provides a compact representation of the analyzed machine condition and can be used as a basis for monitoring changes in machine behavior.

The embedded implementation of the complete health-assessment pipeline is still under development.

---

## Two-Level Processing Architecture

VectoraLab follows a two-level processing concept.

### Edge Layer

The edge layer is based on the STM32H750 and vibration sensor.

Its development focuses on:

* Sensor acquisition
* Embedded signal processing
* Feature extraction
* Efficient data transfer
* Future embedded machine-learning inference

### Software Layer

The software layer provides:

* Vibration analysis
* Visualization
* Feature analysis
* Health assessment
* Monitoring functionality

The software layer is currently more mature than the embedded hardware layer.

---

## Machine Learning

An INT8 TinyML inference pipeline for the STM32 platform is currently **under development**.

The purpose of this component is to investigate whether selected machine-learning models can be deployed directly on the edge device for machine-condition analysis.

This repository does not present the embedded TinyML system as completed.

---

## Current Development Stage

VectoraLab is currently transitioning from a software-focused prototype toward an integrated hardware and software system.

### Implemented

* Software-based vibration analysis
* Software-based Health Score
* Vibration visualization and spectral analysis
* Initial system architecture

### In Development

* STM32H750 embedded processing
* IIS3DWB hardware integration
* Embedded signal-processing pipeline
* INT8 TinyML inference
* Machine-to-software communication

### Under Construction

* Physical hardware prototype
* PCB / hardware assembly
* End-to-end validation with real machine vibration

---

## Design Philosophy

VectoraLab is being developed around several principles:

### Edge-Assisted Processing

Move selected processing closer to the machine while retaining the flexibility of software-based analysis.

### Signal-Based Assessment

Use measurable vibration characteristics rather than relying only on a single raw signal representation.

### Modular Architecture

Keep sensing, embedded processing, signal analysis, and software visualization as separate layers so that individual components can evolve independently.

### Progressive Validation

Develop and validate the system incrementally, moving from software analysis to embedded processing and finally to physical machine testing.

---

## Project Scope

This public repository contains selected technical documentation, examples, sample data, and educational material related to VectoraLab.

The production software, private infrastructure, authentication, billing, administration, deployment configuration, and other proprietary implementation details are intentionally excluded.

---

## Project Status

**Active development**

The software analysis layer is operational, while the embedded hardware and edge-processing components are currently being developed and assembled.
