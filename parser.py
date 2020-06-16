"""
Script to generate wx/__init__.py
"""

import sys
del sys.path[0]

import pathlib

import wx
import wx.ribbon, wx.grid, wx.dataview, wx.richtext, wx.html
import wx.html2, wx.stc, wx.media, wx.propgrid, wx.xrc, wx.xml
import wx.adv, wx.aui

import wx.tools
import wx.tools.dbg, wx.tools.helpviewer, wx.tools.img2img, wx.tools.img2png
import wx.tools.img2py, wx.tools.img2xpm, wx.tools.pywxrc, wx.tools.wxget

import wx.py
import wx.py.buffer, wx.py.crust, wx.py.crustslices, wx.py.dispatcher
import wx.py.document, wx.py.editor, wx.py.editwindow, wx.py.filling
import wx.py.frame, wx.py.images, wx.py.interpreter, wx.py.introspect
import wx.py.magic, wx.py.parse, wx.py.path, wx.py.pseudo, wx.py.PyAlaCarte
import wx.py.PyAlaMode, wx.py.PyAlaModeTest, wx.py.PyCrust, wx.py.PyFilling
import wx.py.PyShell, wx.py.PySlices, wx.py.PySlicesShell, wx.py.PyWrap
import wx.py.shell, wx.py.sliceshell, wx.py.version

import wx.lib
import wx.lib.anchors, wx.lib.busy, wx.lib.buttons, wx.lib.calendar
import wx.lib.ClickableHtmlWindow, wx.lib.colourdb, wx.lib.colourselect
import wx.lib.colourutils, wx.lib.combotreebox, wx.lib.delayedresult
import wx.lib.dialogs, wx.lib.docview, wx.lib.dragscroller, wx.lib.splitter
import wx.lib.eventStack, wx.lib.eventwatcher, wx.lib.evtmgr, wx.lib.CDate
import wx.lib.fancytext, wx.lib.filebrowsebutton, wx.lib.foldmenu
import wx.lib.gridmovers, wx.lib.imagebrowser, wx.lib.imageutils, wx.lib.nvdlg
import wx.lib.inspection, wx.lib.intctrl, wx.lib.itemspicker, wx.lib.ticker_xrc
import wx.lib.layoutf, wx.lib.msgpanel, wx.lib.multisash, wx.lib.newevent
import wx.lib.pdfwin, wx.lib.platebtn, wx.lib.popupctl, wx.lib.printout
import wx.lib.pydocview, wx.lib.rcsizer, wx.lib.resizewidget
import wx.lib.sheet, wx.lib.sized_controls, wx.lib.softwareupdate
import wx.lib.statbmp, wx.lib.stattext, wx.lib.throbber, wx.lib.ticker
import wx.lib.utils, wx.lib.wordwrap, wx.lib.wxpTag, wx.lib.progressindicator
import wx.lib.langlistctrl, wx.lib.embeddedimage, wx.lib.expando
import wx.lib.gestures, wx.lib.infoframe, wx.lib.scrolledpanel, wx.lib.wxcairo

import wx.lib.agw
import wx.lib.analogclock
import wx.lib.art
import wx.lib.colourchooser
import wx.lib.editor
import wx.lib.floatcanvas
import wx.lib.gizmos
import wx.lib.masked
import wx.lib.mixins
import wx.lib.ogl
import wx.lib.plot
import wx.lib.pubsub


def parse(module, fp):
	fp.write("""# Based on wxPython
# Copyright: (c) 2018 by Total Control Software
# License:   wxWindows License


def dummy_function(*args, **kwargs):
	return 0


""")
	
	for obj in dir(module):
		name = obj
		
		the_object = getattr(module, obj)
		obj_type = str(type(the_object))
		doc = the_object.__doc__
		
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
			if obj.__doc__ == """str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.""":
				val = "''"

			else:
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
		parse(getattr(wx.lib, submodule_name), fp)
		
		
def parse_tools_submodule(submodule_name):
	with open(f"wx/tools/{submodule_name}.py", "w") as fp:
		parse(getattr(wx.tools, submodule_name), fp)
		
		
