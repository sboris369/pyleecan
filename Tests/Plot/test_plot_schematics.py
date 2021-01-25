import pytest
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM12 import SlotM12
from pyleecan.Classes.SlotM13 import SlotM13
from pyleecan.Classes.SlotM14 import SlotM14
from pyleecan.Classes.SlotM15 import SlotM15
from pyleecan.Classes.SlotM16 import SlotM16

from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.Classes.SlotW13 import SlotW13
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW15 import SlotW15
from pyleecan.Classes.SlotW16 import SlotW16
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW24 import SlotW24
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.Classes.SlotW27 import SlotW27
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.Classes.SlotW29 import SlotW29
from Tests import save_plot_path as save_path
from os.path import join, isdir, isfile
from os import makedirs, remove

SCHEMATICS_PATH = join(save_path, "Schematics")

if not isdir(SCHEMATICS_PATH):
    makedirs(SCHEMATICS_PATH)

slot_test = list()
slot_test.append(
    {"test_obj": SlotM10(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM11(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM12(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM13(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM14(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM15(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM16(), "type_add_active": 2,}
)

slot_test.append(
    {"test_obj": SlotW10(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW11(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW12(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW13(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW14(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW15(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW16(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW21(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW22(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW23(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW24(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW25(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW26(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW27(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW28(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW29(), "type_add_active": 1,}
)


class Test_plot_schematics(object):
    @pytest.mark.parametrize("test_dict", slot_test)
    def test_slot(self, test_dict):
        """Slot Schematics"""
        file_name = type(test_dict["test_obj"]).__name__ + ".png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        test_obj = test_dict["test_obj"]
        test_obj.plot_schematics(
            is_default=True,
            is_add_point_label=False,
            is_add_schematics=True,
            is_add_main_line=True,
            type_add_active=test_dict["type_add_active"],
            save_path=file_path,
            is_show_fig=False,
        )

    @pytest.mark.parametrize("test_dict", slot_test)
    def test_slot_point(self, test_dict):
        """Slot Schematics"""
        file_name = type(test_dict["test_obj"]).__name__ + "_point.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        test_obj = test_dict["test_obj"]
        test_obj.plot_schematics(
            is_default=True,
            is_add_point_label=True,
            is_add_schematics=False,
            is_add_main_line=True,
            type_add_active=test_dict["type_add_active"],
            save_path=file_path,
            is_show_fig=False,
        )
