# Vibration Analysis

## Overview

Vibration analysis is one of the core processing stages in VectoraLab.

The basic idea is to transform a raw vibration signal into measurable characteristics that can be used to understand changes in machine behavior.

A simplified processing pipeline is:

```text
Raw Vibration Signal
        │
        ▼
Preprocessing
        │
        ▼
Time-Domain Analysis
        │
        ├── RMS
        ├── Peak
        ├── Crest Factor
        └── Kurtosis
        │
        ▼
Frequency-Domain Analysis
        │
        └── FFT
        │
        ▼
Feature Set
        │
        ▼
Health Assessment
```

---

## Raw Vibration Signal

The vibration sensor produces a sequence of acceleration measurements over time.

A discrete vibration signal can be represented as:

```text
x[0], x[1], x[2], ..., x[N-1]
```

where:

* `x[n]` is a sampled acceleration value
* `N` is the number of samples
* `n` is the sample index

For the current VectoraLab design:

```text
Sampling Rate = 5000 samples/second
```

The sampling interval is therefore:

```text
Ts = 1 / Fs

Ts = 1 / 5000

Ts = 0.0002 seconds
```

or:

```text
Ts = 0.2 ms
```

---

## Why Analyze Vibration?

Rotating machinery produces vibration during normal operation.

Changes in vibration behavior can be associated with changes in the mechanical system.

Examples of conditions that can affect vibration include:

* Mechanical imbalance
* Misalignment
* Bearing-related behavior
* Looseness
* Periodic mechanical forces
* Changes in operating conditions

The presence of a particular vibration pattern does not by itself prove a specific fault. Machine condition should be interpreted using appropriate operating context, baseline measurements, and validation.

---

# Time-Domain Analysis

Time-domain analysis examines the amplitude of the vibration signal directly as a function of time.

It is useful for measuring the overall magnitude and statistical characteristics of a vibration waveform.

---

## RMS

Root Mean Square (RMS) is a commonly used measure of the overall energy or magnitude of a vibration signal.

For a discrete signal:

```text
RMS = sqrt( (1/N) × Σ x[n]² )
```

RMS is useful for tracking changes in overall vibration amplitude.

For example, a monitoring system can compare the RMS value of a current measurement window with previous measurements.

```text
Low RMS
   │
   ├── Lower overall vibration amplitude
   │
   ▼
Higher RMS
   │
   └── Higher overall vibration amplitude
```

RMS alone should not be treated as a complete machine-diagnosis method.

---

## Peak Amplitude

Peak amplitude represents the largest absolute magnitude observed in a measurement window.

```text
Peak = max(|x[n]|)
```

Peak measurements can highlight short-duration high-amplitude events that may not be obvious from RMS alone.

For example:

```text
Normal waveform
────────────────────────

Signal with transient event
───────────────╱╲────────
                ↑
              Peak
```

---

## Crest Factor

Crest factor relates the peak amplitude to the RMS value:

```text
Crest Factor = Peak / RMS
```

It provides an indication of how strongly a signal is dominated by peaks relative to its overall level.

A signal containing impulsive events can exhibit a higher crest factor than a smoother waveform with a similar RMS level.

---

## Kurtosis

Kurtosis is a statistical measure that can help describe the distribution of signal amplitudes.

For a simplified standardized discrete signal:

```text
Kurtosis =
(1/N) × Σ ((x[n] - μ) / σ)⁴
```

where:

* `μ` is the signal mean
* `σ` is the standard deviation
* `N` is the number of samples

Kurtosis can be particularly useful when investigating impulsive characteristics in vibration signals.

However, kurtosis can also be affected by noise, measurement conditions, and signal preprocessing.

---

# Frequency-Domain Analysis

Time-domain features describe what happens to the signal amplitude over time.

Frequency-domain analysis provides another perspective by describing how signal content is distributed across frequencies.

The main tool used for this transformation is the **Fast Fourier Transform (FFT)**.

```text
Time Domain
     │
     ▼
    FFT
     │
     ▼
Frequency Domain
```

A frequency spectrum can help identify periodic components that may be difficult to distinguish directly from the time waveform.

---

## Example

Suppose a rotating machine produces a dominant periodic component.

In the time domain, this may appear as a repeating waveform.

In the frequency domain, the same behavior can appear as a concentration of spectral energy around a particular frequency.

