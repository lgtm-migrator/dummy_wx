"""
Script to generate wx/__init__.py
"""

# stdlib
import inspect
import re
import sys

del sys.path[0]

# stdlib
import pathlib

# this package
import wx
import wx.adv
import wx.aui
import wx.dataview
import wx.grid
import wx.html
import wx.html2
import wx.lib
import wx.lib.agw
import wx.lib.analogclock
import wx.lib.anchors
import wx.lib.art
import wx.lib.busy
import wx.lib.buttons
import wx.lib.calendar
import wx.lib.CDate
import wx.lib.ClickableHtmlWindow
import wx.lib.colourchooser
import wx.lib.colourdb
import wx.lib.colourselect
import wx.lib.colourutils
import wx.lib.combotreebox
import wx.lib.delayedresult
import wx.lib.dialogs
import wx.lib.docview
import wx.lib.dragscroller
import wx.lib.editor
import wx.lib.embeddedimage
import wx.lib.eventStack
import wx.lib.eventwatcher
import wx.lib.evtmgr
import wx.lib.expando
import wx.lib.fancytext
import wx.lib.filebrowsebutton
import wx.lib.floatcanvas
import wx.lib.foldmenu
import wx.lib.gestures
import wx.lib.gizmos
import wx.lib.gridmovers
import wx.lib.imagebrowser
import wx.lib.imageutils
import wx.lib.infoframe
import wx.lib.inspection
import wx.lib.intctrl
import wx.lib.itemspicker
import wx.lib.langlistctrl
import wx.lib.layoutf
import wx.lib.masked
import wx.lib.mixins
import wx.lib.msgpanel
import wx.lib.multisash
import wx.lib.newevent
import wx.lib.nvdlg
import wx.lib.ogl
import wx.lib.pdfwin
import wx.lib.platebtn
import wx.lib.plot
import wx.lib.popupctl
import wx.lib.printout
import wx.lib.progressindicator
import wx.lib.pubsub
import wx.lib.pydocview
import wx.lib.rcsizer
import wx.lib.resizewidget
import wx.lib.scrolledpanel
import wx.lib.sheet
import wx.lib.sized_controls
import wx.lib.softwareupdate
import wx.lib.splitter
import wx.lib.statbmp
import wx.lib.stattext
import wx.lib.throbber
import wx.lib.ticker
import wx.lib.ticker_xrc
import wx.lib.utils
import wx.lib.wordwrap
import wx.lib.wxcairo
import wx.lib.wxpTag
import wx.media
import wx.propgrid
import wx.py
import wx.py.buffer
import wx.py.crust
import wx.py.crustslices
import wx.py.dispatcher
import wx.py.document
import wx.py.editor
import wx.py.editwindow
import wx.py.filling
import wx.py.frame
import wx.py.images
import wx.py.interpreter
import wx.py.introspect
import wx.py.magic
import wx.py.parse
import wx.py.path
import wx.py.pseudo
import wx.py.PyAlaCarte
import wx.py.PyAlaMode
import wx.py.PyAlaModeTest
import wx.py.PyCrust
import wx.py.PyFilling
import wx.py.PyShell
import wx.py.PySlices
import wx.py.PySlicesShell
import wx.py.PyWrap
import wx.py.shell
import wx.py.sliceshell
import wx.py.version
import wx.ribbon
import wx.richtext
import wx.stc
import wx.tools
import wx.tools.dbg
import wx.tools.helpviewer
import wx.tools.img2img
import wx.tools.img2png
import wx.tools.img2py
import wx.tools.img2xpm
import wx.tools.pywxrc
import wx.tools.wxget
import wx.xml
import wx.xrc


