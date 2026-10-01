# Spectrogram and Short-Time Fourier Transform

## Overview

A vibration signal is not always stationary.

The frequency content of a machine can change over time because of changes in:

* Rotational speed
* Mechanical load
* Operating conditions
* Transient events
* Machine behavior

A conventional FFT provides frequency information for a selected signal window.

A **spectrogram** extends this idea by showing how the frequency content changes over time.

Conceptually:

```text
Vibration Signal
       │
       ▼
Divide into short frames
       │
       ▼
Window each frame
       │
       ▼
FFT for each frame
       │
       ▼
Spectral Magnitude
       │
       ▼
Spectrogram
```

---

# Short-Time Fourier Transform

The mathematical foundation of a spectrogram is the **Short-Time Fourier Transform (STFT)**.

Instead of applying one FFT to the complete signal, the signal is divided into shorter overlapping sections.

```text
Continuous Signal

──────────────────────────────────────────────► Time
      │──────── Frame 1 ────────│
              │──────── Frame 2 ────────│
                      │──────── Frame 3 ────────│
```

Each frame is processed independently.

The resulting spectra are then arranged along the time axis.

---

## STFT Concept

A simplified representation of the STFT is:

```text
STFT(x) = FFT{ x[n] · w[n-m] }
```

where:

* `x[n]` is the input signal
* `w[n-m]` is the window function
* `m` represents the position of the analysis window

The result contains information in both time and frequency.

---

# Spectrogram Representation

A spectrogram can be visualized as a two-dimensional representation:

```text
Frequency
   ▲
   │
   │       ▓▓
   │     ▓▓▓▓       ▓
   │   ▓▓▓▓▓▓     ▓▓▓
   │ ▓▓▓▓▓▓▓▓   ▓▓▓▓▓
   │
   └────────────────────────► Time
```

The two axes represent:

* **Horizontal axis:** Time
* **Vertical axis:** Frequency

The intensity or color at each point represents the magnitude or power of the signal at that time and frequency.

---

# Why Use a Spectrogram?

A normal FFT answers a question such as:

> What frequencies are present in this signal window?

A spectrogram can additionally answer:

> How does the frequency content change over time?

This distinction is useful for machine monitoring.

For example, a frequency component that appears only during a particular operating period may be easier to identify using a spectrogram than with a single FFT.

---

# Time-Frequency Analysis

A spectrogram provides a compromise between time resolution and frequency resolution.

The general relationship is:

```text
Shorter Analysis Window
        │
        ├── Better time resolution
        └── Lower frequency resolution


Longer Analysis Window
        │
        ├── Better frequency resolution
        └── Lower time resolution
```

This is the same fundamental trade-off encountered in FFT-based analysis.

---

# Window Length

The window length determines how much signal is analyzed at each STFT step.

For example:

```text
Sampling Rate = 5000 Hz
Window Length = 500 samples
```

The corresponding time duration is:

```text
T = N / Fs

T = 500 / 5000

T = 0.1 seconds
```

So each analysis frame represents approximately:

**100 ms**

of vibration data.

The actual window length used by VectoraLab can be adjusted according to the target application and embedded processing constraints.

---

# Window Overlap

Adjacent STFT windows can overlap.

For example, with 50% overlap:

```text
Frame 1
│──────────────────│
        Frame 2
        │──────────────────│
                Frame 3
                │──────────────────│
```

Overlap can provide more frequent spectral updates while maintaining a useful analysis window.

However, increased overlap also increases the amount of computation required.

---

# Spectral Magnitude

Each STFT frame produces a frequency spectrum.

The magnitude can be calculated from the real and imaginary FFT components:

```text
Magnitude[k] =
sqrt(Re[k]² + Im[k]²)
```

The magnitudes from successive frames can then be arranged into a two-dimensional matrix:

```text
          Time →
Frequency
   ↑
   │  M[0,0] M[0,1] M[0,2] M[0,3]
   │  M[1,0] M[1,1] M[1,2] M[1,3]
   │  M[2,0] M[2,1] M[2,2] M[2,3]
   │     ...
   └──────────────────────────────
```

This matrix is the basis for the spectrogram visualization.

---

# Example: Changing Rotational Behavior

Consider a machine whose rotational speed changes over time.

The vibration frequencies associated with rotational behavior may also change.

A conventional FFT over a long signal can combine these different operating conditions into one spectrum.

A spectrogram can show the evolution:

```text
Frequency
   ▲
   │
   │             ╱
   │           ╱
   │         ╱
   │       ╱
   │     ╱
   │   ╱
   └────────────────────────► Time
```

The diagonal pattern represents a frequency component changing over time.

This type of representation can be useful when analyzing transient or variable-speed operation.

---

# Spectrogram and Machine Monitoring

A spectrogram can help visualize:

* Changing frequency components
* Transient events
* Periodic behavior
* Harmonic structures
* Changes during startup
* Changes during shutdown
* Variable-speed operation
* Frequency bands that appear intermittently

It can therefore be a useful exploratory tool for understanding machine vibration.

---

# Spectrogram Is Not a Diagnosis

A spectrogram is a visualization and signal-analysis method.

It does **not**, by itself, prove that a particular mechanical fault exists.

A practical condition-monitoring system should consider additional information such as:

* Machine operating conditions
* Rotational speed
* Load
* Sensor position
* Baseline measurements
* Time-domain features
* Frequency-domain features
* Historical behavior

VectoraLab treats the spectrogram as one analysis tool rather than a standalone fault-diagnosis algorithm.

---

# Relation to VectoraLab

The VectoraLab software includes vibration-analysis functionality that can be used to explore signal behavior in both the time and frequency domains.

Spectrogram analysis fits naturally into the overall processing architecture:

```text
Raw Vibration
      │
      ├───────────────┐
      ▼               ▼
Time Domain      Frequency Domain
      │               │
      │              FFT
      │               │
      │               ▼
      │          Spectrogram
      │
      └──────────┬──────────┘
                 ▼
          Feature Analysis
                 │
                 ▼
           Health Assessment
```

The spectrogram can provide additional visual context when investigating how vibration characteristics evolve over time.

---

# Computational Considerations

An STFT requires multiple FFT operations because a separate FFT is performed for each analysis frame.

Compared with a single FFT, this increases computational requirements.

For an embedded implementation, the following parameters must be considered:

* Sampling rate
* FFT size
* Window length
* Window type
* Frame overlap
* Processing time
* Memory usage
* Data throughput

These parameters will be evaluated as the STM32H750 implementation progresses.

---

# Current Status

| Component                           | Status                          |
| ----------------------------------- | ------------------------------- |
| Spectrogram concept                 | Defined                         |
| Software time-frequency analysis    | Under development / exploration |
| STFT parameter selection            | Not finalized                   |
| STM32H750 STFT implementation       | Not completed                   |
| Real-machine spectrogram validation | Not completed                   |

---

# Summary

A spectrogram extends FFT-based analysis by adding the time dimension.

The basic process is:

```text
Signal
   ↓
Frame
   ↓
Window
   ↓
FFT
   ↓
Magnitude
   ↓
Repeat over time
   ↓
Spectrogram
```

For VectoraLab, this provides a way to explore how machine vibration changes over time and complements the existing time-domain and frequency-domain analysis.

The final STFT configuration will be determined during software and embedded-system development and validated using real vibration measurements.