def parse_py_submodule(submodule_name):
	with open(f"wx/py/{submodule_name}.py", "w") as fp:
		parse(getattr(wx.py, submodule_name), fp)
		

pathlib.Path("wx").mkdir()

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
		"ticker_xrc", "utils", "wordwrap", "wxpTag", "wxcairo"
		]:
	parse_lib_submodule(submodule)


if not pathlib.Path("./wx/tools").exists():
	pathlib.Path("./wx/tools").mkdir()

with open("wx/tools/__init__.py", "w") as fp:
	parse(wx.lib, fp)

for submodule in [
		"dbg", "helpviewer", "img2img", "img2png",
		"img2py", "img2xpm", "pywxrc", "wxget",
		]:
	parse_tools_submodule(submodule)
	
if not pathlib.Path("./wx/py").exists():
	pathlib.Path("./wx/py").mkdir()

with open("wx/py/__init__.py", "w") as fp:
	parse(wx.lib, fp)

for submodule in [
		"buffer", "crust", "crustslices", "dispatcher", "document",
		"editor", "editwindow", "filling", "frame", "images",
		"interpreter", "introspect", "magic", "parse", "path", "pseudo",
		"PyAlaCarte", "PyAlaMode", "PyAlaModeTest", "PyCrust", "PyFilling",
		"PyShell", "PySlices", "PySlicesShell", "PyWrap", "shell",
		"sliceshell", "version",
		]:
	parse_py_submodule(submodule)


for module in [
		"grid",	"dataview",	"richtext",	"ribbon", "aui",
		"html", "html2", "stc", "media", "adv",
		"propgrid", "xrc", "xml",
		]:
	parse_module(module)


# TODO: The following in wx.lib:
"""
agw
	aui
		aui_constants
		aui_switcherdialog
		aui_utilities
		auibar
		auibook
		dockart
		framemanager
		tabart
		tabmdi
	persist
		persist_constants
		persist_handler
		persistencemanager
	ribbon
		art
		art_aui
		art_default
		art_internal
		art_msw
		art_osx
		bar
		buttonbar
		control
		gallery
		page
		panel
		toolbar
		
	advancedsplash
	aquabutton
	artmanager
	balloontip
	buttonpanel
	cubecolourdialog
	customtreectrl
	flatmenu
	flatnotebook
	floatspin
	fmcustomizedlg
	fmresources
	foldpanelbar
	fourwaysplitter
	genericmessagedialog
	gradientbutton
	hyperlink
	hypertreelist
	infobar
	knobctrl
	labelbook
	multidirdialog
	peakmeter
	piectrl
	pybusyinfo
	pycollapsiblepane
	pygauge
	pyprogress
	rulerctrl
	shapedbutton
	shortcuteditor
	speedmeter
	supertooltip
	thumbnailctrl
	toasterbox
	ultimatelistctrl
	xlsgrid
	zoombar


analogclock
	lib_setup
		buttontreectrlpanel
		fontselect
	analogclick
	helpers
	setup
	styles
art
	flatart
	img2pyartprov
colourchooser
	canvas
	intl
	pycolourbox
	pycolourchooser
	pycolourslider
	pypalette
editor
	editor
	images
	selection
floatcanvas
	Utilities
		BBox
		Colors
		GUI
	FCEvents
	FCObjects
	FloatCanvas
	GUIMode
	NavCanvas
	Resources
	ScreenShot
gizmos
	dynamicsash
	ledctrl
	treelistctrl
masked
	combobox
	ctrl
	ipaddrctrl
	maskededit
	numctrl
	textctrl
	timectrl
mixins
	grid
	gridlabelrenderer
	imagelist
	inspection
	listctrl
	rubberband
	treemixin
ogl
	basic
	bmpshape
	canvas
	composit
	diagram
	divided
	drawn
	lines
	oglmisc
plot
	examples
		demo
		simple_example
	__main__
	plotcanvas
	plotobjects
	utils
"""
