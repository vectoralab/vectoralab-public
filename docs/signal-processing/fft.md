# FFT-Based Vibration Analysis

## Overview

The Fast Fourier Transform (FFT) is one of the main tools used in VectoraLab for frequency-domain analysis of vibration signals.

A vibration signal is initially represented as a sequence of measurements over time.

The FFT transforms this representation into a frequency-domain representation, making it possible to examine how signal content is distributed across different frequencies.

```text
Time-Domain Signal
        │
        ▼
    Preprocessing
        │
        ▼
      Window
        │
        ▼
       FFT
        │
        ▼
Frequency Spectrum
```

---

## Sampling Rate

The current VectoraLab design uses a sampling rate of:

```text
Fs = 5000 Hz
```

This means that 5000 samples are acquired every second.

The sampling interval is:

```text
Ts = 1 / Fs

Ts = 1 / 5000

Ts = 0.0002 s
```

or:

```text
Ts = 0.2 ms
```

---

## Nyquist Frequency

For a sampled signal, the Nyquist frequency is half of the sampling rate.

```text
fNyquist = Fs / 2

fNyquist = 5000 / 2

fNyquist = 2500 Hz
```

Therefore, the current 5 kHz sampling design provides a theoretical frequency range up to approximately:

**2.5 kHz**

for conventional baseband sampling.

In practical systems, anti-aliasing considerations and sensor characteristics must also be taken into account.

---

## FFT Input

The FFT operates on a finite block of samples.

For a signal containing `N` samples:

```text
x[0], x[1], x[2], ..., x[N-1]
```

the FFT produces a set of complex frequency-domain coefficients.

Each coefficient contains:

* Real component
* Imaginary component

These components can be used to calculate the magnitude and phase of each frequency bin.

---

## DFT Concept

The Discrete Fourier Transform (DFT) can be written as:

```text
X[k] = Σ x[n] · e^(-j 2πkn/N)
```

where:

* `x[n]` is the input signal
* `X[k]` is the frequency-domain coefficient
* `N` is the number of samples
* `k` is the frequency-bin index
* `j` is the imaginary unit

The FFT is an efficient algorithm for calculating the DFT.

---

## Frequency Resolution

The frequency resolution of an FFT depends on the sampling rate and the number of samples.

The frequency-bin spacing is:

```text
Δf = Fs / N
```

For example, with:

```text
Fs = 5000 Hz
N = 1000 samples
```

the frequency resolution would be:

```text
Δf = 5000 / 1000

Δf = 5 Hz
```

Therefore, increasing the FFT frame length improves frequency resolution, but also increases the amount of data that must be collected before a complete FFT frame is available.

---

## Frequency Bins

The frequency associated with a bin `k` can be approximated by:

```text
f[k] = k × Fs / N
```

For example:

```text
k = 0
```

corresponds to the DC component.

Higher values of `k` correspond to higher frequencies.

For a real-valued signal, only the positive-frequency portion is normally required for many vibration-analysis applications.

---

## FFT Magnitude

The FFT output is complex.

If:

```text
X[k] = Re[k] + j Im[k]
```

the magnitude can be calculated as:

```text
|X[k]| = sqrt(Re[k]² + Im[k]²)
```

A magnitude spectrum can therefore be represented as:

```text
Amplitude
   │
   │             │
   │             │
   │       │     │
   │       │     │
───┴───────┴─────┴──────────► Frequency
           f1    f2
```

The peaks in the spectrum can reveal dominant periodic components in the vibration signal.

---

## Windowing

A finite signal frame does not necessarily contain an integer number of cycles of the underlying periodic components.

Directly applying an FFT to such a frame can introduce spectral leakage.

A window function can be applied before the FFT.

One commonly used window is the **Hann window**.

Conceptually:

```text
Raw Signal
    │
    ▼
Apply Hann Window
    │
    ▼
Windowed Signal
    │
    ▼
FFT
```

The window changes the trade-off between spectral leakage and frequency resolution.

---

## Spectral Leakage

Spectral leakage occurs when signal energy spreads into neighboring frequency bins.

For example, a theoretical single-frequency component may not appear as one perfectly isolated FFT bin.

Instead, its energy can spread around the actual frequency.

