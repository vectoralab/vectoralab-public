# Vibration Sample Data

This directory contains synthetic vibration datasets for testing and demonstrating the VectoraLab vibration-analysis workflow.

The datasets are generated at:

- Sampling rate: 5 kHz
- Duration: 1 second
- Number of samples: 5000 per dataset
- Machine speed: 1500 RPM
- Fundamental rotational frequency: 25 Hz

## Files

### normal.csv

Synthetic vibration signal representing a relatively stable operating condition.

The signal contains:

- 25 Hz fundamental rotational component
- 50 Hz second harmonic
- Low-level Gaussian noise

### noisy.csv

Synthetic vibration signal with increased broadband noise compared with the normal condition.

This dataset can be used to demonstrate the effect of increased vibration noise on time-domain features.

### impulse.csv

Synthetic vibration signal containing periodic transient impulses in addition to the rotational components.

This dataset is intended to demonstrate how impulsive behavior can affect vibration features such as:

- Peak
- Crest Factor
- Kurtosis

## CSV Format

Each file contains two columns:

```text
time_s,acceleration
