# -*- coding: utf-8 -*-

from ....Classes.LamSlotWind import LamSlotWind
from ....Methods.Machine import MachineCheckError


def check(self):
    """Check that the Machine object is correct

    Parameters
    ----------
    self : MachineWRSG
        A MachineWRSG object

    Returns
    -------
    None

    Raises
    _______
    M4C_WrongRotor
        The Rotor of a MachineWRSG must be a LamSlotWind
    M4C_WrongStator
        The Stator of a MachineWRSG must be a LamSlotWind
    M4C_PError
        The stator and the rotor winding must have the same value for p
    """

    super(type(self), self).check()

    if not isinstance(self.rotor, LamSlotWind):
        raise M4C_WrongRotor("The Rotor of a MachineWRSG must be a LamSlotWind")
    if not isinstance(self.stator, LamSlotWind):
        raise M4C_WrongStator("The Stator of a MachineWRSG must be a " "LamSlotWind")
    if self.rotor.winding.p != self.stator.winding.p:
        raise M4C_PError(
            "The stator and the rotor winding must have the " "same value for p"
        )


class M4C_WrongRotor(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    with
        Winding

    """

    pass


class M4C_WrongStator(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    with
        Winding

    """

    pass


class M4C_PError(MachineCheckError):
    """

    Parameters
    ----------

    Returns
    -------

    Raises
    ------
    different
        p value

    """

    pass
