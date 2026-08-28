'''Analytical models for steady-state radial heat conduction.'''
import numpy as np

def calculate_fuel_temperature(
        radius: np.array,
        fuel_radius: float,
        surface_temperature: float,
        thermal_conductivity: float,
        volumetric_heat_generation: float,
) -> np.ndarray:
    ''''''
    