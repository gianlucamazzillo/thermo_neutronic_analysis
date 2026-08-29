from dataclasses import dataclass
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
        density = PropSI('DMASS', 'T', temperature, 'P', pressure, fluid)
        dynamic_viscosity = PropSI(
              'VISCOSITY', 'T', temperature, 'P', pressure, fluid
        )

        return FluidProperties(
              density = density,
              dynamic_viscosity = dynamic_viscosity,
              kinematic_viscosity = kinematic_viscosity,
              thermal_conductivity = PropSI(
                    'VISCOSITY', 'T', temperature, 'P', pressure, fluid
              )
              specific_heat = 

        )




