# quantum-energy-calculator
A Python tool to calculate photon energy levels using Planck's constant for quantum physics simulations.
# ⚛️ Quantum Energy Calculator

A lightweight Python script designed for Quantum Physics and Astrophysics simulations. This tool calculates the energy ($E$) of a photon based on its frequency ($f$) using Planck's relation equation.

## 📐 Physics Logic
The photon energy is calculated using the Planck equation:

$$E = h \cdot f$$

Where:
- **$E$**: Energy of the photon in Joules ($J$)
- **$h$**: Planck's constant ($6.626 \times 10^{-34} \text{ J}\cdot\text{s}$)
- **$f$**: Electromagnetic wave frequency in Hertz ($\text{Hz}$)

## 🚀 Features
- **Exception Handling:** Robust input validation using `try/except` blocks to handle non-numeric inputs gracefully.
- **Data Validation:** Ensures physical constraints (frequency must be a positive float).
- **Modular Design:** Divided into functional blocks (`main()` and `calculate_energy()`) following PEP 8 guidelines.

## 🛠️ Usage

1. Run the script via terminal:
   ```bash
   python energy.py
