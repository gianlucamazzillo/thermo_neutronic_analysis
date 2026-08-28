"""Analytical models for steady-state radial heat conduction."""

import numpy as np


def calculate_fuel_temperature(
    radius: np.ndarray,
    fuel_radius: float,
    surface_temperature: float,
    thermal_conductivity: float,
    volumetric_heat_generation: float,
) -> np.ndarray:
    """Calculate the radial temperature profile of a cylindrical fuel pin.

    Assumes steady-state radial conduction, uniform volumetric heat
    generation, constant thermal conductivity, and prescribed surface
    temperature.

    All inputs must use SI units.
    """
    radii = np.asarray(radius, dtype=float)

    if fuel_radius <= 0:
        raise ValueError("fuel_radius must be greater than zero.")

    if thermal_conductivity <= 0:
        raise ValueError("thermal_conductivity must be greater than zero.")

    if volumetric_heat_generation < 0:
        raise ValueError(
            "volumetric_heat_generation cannot be negative."
        )

    if np.any(radii < 0) or np.any(radii > fuel_radius):
        raise ValueError(
            "All radius values must be between zero and fuel_radius."
        )

    return surface_temperature + (
        volumetric_heat_generation
        * (fuel_radius**2 - radii**2)
        / (4 * thermal_conductivity)
    )