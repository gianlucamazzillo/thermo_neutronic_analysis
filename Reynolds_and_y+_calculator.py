from dataclasses import dataclass
from math import sqrt
from CoolProp.CoolProp import PropsSI
@dataclass
class FluidProperties:
    density: float
    dynamic_viscosity: float
    kinematic_viscosity: float
    thermal_conductivity: float
    specific_heat: float
    prandtl_number: float

def get_fluid_properties(fluid: str, 
                         temperature: float, 
                         pressure: float,
                         ) -> FluidProperties: 

        if temperature <= 0:
            raise ValueError('Temperature must be greater than 0K.')

        if pressure <= 0:
            raise ValueError ('Pressure must be greater than 0Pa.')

        density = PropsSI('DMASS', 'T', temperature, 'P', pressure, fluid)

        dynamic_viscosity = PropsSI(
              'VISCOSITY', 'T', temperature, 'P', pressure, fluid
        )

        thermal_conductivity = PropsSI(
            'CONDUCTIVITY', 'T', temperature, 'P', pressure, fluid
        )

        specific_heat = PropsSI(
             'CPMASS', 'T', temperature, 'P', pressure, fluid
        )

        kinematic_viscosity = dynamic_viscosity / density

        prandtl_number = (
            specific_heat 
            * dynamic_viscosity 
            / thermal_conductivity
        )

        return FluidProperties(
              density = density,
              dynamic_viscosity = dynamic_viscosity,
              kinematic_viscosity = kinematic_viscosity,
              thermal_conductivity = thermal_conductivity,
              specific_heat = specific_heat,
              prandtl_number = prandtl_number,
        )

def calculate_reynolds_number (
      mean_velocity: float,
      equivalent_diameter: float,
      fluid_properties: FluidProperties,
      ) -> float:

     return (
          mean_velocity
          * equivalent_diameter
          * fluid_properties.density
          / fluid_properties.dynamic_viscosity
     )

def calculate_y_plus(
      wall_distance: float,
      wall_shear_stress: float,
      fluid_properties: FluidProperties,
) -> float:
     friction_velocity = sqrt(
          wall_shear_stress / fluid_properties.density
     )

     return (
          friction_velocity
          * wall_distance
          / fluid_properties.kinematic_viscosity
     )


#--------------------------------------TESTS------------------------------------

if __name__ == "__main__":
    water = get_fluid_properties(
        fluid="Water",
        temperature=298.15,
        pressure=101325,
    )

    reynolds = calculate_reynolds_number(
        mean_velocity=2.0,
        equivalent_diameter=0.05,
        fluid_properties=water,
    )

    y_plus = calculate_y_plus(
        wall_distance=0.0001,
        wall_shear_stress=5.0,
        fluid_properties=water,
    )

    print(water)
    print(f"Reynolds number: {reynolds:.5e}")
    print(f"y+: {y_plus:.5f}")