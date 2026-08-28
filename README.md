# Thermo-Neutronic Analysis

A Python project for the development and validation of reduced-order thermal
models for compact nuclear systems.

## Current scope

The first development stage focuses on steady-state radial heat conduction in
a cylindrical fuel region with uniform volumetric heat generation.

The initial model assumes:

- one-dimensional radial conduction;
- steady-state conditions;
- constant thermal conductivity;
- uniform volumetric heat generation;
- prescribed fuel surface temperature.

These assumptions provide an analytical benchmark for validating later
numerical models.

## Development roadmap

1. Analytical radial temperature distribution
2. Physical and numerical validation tests
3. Parametric studies with NumPy and Matplotlib
4. Fuel gap and cladding thermal resistances
5. Temperature-dependent material properties
6. Finite-difference thermal solver
7. Neutronic power-distribution coupling

## Project structure

- `src/thermo_neutronic_analysis/`: physical models
- `examples/`: executable analysis cases
- `tests/`: validation tests