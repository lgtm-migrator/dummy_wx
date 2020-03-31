"""
Script to generate wx/__init__.py
"""

import sys
del sys.path[0]

import pathlib

import wx
import wx.ribbon, wx.grid, wx.dataview, wx.richtext, wx.html
import wx.html2, wx.stc, wx.media, wx.propgrid, wx.xrc, wx.xml
import wx.py, wx.tools, wx.adv, wx.lib, wx.aui
from wx.lib import (
	anchors, busy, buttons, calendar, CDate,
	ClickableHtmlWindow, colourdb, colourselect,
	colourutils, combotreebox, delayedresult,
	dialogs, docview, dragscroller,	embeddedimage,
	eventStack,	eventwatcher, evtmgr, expando,
	fancytext, filebrowsebutton, foldmenu, gestures,
	gridmovers, imagebrowser, imageutils, infoframe,
	inspection, intctrl, itemspicker, langlistctrl,
	layoutf, msgpanel, multisash, newevent, nvdlg,
	pdfwin, platebtn, popupctl, printout, progressindicator,
	pydocview, rcsizer, resizewidget, scrolledpanel,
	sheet, sized_controls, softwareupdate, splitter,
	statbmp, stattext, throbber, ticker, ticker_xrc,
	utils, wordwrap, wxpTag,
	)
# Don't remove these imports: they are actually used


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
		# Special case for PyEventBinder; it needs to be a custom class as it might get called
		elif name == "PyEventBinder":
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


def parse_module(module_name):
	with open(f"wx/{module_name}.py", "w") as fp:
		parse(getattr(wx, module_name), fp)


def parse_lib_submodule(submodule_name):
	with open(f"wx/lib/{submodule_name}.py", "w") as fp:
		parse(globals()[submodule_name], fp)
		
		
with open("wx/__init__.py", "w") as fp:
	parse(wx, fp)
	
	fp.write("""

class PyEventBinder(object):
	def __init__(self, evtType, expectedIDs=0):
		pass
	
	def Bind(self, target, id1, id2, function):
		pass
	
	def Unbind(self, target, id1, id2, handler=None):
		return False
	
	def _getEvtType(self):
		return 0
	
	typeId = property(_getEvtType)


""")


if not pathlib.Path("./wx/lib").exists():
	pathlib.Path("./wx/lib").mkdir()

with open("wx/lib/__init__.py", "w") as fp:
	parse(wx.lib, fp)

for submodule in [
		"anchors", "busy", "buttons", "calendar", "CDate",
		"ClickableHtmlWindow", "colourdb", "colourselect",
		"colourutils", "combotreebox", "delayedresult",
		"dialogs", "docview", "dragscroller", "embeddedimage",
		"eventStack", "eventwatcher", "evtmgr", "expando",
		"fancytext", "filebrowsebutton", "foldmenu", "gestures",
		"gridmovers", "imagebrowser", "imageutils", "infoframe",
		"inspection", "intctrl", "itemspicker", "langlistctrl",
		"layoutf", "msgpanel", "multisash", "newevent", "nvdlg",
		"pdfwin", "platebtn", "popupctl", "printout",
		"progressindicator", "pydocview", "rcsizer", "resizewidget",
		"scrolledpanel", "sheet", "sized_controls", "softwareupdate",
		"splitter", "statbmp", "stattext", "throbber", "ticker",
		"ticker_xrc", "utils", "wordwrap", "wxpTag",
		]:
	parse_lib_submodule(submodule)


for module in [
		"grid",	"dataview",	"richtext",	"ribbon", "aui",
		"html", "html2", "stc", "media", "adv",
		"propgrid", "xrc", "xml", "py", "tools",
		]:
	parse_module(module)

