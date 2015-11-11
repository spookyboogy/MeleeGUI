#!/usr/bin/env python3
from cx_Freeze import setup, Executable
import os

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('readstat.py', targetName = 'MeleeGUI.exe')
]

imgdeps = [item for item in os.listdir() if item.endswith(".png")]


for item in os.listdir():
	if item.endswith('.png'):
		imgdeps
setup(name='MeleeGUI',
      version = '1.0',
      description = """Replica of Melee menus, CSS, and stats screen.
      				   Extensive features intended to be added. 
      				   This is only alpha.""",
      options = { 'build_exe' : {'include_files' : imgdeps}},
      executables = executables)
