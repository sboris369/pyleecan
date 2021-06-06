# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox, QWidget

from .....GUI.Dialog.DMachineSetup.SMachineType.Gen_SMachineType import Gen_SMachineType
from .....Classes.Winding import Winding
from .....Classes.MachineIPMSM import MachineIPMSM
from .....Classes.MachineSIPMSM import MachineSIPMSM
from .....Classes.MachineSyRM import MachineSyRM
from .....definitions import PACKAGE_NAME


class SMachineType(Gen_SMachineType, QWidget):
    """First Step to setup the Machine Type"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for the DMachineSetup nav
    step_name = "Machine Type"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SMachineType
            A SMachineType widget
        machine : Machine
            current machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.material_dict = material_dict
        self.is_stator = is_stator

        # Dynamic import to avoid import loop
        module = __import__(
            PACKAGE_NAME + ".GUI.Dialog.DMachineSetup", fromlist=["DMachineSetup"]
        )
        self.mach_list = getattr(module, "mach_list")
        self.mach_index = getattr(module, "mach_index")

        # Fill the combobox
        self.c_type.clear()
        self.c_type.addItems(
            [self.mach_dict["name"] for self.mach_dict in self.mach_list]
        )
        # Update the GUI to the current machine type
        index = self.mach_index.index(type(self.machine))
        self.mach_dict = self.mach_list[index]
        self.txt_type_machine.setText(self.mach_dict["txt"])
        self.img_type_machine.setPixmap(QPixmap(self.mach_dict["img"]))
        self.c_type.setCurrentIndex(index)

        # For the WRSG machine type, we hide the pole pair label
        # and spin box for it is not used during machine type selection.
        # The label and spinbox are set back to visible if you change the
        # machine type to something other then WRSG.
        if machine.type_machine == 12:
            self.in_p.setVisible(False)
            self.si_p.setVisible(False)
        elif machine.stator.get_pole_pair_number() is not None:
            self.si_p.setValue(machine.stator.winding.p)
        else:
            self.si_p.clear()  # Empty spinbox

        # Set default values
        self.machine.stator.is_stator = True
        self.machine.rotor.is_stator = False

        if machine.rotor.is_internal is None:
            self.machine.rotor.is_internal = True
            self.machine.stator.is_internal = False
            self.is_inner_rotor.setCheckState(Qt.Checked)
        elif machine.rotor.is_internal:
            self.is_inner_rotor.setCheckState(Qt.Checked)
        else:
            self.is_inner_rotor.setCheckState(Qt.Unchecked)

        # WRSM and WRSG can only have inner rotor
        if self.machine.type_machine == 9 or 12:
            self.is_inner_rotor.setEnabled(False)
        else:
            self.is_inner_rotor.setEnabled(True)

        if machine.name not in [None, ""]:
            self.le_name.setText(machine.name)

        # Connect the slot/signal
        self.si_p.editingFinished.connect(self.set_p)
        self.is_inner_rotor.toggled.connect(self.set_inner_rotor)
        self.le_name.editingFinished.connect(self.s_set_name)
        self.c_type.currentIndexChanged.connect(self.set_machine_type)

    def s_set_name(self):
        """Set the name of the machine

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        """
        self.machine.name = str(self.le_name.text())
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_p(self):
        """Signal to update the value of p according to the spinbox

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        """
        if self.machine.type_machine == 12:
            # For WRSG Machine Type: Winding and Pole pairs cannot be set here.
            # Pole pairs are dependent on Rotor speed and output Frequency.
            # The choice of Stator Winding type can be either Concentrated or
            # distributed windings. Also, distributed windings can be Integral or
            # fractional slot windings. So these values are set latter.
            # NOTE: since nothing gets changed self.saveNeeded.emit() is not called.
            return

        value = self.si_p.value()
        if self.machine.stator.winding is None:
            self.machine.stator.winding = Winding()
            self.machine.stator.winding._set_None()
        self.machine.set_pole_pair_number(value)

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_inner_rotor(self, is_checked):
        """Signal to update the value of is_internal according to the widget

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        is_checked : bool
            State of is_internal
        """

        self.machine.stator.is_internal = not is_checked
        self.machine.rotor.is_internal = is_checked
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_machine_type(self, index):
        """Change the machine type according to the combobox

        Parameters
        ----------
        self : SMachineType
            A SMachineType object
        index : int
            Selected machine type index
        """
        p = self.machine.stator.get_pole_pair_number()
        # Get the correct machine class
        mach = self.mach_list[index]["init_machine"]
        self.machine = type(mach)(init_dict=mach.as_dict())
        if p is not None:
            self.si_p.setValue(p)
            self.set_p()
        # Update the GUI with the new machine
        self.parent().machine = self.machine
        self.parent().update_nav(next_step=0)
        if self.parent() is not None:
            self.parent().main_layout.removeWidget(self)

    @staticmethod
    def check(machine):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        machine : Machine
            Machine to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        # The WRSG Machine Type set Winding and Pole pairs later.
        if machine.type_machine == 12:
            return
        try:
            if machine.stator.winding is None:
                return "Missing stator winding"
            if machine.stator.get_pole_pair_number() in [None, 0]:
                return "p must be >0 !"
        except Exception as e:
            return str(e)