def parse(module, fp):
	fp.write(
			"""# Based on wxPython
# Copyright: (c) 2018 by Total Control Software
# License:   wxWindows License


def dummy_function(*args, **kwargs):
	return 0


"""
			)

	seen_objects = []
	deferred_objects = []

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
		elif name == "wxWidgets_version":
			val = f"'{the_object}'"

		elif name.startswith("ID_") and the_object.__class__ is wx.WindowIDRef:
			val = int(the_object)

		elif name.startswith("IMAGE_OPTION_") and obj_type == "<class 'str'>":
			val = f"'{(getattr(wx, obj))}'"
		elif obj_type == "<class 'bytes'>":
			val = repr(the_object)
		elif obj_type == "<class 'str'>":
			val = repr(the_object)
		elif obj_type == "<class 'int'>":
			val = repr(the_object)
		elif obj_type == "<class 'float'>":
			val = repr(the_object)
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
		elif inspect.isclass(the_object):
			val = "object"
		elif obj_type.startswith("<class 'wx"):
			if the_object.__doc__ == """str(object='') -> str
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
				val = str(the_object)

		elif obj_type == "<class 'type'>":
			val = "object"
		elif obj_type == "<class 'PyCapsule'>":
			val = "object"

		else:
			print(name, obj_type)

		if val:
			if val == "INVALID DateTime":
				val = "''"

			group = '|'.join(["core", module.__name__.split('.')[-1]])
			repr_match = re.match(fr"<wx\._?({group})\.(.*) object at 0x.*>", val)
			if val == "object":
				fp.write(f"class {name}: ...\n")
			elif repr_match:
				if repr_match.group(1) in seen_objects:
					fp.write(f"{name} = {repr_match.group(2)}()\n")
				else:
					deferred_objects.append((name, repr_match.group(2)))
					continue
			else:
				fp.write(f"{name} = {val}\n")
			seen_objects.append(name)

	for name, repr_ in deferred_objects:
		fp.write(f"{name} = {repr_}()\n")


def parse_module(module_name):
	with open(f"wx/{module_name}.py", 'w') as fp:
		fp.write("from wx import PyEventBinder\n\n")
		parse(getattr(wx, module_name), fp)


def parse_lib_submodule(submodule_name):
	with open(f"wx/lib/{submodule_name}.py", 'w') as fp:
		parse(getattr(wx.lib, submodule_name), fp)


def parse_tools_submodule(submodule_name):
	with open(f"wx/tools/{submodule_name}.py", 'w') as fp:
		parse(getattr(wx.tools, submodule_name), fp)


def parse_py_submodule(submodule_name):
	with open(f"wx/py/{submodule_name}.py", 'w') as fp:
		parse(getattr(wx.py, submodule_name), fp)


pathlib.Path("wx").mkdir()

with open("wx/__init__.py", 'w') as fp:
	fp.write(
			"""

class PyEventBinder(object):
	def __init__(self, evtType=None, expectedIDs=0):
		pass

	def Bind(self, target, id1, id2, function):
		pass

	def Unbind(self, target, id1, id2, handler=None):
		return False

	def _getEvtType(self):
		return 0

	typeId = property(_getEvtType)


