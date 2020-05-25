import pytest


@pytest.mark.parametrize("mod", [
		"wx",
		"wx.ribbon", "wx.grid", "wx.dataview", "wx.richtext", "wx.html",
		"wx.html2", "wx.stc", "wx.media", "wx.propgrid", "wx.xrc", "wx.xml",
		"wx.adv", "wx.aui",

		"wx.tools",
		"wx.tools.dbg", "wx.tools.helpviewer", "wx.tools.img2img", "wx.tools.img2png",
		"wx.tools.img2py", "wx.tools.img2xpm", "wx.tools.pywxrc", "wx.tools.wxget",

		"wx.py",
		"wx.py.buffer", "wx.py.crust", "wx.py.crustslices", "wx.py.dispatcher",
		"wx.py.document", "wx.py.editor", "wx.py.editwindow", "wx.py.filling",
		"wx.py.frame", "wx.py.images", "wx.py.interpreter", "wx.py.introspect",
		"wx.py.magic", "wx.py.parse", "wx.py.path", "wx.py.pseudo", "wx.py.PyAlaCarte",
		"wx.py.PyAlaMode", "wx.py.PyAlaModeTest", "wx.py.PyCrust", "wx.py.PyFilling",
		"wx.py.PyShell", "wx.py.PySlices", "wx.py.PySlicesShell", "wx.py.PyWrap",
		"wx.py.shell", "wx.py.sliceshell", "wx.py.version",

		"wx.lib",
		"wx.lib.anchors", "wx.lib.busy", "wx.lib.buttons", "wx.lib.calendar",
		"wx.lib.ClickableHtmlWindow", "wx.lib.colourdb", "wx.lib.colourselect",
		"wx.lib.colourutils", "wx.lib.combotreebox", "wx.lib.delayedresult",
		"wx.lib.dialogs", "wx.lib.docview", "wx.lib.dragscroller", "wx.lib.splitter",
		"wx.lib.eventStack", "wx.lib.eventwatcher", "wx.lib.evtmgr", "wx.lib.CDate",
		"wx.lib.fancytext", "wx.lib.filebrowsebutton", "wx.lib.foldmenu",
		"wx.lib.gridmovers", "wx.lib.imagebrowser", "wx.lib.imageutils", "wx.lib.nvdlg",
		"wx.lib.inspection", "wx.lib.intctrl", "wx.lib.itemspicker", "wx.lib.ticker_xrc",
		"wx.lib.layoutf", "wx.lib.msgpanel", "wx.lib.multisash", "wx.lib.newevent",
		"wx.lib.pdfwin", "wx.lib.platebtn", "wx.lib.popupctl", "wx.lib.printout",
		"wx.lib.pydocview", "wx.lib.rcsizer", "wx.lib.resizewidget",
		"wx.lib.sheet", "wx.lib.sized_controls", "wx.lib.softwareupdate",
		"wx.lib.statbmp", "wx.lib.stattext", "wx.lib.throbber", "wx.lib.ticker",
		"wx.lib.utils", "wx.lib.wordwrap", "wx.lib.wxpTag", "wx.lib.progressindicator",
		"wx.lib.langlistctrl", "wx.lib.embeddedimage", "wx.lib.expando",
		"wx.lib.gestures", "wx.lib.infoframe", "wx.lib.scrolledpanel", "wx.lib.wxcairo",
		])
def test_successful_imports(mod):
	assert __import__(mod)
