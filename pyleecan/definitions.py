# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath, isdir, isfile
import os
import platform
import shutil
from logging import getLogger
from json import load
from matplotlib.colors import ListedColormap
from matplotlib.cm import get_cmap, register_cmap
from numpy import load as np_load
from matplotlib import font_manager


ROOT_DIR = normpath(abspath(join(dirname(__file__), ".."))).replace("\\", "/")
MAIN_DIR = dirname(realpath(__file__)).replace("\\", "/")

PACKAGE_NAME = MAIN_DIR[len(ROOT_DIR) + 1 :]  # To allow to change pyleecan directory

# Pyleecan user folder
if platform.system() == "Windows":
    USER_DIR = join(os.environ["APPDATA"], PACKAGE_NAME)
    USER_DIR = USER_DIR.replace("\\", "/")
else:
    USER_DIR = os.environ["HOME"] + "/.local/share/" + PACKAGE_NAME

GEN_DIR = join(MAIN_DIR, "Generator").replace("\\", "/")
DOC_DIR = join(GEN_DIR, "ClassesRef").replace(
    "\\", "/"
)  # Absolute path to classes reference dir
INT_DIR = join(GEN_DIR, "Internal").replace(
    "\\", "/"
)  # Absolute path to  internal classes ref. dir

GUI_DIR = join(MAIN_DIR, "GUI").replace("\\", "/")
RES_PATH = join(GUI_DIR, "Resources").replace("\\", "/")  # Default Resouces folder name
RES_NAME = "pyleecan.qrc"  # Default Resouces file name

TEST_DIR = join(MAIN_DIR, "../Tests")

try:
    from .default_variable import default_config_dict
    from .Functions.init_environment import (
        edit_config_dict,
        read_config_dict,
        copy_folder,
    )
except ImportError:
    sys.path.insert(0, ROOT_DIR)
    exec("from pyleecan.default_variable import default_config_dict")
    exec(
        "from pyleecan.Functions.init_environment import edit_config_dict, read_config_dict, copy_folder"
    )

if isfile(join(USER_DIR, "config.json")):  # Load the config file if it exist
    with open(join(USER_DIR, "config.json"), "r") as config_file:
        config_dict = load(config_file)

    # Check that config_dict contains all the default_config_dict keys
    for key, val in default_config_dict.items():
        if key not in config_dict:
            config_dict[key] = val
            edit_config_dict(USER_DIR, config_dict)

else:  # Default values
    config_dict = default_config_dict

DATA_DIR = config_dict["DATA_DIR"]
MATLIB_DIR = config_dict["MATLIB_DIR"]

copy_folder("Data", "Data")
edit_config_dict(USER_DIR, config_dict)

# Load the color_dict
color_path = join(config_dict["DATA_DIR"], config_dict["COLOR_DICT_NAME"])
if not isfile(color_path):  # Default colors
    color_path = join(config_dict["DATA_DIR"], "pyleecan_color.json")
with open(color_path, "r") as color_file:
    config_dict["color_dict"] = load(color_file)

# Register the colormap
cmap_name = config_dict["color_dict"]["COLOR_MAP"]
cmap_path = join(config_dict["DATA_DIR"], cmap_name) + ".npy"
try:
    get_cmap(name=cmap_name)
except:
    if not isfile(cmap_path):  # Default colormap
        config_dict["color_dict"]["COLOR_MAP"] = "RdBu_r"
    else:
        cmap = np_load(cmap_path)
        cmp = ListedColormap(cmap)
        register_cmap(name=config_dict["color_dict"]["COLOR_MAP"], cmap=cmp)

# # Register fonts
# font_dirs = config_dict["DATA_DIR"]
# font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
# font_list = font_manager.createFontList(font_files)
# font_manager.fontManager.ttflist.extend(font_list)
