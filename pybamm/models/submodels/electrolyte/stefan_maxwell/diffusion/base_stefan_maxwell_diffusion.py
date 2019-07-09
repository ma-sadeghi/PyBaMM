#
# Base class for electrolyte diffusion employing stefan-maxwell
#
from ...base_electrolyte_diffusion import BaseElectrolyteDiffusion
import pybamm


class BaseModel(BaseElectrolyteDiffusion):
    """Base class for conservation of mass in the electrolyte employing the
    Stefan-Maxwell constitutive equations.

    Parameters
    ----------
    param : parameter class
        The parameters to use for this submodel


    **Extends:** :class:`pybamm.electrolyte.BaseElectrolyteDiffusion`
    """

    def __init__(self, param):
        super().__init__(param)

    def set_boundary_conditions(self, variables):

        c_e = variables["Electrolyte concentration"]

        self.boundary_conditions = {
            c_e: {
                "left": (pybamm.Scalar(0), "Neumann"),
                "right": (pybamm.Scalar(0), "Neumann"),
            }
        }
