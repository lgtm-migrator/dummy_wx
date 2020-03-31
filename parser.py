"""
Script to generate wx/__init__.py
"""

import sys
del sys.path[0]

import pathlib

def parse(module, fp):
	fp.write("""# Based on wxPython
# Copyright: (c) 2018 by Total Control Software
# License:   wxWindows License


def dummy_function(*args, **kwargs):
	return 0


""")
	
	for obj in dir(module):
		name = obj
		
		obj_type = str(type(getattr(module, obj)))
		
		val = None
		
		# ignore magic methods
		if name.startswith("__") and name.endswith("__"):
			continue
		elif name.startswith("IMAGE_OPTION_") and obj_type == "<class 'str'>":
			val = f"'{(getattr(wx, obj))}'"
		elif obj_type == "<class 'bytes'>":
			val = "bytes()"
		elif obj_type == "<class 'str'>":
			val = "''"
		elif obj_type == "<class 'int'>":
			val = "0"
		elif obj_type == "<class 'float'>":
			val = "0.0"
		elif obj_type == "<class 'list'>":
			val = "[]"
		elif obj_type == "<class 'tuple'>":
			val = "tuple()"
		elif obj_type == "<class 'NoneType'>":
			val = "None"
		elif obj_type == "<class 'dict'>":
			val = "dict()"
		
		elif obj_type in {"<class 'function'>", "<class 'builtin_function_or_method'>"}:
			val = "dummy_function"
		elif obj_type.startswith("<class 'sip"):
			val = "object"
		elif obj_type.startswith("<class 'wx"):
			val = "object"
		elif obj_type == "<class 'type'>":
			val = "object"
		elif obj_type == "<class 'PyCapsule'>":
			val = "object"
		
		else:
			print(name, obj_type)
		
		if val:
			fp.write(f"{name} = {val}\n")

import wx

with open("wx/__init__.py", "w") as fp:
	parse(wx, fp)

import wx.html2

with open("wx/html2.py", "w") as fp:
	parse(wx.html2, fp)

import wx.stc

with open("wx/stc.py", "w") as fp:
	parse(wx.stc, fp)
	
if not pathlib.Path("./wx/lib").exists():
	pathlib.Path("./wx/lib").mkdir()

import wx.lib

with open("wx/lib/__init__.py", "w") as fp:
	parse(wx.lib, fp)

import wx.lib.embeddedimage

with open("wx/lib/embeddedimage.py", "w") as fp:
	parse(wx.lib.embeddedimage, fp)
	
import wx.lib.filebrowsebutton

with open("wx/lib/filebrowsebutton.py", "w") as fp:
	parse(wx.lib.filebrowsebutton, fp)

import wx.adv

if not pathlib.Path("./wx/adv").exists():
	pathlib.Path("./wx/adv").mkdir()
	
with open("wx/adv/__init__.py", "w") as fp:
	parse(wx.adv, fp)

import wx.grid

if not pathlib.Path("./wx/grid").exists():
	pathlib.Path("./wx/grid").mkdir()
	
with open("wx/grid/__init__.py", "w") as fp:
	parse(wx.grid, fp)
	
import wx.dataview

if not pathlib.Path("./wx/dataview").exists():
	pathlib.Path("./wx/dataview").mkdir()
	
with open("wx/dataview/__init__.py", "w") as fp:
	parse(wx.dataview, fp)
	
import wx.richtext

if not pathlib.Path("./wx/richtext").exists():
	pathlib.Path("./wx/richtext").mkdir()
	
with open("wx/richtext/__init__.py", "w") as fp:
	parse(wx.richtext, fp)

import wx.ribbon

if not pathlib.Path("./wx/ribbon").exists():
	pathlib.Path("./wx/ribbon").mkdir()
	
with open("wx/ribbon/__init__.py", "w") as fp:
	parse(wx.ribbon, fp)

