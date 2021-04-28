# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/WindingUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/WindingUD
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Winding import Winding

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.WindingUD.comp_connection_mat import comp_connection_mat
except ImportError as error:
    comp_connection_mat = error

try:
    from ..Methods.Machine.WindingUD.init_as_CW1L import init_as_CW1L
except ImportError as error:
    init_as_CW1L = error

try:
    from ..Methods.Machine.WindingUD.init_as_CW2LR import init_as_CW2LR
except ImportError as error:
    init_as_CW2LR = error

try:
    from ..Methods.Machine.WindingUD.init_as_CW2LT import init_as_CW2LT
except ImportError as error:
    init_as_CW2LT = error

try:
    from ..Methods.Machine.WindingUD.init_as_DWL import init_as_DWL
except ImportError as error:
    init_as_DWL = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Conductor import Conductor


class WindingUD(Winding):
    """User defined winding"""

    VERSION = 1
    NAME = "User defined"

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.WindingUD.comp_connection_mat
    if isinstance(comp_connection_mat, ImportError):
        comp_connection_mat = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method comp_connection_mat: "
                    + str(comp_connection_mat)
                )
            )
        )
    else:
        comp_connection_mat = comp_connection_mat
    # cf Methods.Machine.WindingUD.init_as_CW1L
    if isinstance(init_as_CW1L, ImportError):
        init_as_CW1L = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method init_as_CW1L: " + str(init_as_CW1L)
                )
            )
        )
    else:
        init_as_CW1L = init_as_CW1L
    # cf Methods.Machine.WindingUD.init_as_CW2LR
    if isinstance(init_as_CW2LR, ImportError):
        init_as_CW2LR = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method init_as_CW2LR: " + str(init_as_CW2LR)
                )
            )
        )
    else:
        init_as_CW2LR = init_as_CW2LR
    # cf Methods.Machine.WindingUD.init_as_CW2LT
    if isinstance(init_as_CW2LT, ImportError):
        init_as_CW2LT = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method init_as_CW2LT: " + str(init_as_CW2LT)
                )
            )
        )
    else:
        init_as_CW2LT = init_as_CW2LT
    # cf Methods.Machine.WindingUD.init_as_DWL
    if isinstance(init_as_DWL, ImportError):
        init_as_DWL = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method init_as_DWL: " + str(init_as_DWL)
                )
            )
        )
    else:
        init_as_DWL = init_as_DWL
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_reverse_wind=False,
        Nslot_shift_wind=0,
        qs=3,
        Ntcoil=7,
        Npcp=2,
        type_connection=0,
        p=3,
        Lewout=0.015,
        conductor=-1,
        coil_pitch=0,
        wind_mat=None,
        Nlayer=1,
        per_a=None,
        is_aper_a=None,
        init_dict=None,
        init_str=None,
    ):
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
            if "is_reverse_wind" in list(init_dict.keys()):
                is_reverse_wind = init_dict["is_reverse_wind"]
            if "Nslot_shift_wind" in list(init_dict.keys()):
                Nslot_shift_wind = init_dict["Nslot_shift_wind"]
            if "qs" in list(init_dict.keys()):
                qs = init_dict["qs"]
            if "Ntcoil" in list(init_dict.keys()):
                Ntcoil = init_dict["Ntcoil"]
            if "Npcp" in list(init_dict.keys()):
                Npcp = init_dict["Npcp"]
            if "type_connection" in list(init_dict.keys()):
                type_connection = init_dict["type_connection"]
            if "p" in list(init_dict.keys()):
                p = init_dict["p"]
            if "Lewout" in list(init_dict.keys()):
                Lewout = init_dict["Lewout"]
            if "conductor" in list(init_dict.keys()):
                conductor = init_dict["conductor"]
            if "coil_pitch" in list(init_dict.keys()):
                coil_pitch = init_dict["coil_pitch"]
            if "wind_mat" in list(init_dict.keys()):
                wind_mat = init_dict["wind_mat"]
            if "Nlayer" in list(init_dict.keys()):
                Nlayer = init_dict["Nlayer"]
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "is_aper_a" in list(init_dict.keys()):
                is_aper_a = init_dict["is_aper_a"]
        # Set the properties (value check and convertion are done in setter)
        # Call Winding init
        super(WindingUD, self).__init__(
            is_reverse_wind=is_reverse_wind,
            Nslot_shift_wind=Nslot_shift_wind,
            qs=qs,
            Ntcoil=Ntcoil,
            Npcp=Npcp,
            type_connection=type_connection,
            p=p,
            Lewout=Lewout,
            conductor=conductor,
            coil_pitch=coil_pitch,
            wind_mat=wind_mat,
            Nlayer=Nlayer,
            per_a=per_a,
            is_aper_a=is_aper_a,
        )
        # The class is frozen (in Winding init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        WindingUD_str = ""
        # Get the properties inherited from Winding
        WindingUD_str += super(WindingUD, self).__str__()
        return WindingUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Winding
        if not super(WindingUD, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self"):
        """Compare two objects and return list of differences"""

        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Winding
        diff_list.extend(super(WindingUD, self).compare(other, name=name))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Winding
        S += super(WindingUD, self).__sizeof__()
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Winding
        WindingUD_dict = super(WindingUD, self).as_dict(**kwargs)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        WindingUD_dict["__class__"] = "WindingUD"
        return WindingUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Winding
        super(WindingUD, self)._set_None()