```text
Idealized
Amplitude
   │
   │          │
   │          │
───┴──────────┴──────────────► Frequency


With Leakage
Amplitude
   │
   │        ▂▄█▄▂
   │      ▂███████▂
───┴─────────────────────────► Frequency
```

Windowing can reduce leakage, although it also changes the spectral shape and amplitude characteristics.

---

## Time-Frequency Trade-Off

FFT analysis involves a trade-off between time resolution and frequency resolution.

A longer frame provides better frequency resolution:

```text
Larger N
   ↓
Smaller Δf
   ↓
Better frequency resolution
```

But a longer frame also requires more time to collect the samples:

```text
Longer frame
   ↓
More observation time
   ↓
Lower temporal responsiveness
```

Conversely:

```text
Smaller N
   ↓
Larger Δf
   ↓
Lower frequency resolution
   ↓
Shorter observation window
```

This trade-off is important when designing an embedded vibration-monitoring system.

---

## Example at 5 kHz

Consider an example configuration:

```text
Sampling Rate = 5000 Hz
FFT Size      = 1024 samples
```

The frequency resolution is:

```text
Δf = 5000 / 1024

Δf ≈ 4.88 Hz
```

The observation time of the frame is:

```text
T = N / Fs

T = 1024 / 5000

T ≈ 0.2048 seconds
```

So approximately 204.8 ms of signal data are required for one 1024-sample frame.

This example is illustrative; the final FFT frame size used in the embedded implementation will be determined during development and validation.

---

## Vibration Analysis Example

Suppose a rotating machine produces a periodic vibration component around a particular frequency.

In the time domain, the signal may appear as:

```text
Amplitude
   │
   │   ╭──╮    ╭──╮    ╭──╮
   │  ╱    ╲  ╱    ╲  ╱    ╲
───┴──────────────────────────► Time
```

After FFT processing, the periodic component can appear as a spectral peak:

```text
Amplitude
   │
   │             █
   │             █
   │             █
───┴─────────────┴────────────► Frequency
                  f
```

Changes in the spectral content over time can provide useful information for condition monitoring.

---

## FFT in VectoraLab

The current software layer uses FFT-based visualization as part of vibration analysis.

The software can:

* Generate or receive vibration signals
* Transform signals into the frequency domain
* Visualize spectral content
* Calculate related signal characteristics
* Support experimentation with vibration-analysis parameters

The embedded FFT implementation for the STM32H750 is part of the ongoing hardware and signal-processing development.

---

## FFT and Health Assessment

FFT output can provide frequency-domain information that contributes to the overall feature set used for machine-condition assessment.

A simplified pipeline is:

```text
Vibration Signal
       │
       ▼
     Window
       │
       ▼
      FFT
       │
       ▼
Magnitude Spectrum
       │
       ▼
Spectral Features
       │
       ├───────────────┐
       │               │
       ▼               ▼
Time Features     Frequency Features
       │               │
       └───────┬───────┘
               ▼
        Health Assessment
```

The FFT itself is not a diagnosis algorithm. It is a signal-processing tool that provides information which can be combined with other features and operating context.

---

## Practical Considerations

Real vibration measurements can be affected by:

* Sensor mounting
* Mechanical coupling
* Sampling jitter
* Electrical noise
* Aliasing
* Operating speed
* Machine load
* Window selection
* FFT frame length
* Frequency resolution

These factors need to be considered when moving from software simulations to measurements from real machinery.

---

## Current Status

| Component                            | Status         |
| ------------------------------------ | -------------- |
| Software FFT analysis                | Implemented    |
| FFT visualization                    | Implemented    |
| Time-domain analysis                 | Implemented    |
| Frequency-domain feature exploration | Implemented    |
| STM32H750 embedded FFT               | In development |
| Final embedded FFT configuration     | Not finalized  |
| Real-machine validation              | Not completed  |

---

## Summary

FFT provides VectoraLab with a frequency-domain view of machine vibration.

With the current 5 kHz sampling design:

```text
Sampling Rate  = 5000 Hz
Nyquist         = 2500 Hz
```

The final FFT configuration will be selected based on the requirements of the embedded system, target machinery, available processing resources, and results from real-machine testing.