```text
Time Domain

Amplitude
   │
   │    /╲    /╲    /╲
   │   /  ╲  /  ╲  /  ╲
───┴──────────────────────► Time


Frequency Domain

Amplitude
   │
   │        │
   │        │
   │        │
───┴────────┴──────────────► Frequency
            f
```

This separation between time and frequency representations is fundamental to vibration analysis.

---

# Windowing

When a finite section of a vibration signal is transformed using an FFT, windowing can be applied before the transform.

A window function reduces discontinuities at the boundaries of the selected signal segment.

A commonly used window is the **Hann window**.

Conceptually:

```text
Raw Frame
    │
    ▼
Hann Window
    │
    ▼
Windowed Frame
    │
    ▼
FFT
```

The choice of window affects spectral leakage and frequency-domain representation.

---

# Analysis Windows

Vibration processing is commonly performed on finite blocks of samples rather than an infinitely long signal.

For example:

```text
Continuous Signal

─────────────────────────────────────────────► Time
       │──────── Frame ────────│
                    │──────── Frame ────────│
```

Frames can be processed independently and, when appropriate, overlapping windows can be used.

The final frame length and overlap configuration are implementation parameters and may change during embedded development.

---

# Feature Extraction

The purpose of feature extraction is to convert a raw vibration waveform into a smaller set of measurable characteristics.

A simplified example is:

```text
                    Raw Signal
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
     Time Domain                Frequency Domain
          │                           │
    ┌─────┼─────┐                     │
    ▼     ▼     ▼                     ▼
   RMS   Peak  Kurtosis              FFT
    │     │     │                     │
    └─────┼─────┘                     │
          │                           │
          └───────────┬───────────────┘
                      ▼
                 Feature Set
```

These features can then be used by subsequent monitoring or health-assessment algorithms.

---

# Feature Interpretation

No single feature should automatically be interpreted as proof of a specific mechanical fault.

For example:

| Feature      | What it describes                              |
| ------------ | ---------------------------------------------- |
| RMS          | Overall signal magnitude                       |
| Peak         | Maximum observed amplitude                     |
| Crest Factor | Peak level relative to RMS                     |
| Kurtosis     | Statistical impulsiveness / distribution shape |
| FFT          | Frequency-domain content                       |

The useful information often comes from **changes over time and relationships between multiple features**, rather than from one measurement in isolation.

---

# Baseline Comparison

A practical monitoring system can establish a baseline for a machine under known operating conditions.

Conceptually:

```text
Baseline
   │
   ▼
Normal Operating Data
   │
   ▼
Feature Distribution
   │
   ▼
Current Measurement
   │
   ▼
Deviation Analysis
```

This approach allows the monitoring system to focus on changes in machine behavior rather than relying only on absolute thresholds.

Operating conditions such as speed, load, mounting location, and sensor orientation can affect measured vibration and should therefore be considered during validation.

---

# Relation to VectoraLab Health Score

VectoraLab's software Health Score is built on the idea of combining vibration-related information into a more compact condition indicator.

A simplified conceptual path is:

```text
Vibration Signal
       │
       ▼
Feature Extraction
       │
       ├── RMS
       ├── Peak
       ├── Crest Factor
       ├── Kurtosis
       └── Spectral Information
       │
       ▼
Feature Evaluation
       │
       ▼
Health Score
```

The Health Score is currently implemented in the software layer.

The embedded version of the complete processing and assessment pipeline is still under development.

---

# Current Implementation Status

| Processing Stage                                      | Status         |
| ----------------------------------------------------- | -------------- |
| Vibration signal generation / acquisition in software | Implemented    |
| Time-domain analysis                                  | Implemented    |
| RMS                                                   | Implemented    |
| Peak                                                  | Implemented    |
| Crest Factor                                          | Implemented    |
| Kurtosis                                              | Implemented    |
| FFT visualization                                     | Implemented    |
| Software Health Score                                 | Implemented    |
| Embedded signal processing                            | In development |
| Embedded TinyML                                       | In development |
| Real-machine validation                               | Not completed  |

---

# Summary

VectoraLab uses vibration analysis to transform raw machine measurements into interpretable signal characteristics.

The current software layer supports time-domain and frequency-domain analysis, while the embedded STM32H750 implementation is being developed to move selected processing closer to the monitored machine.

The overall objective is to create a connected pipeline from:

```text
Machine
   ↓
Vibration
   ↓
Sensor
   ↓
Embedded Processing
   ↓
Signal Features
   ↓
Health Assessment
   ↓
Software Monitoring
```

The processing pipeline will continue to be validated as the physical hardware prototype is completed.
