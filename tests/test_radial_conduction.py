"""Validation tests for radial-conduction models."""

import numpy as np
import pytest

from src.thermo_neutronic_analysis.radial_conduction import (
    calculate_fuel_temperature,
)


def test_surface_temperature_matches_boundary_condition():
    temperatures = calculate_fuel_temperature(
        radius=np.array([0.004]),
        fuel_radius=0.004,
        surface_temperature=600.0,
        thermal_conductivity=3.0,
        volumetric_heat_generation=2.0e8,
    )

    assert temperatures[0] == pytest.approx(600.0)


def test_centerline_temperature_matches_analytical_solution():
    temperatures = calculate_fuel_temperature(
        radius=np.array([0.0]),
        fuel_radius=0.004,
        surface_temperature=600.0,
        thermal_conductivity=3.0,
        volumetric_heat_generation=2.0e8,
    )

    expected_temperature = 600.0 + (
        2.0e8 * 0.004**2 / (4 * 3.0)
    )

    assert temperatures[0] == pytest.approx(expected_temperature)


def test_temperature_decreases_toward_surface():
    radii = np.linspace(0.0, 0.004, 20)

    temperatures = calculate_fuel_temperature(
        radius=radii,
        fuel_radius=0.004,
        surface_temperature=600.0,
        thermal_conductivity=3.0,
        volumetric_heat_generation=2.0e8,
    )

    assert np.all(np.diff(temperatures) <= 0)


def test_rejects_nonpositive_thermal_conductivity():
    with pytest.raises(ValueError):
        calculate_fuel_temperature(
            radius=np.array([0.0]),
            fuel_radius=0.004,
            surface_temperature=600.0,
            thermal_conductivity=0.0,
            volumetric_heat_generation=2.0e8,
        )


def test_rejects_radius_outside_fuel():
    with pytest.raises(ValueError):
        calculate_fuel_temperature(
            radius=np.array([0.005]),
            fuel_radius=0.004,
            surface_temperature=600.0,
            thermal_conductivity=3.0,
            volumetric_heat_generation=2.0e8,
        )