"""
			)

	parse(wx, fp)

if not pathlib.Path("./wx/lib").exists():
	pathlib.Path("./wx/lib").mkdir()
#
# with open("wx/lib/__init__.py", "w") as fp:
# 	fp.write("from wx import PyEventBinder\n\n")
# 	parse(wx.lib, fp)
#
# for submodule in [
# 		"anchors",
# 		"busy",
# 		"buttons",
# 		"calendar",
# 		"CDate",
# 		"ClickableHtmlWindow",
# 		"colourdb",
# 		"colourselect",
# 		"colourutils",
# 		"combotreebox",
# 		"delayedresult",
# 		"dialogs",
# 		"docview",
# 		"dragscroller",
# 		"embeddedimage",
# 		"eventStack",
# 		"eventwatcher",
# 		"evtmgr",
# 		"expando",
# 		"fancytext",
# 		"filebrowsebutton",
# 		"foldmenu",
# 		"gestures",
# 		"gridmovers",
# 		"imagebrowser",
# 		"imageutils",
# 		"infoframe",
# 		"inspection",
# 		"intctrl",
# 		"itemspicker",
# 		"langlistctrl",
# 		"layoutf",
# 		"msgpanel",
# 		"multisash",
# 		"newevent",
# 		"nvdlg",
# 		"pdfwin",
# 		"platebtn",
# 		"popupctl",
# 		"printout",
# 		"progressindicator",
# 		"pydocview",
# 		"rcsizer",
# 		"resizewidget",
# 		"scrolledpanel",
# 		"sheet",
# 		"sized_controls",
# 		"softwareupdate",
# 		"splitter",
# 		"statbmp",
# 		"stattext",
# 		"throbber",
# 		"ticker",
# 		"ticker_xrc",
# 		"utils",
# 		"wordwrap",
# 		"wxpTag",
# 		"wxcairo"
# 		]:
# 	parse_lib_submodule(submodule)

if not pathlib.Path("./wx/tools").exists():
	pathlib.Path("./wx/tools").mkdir()

with open("wx/tools/__init__.py", 'w') as fp:
	parse(wx.lib, fp)

for submodule in [
		"dbg",
		"helpviewer",
		"img2img",
		"img2png",
		"img2py",
		"img2xpm",
		"pywxrc",
		"wxget",
		]:
	parse_tools_submodule(submodule)

if not pathlib.Path("./wx/py").exists():
	pathlib.Path("./wx/py").mkdir()

with open("wx/py/__init__.py", 'w') as fp:
	parse(wx.lib, fp)

for submodule in [
		"buffer",
		"crust",
		"crustslices",
		"dispatcher",
		"document",
		"editor",
		"editwindow",
		"filling",
		"frame",
		"images",
		"interpreter",
		"introspect",
		"magic",
		"parse",
		"path",
		"pseudo",
		"PyAlaCarte",
		"PyAlaMode",
		"PyAlaModeTest",
		"PyCrust",
		"PyFilling",
		"PyShell",
		"PySlices",
		"PySlicesShell",
		"PyWrap",
		"shell",
		"sliceshell",
		"version",
		]:
	parse_py_submodule(submodule)

for module in [
		"grid",
		"dataview",
		"richtext",
		"ribbon",
		"aui",
		"html",
		"html2",
		"stc",
		"media",
		"adv",
		"propgrid",
		"xrc",
		"xml",
		]:
	parse_module(module)

# TODO: The following in wx.lib:
#
# agw
# 	aui
# 		aui_constants
# 		aui_switcherdialog
# 		aui_utilities
# 		auibar
# 		auibook
# 		dockart
# 		framemanager
# 		tabart
# 		tabmdi
# 	persist
# 		persist_constants
# 		persist_handler
# 		persistencemanager
# 	ribbon
# 		art
# 		art_aui
# 		art_default
# 		art_internal
# 		art_msw
# 		art_osx
# 		bar
# 		buttonbar
# 		control
# 		gallery
# 		page
# 		panel
# 		toolbar
#
# 	advancedsplash
# 	aquabutton
# 	artmanager
# 	balloontip
# 	buttonpanel
# 	cubecolourdialog
# 	customtreectrl
# 	flatmenu
# 	flatnotebook
# 	floatspin
# 	fmcustomizedlg
# 	fmresources
# 	foldpanelbar
# 	fourwaysplitter
# 	genericmessagedialog
# 	gradientbutton
# 	hyperlink
# 	hypertreelist
# 	infobar
# 	knobctrl
# 	labelbook
# 	multidirdialog
# 	peakmeter
# 	piectrl
# 	pybusyinfo
# 	pycollapsiblepane
# 	pygauge
# 	pyprogress
# 	rulerctrl
# 	shapedbutton
# 	shortcuteditor
# 	speedmeter
# 	supertooltip
# 	thumbnailctrl
# 	toasterbox
# 	ultimatelistctrl
# 	xlsgrid
# 	zoombar
#
#
# analogclock
# 	lib_setup
# 		buttontreectrlpanel
# 		fontselect
# 	analogclick
# 	helpers
# 	setup
# 	styles
# art
# 	flatart
# 	img2pyartprov
# colourchooser
# 	canvas
# 	intl
# 	pycolourbox
# 	pycolourchooser
# 	pycolourslider
# 	pypalette
# editor
# 	editor
# 	images
# 	selection
# floatcanvas
# 	Utilities
# 		BBox
# 		Colors
# 		GUI
# 	FCEvents
# 	FCObjects
# 	FloatCanvas
# 	GUIMode
# 	NavCanvas
# 	Resources
# 	ScreenShot
# gizmos
# 	dynamicsash
# 	ledctrl
# 	treelistctrl
# masked
# 	combobox
# 	ctrl
# 	ipaddrctrl
# 	maskededit
# 	numctrl
# 	textctrl
# 	timectrl
# mixins
# 	grid
# 	gridlabelrenderer
# 	imagelist
# 	inspection
# 	listctrl
# 	rubberband
# 	treemixin
# ogl
# 	basic
# 	bmpshape
# 	canvas
# 	composit
# 	diagram
# 	divided
# 	drawn
# 	lines
# 	oglmisc
# plot
# 	examples
# 		demo
# 		simple_example
# 	__main__
# 	plotcanvas
# 	plotobjects
# 	utils
