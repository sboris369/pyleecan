# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/HoleMag.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/HoleMag
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Hole import Hole

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.HoleMag.comp_mass_magnet_id import comp_mass_magnet_id
except ImportError as error:
    comp_mass_magnet_id = error

try:
    from ..Methods.Slot.HoleMag.comp_mass_magnets import comp_mass_magnets
except ImportError as error:
    comp_mass_magnets = error

try:
    from ..Methods.Slot.HoleMag.comp_surface_magnets import comp_surface_magnets
except ImportError as error:
    comp_surface_magnets = error

try:
    from ..Methods.Slot.HoleMag.comp_volume_magnets import comp_volume_magnets
except ImportError as error:
    comp_volume_magnets = error

try:
    from ..Methods.Slot.HoleMag.get_magnet_list import get_magnet_list
except ImportError as error:
    get_magnet_list = error

try:
    from ..Methods.Slot.HoleMag.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error


from ._check import InitUnKnowClassError
from .Material import Material


class HoleMag(Hole):
    """Hole with magnets for lamination (abstract)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.HoleMag.comp_mass_magnet_id
    if isinstance(comp_mass_magnet_id, ImportError):
        comp_mass_magnet_id = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleMag method comp_mass_magnet_id: "
                    + str(comp_mass_magnet_id)
                )
            )
        )
    else:
        comp_mass_magnet_id = comp_mass_magnet_id
    # cf Methods.Slot.HoleMag.comp_mass_magnets
    if isinstance(comp_mass_magnets, ImportError):
        comp_mass_magnets = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleMag method comp_mass_magnets: "
                    + str(comp_mass_magnets)
                )
            )
        )
    else:
        comp_mass_magnets = comp_mass_magnets
    # cf Methods.Slot.HoleMag.comp_surface_magnets
    if isinstance(comp_surface_magnets, ImportError):
        comp_surface_magnets = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleMag method comp_surface_magnets: "
                    + str(comp_surface_magnets)
                )
            )
        )
    else:
        comp_surface_magnets = comp_surface_magnets
    # cf Methods.Slot.HoleMag.comp_volume_magnets
    if isinstance(comp_volume_magnets, ImportError):
        comp_volume_magnets = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleMag method comp_volume_magnets: "
                    + str(comp_volume_magnets)
                )
            )
        )
    else:
        comp_volume_magnets = comp_volume_magnets
    # cf Methods.Slot.HoleMag.get_magnet_list
    if isinstance(get_magnet_list, ImportError):
        get_magnet_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleMag method get_magnet_list: " + str(get_magnet_list)
                )
            )
        )
    else:
        get_magnet_list = get_magnet_list
    # cf Methods.Slot.HoleMag.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleMag method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Zh=36, mat_void=-1, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Set the properties (value check and convertion are done in setter)
        # Call Hole init
        super(HoleMag, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        HoleMag_str = ""
        # Get the properties inherited from Hole
        HoleMag_str += super(HoleMag, self).__str__()
        return HoleMag_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(HoleMag, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Hole
        HoleMag_dict = super(HoleMag, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        HoleMag_dict["__class__"] = "HoleMag"
        return HoleMag_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Hole
        super(HoleMag, self)._set_None()
