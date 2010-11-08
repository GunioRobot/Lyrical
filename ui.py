import wx
try:
	import wx.lib.wxcairo
	import cairo
	haveCairo = True
except ImportError:
	haveCairo = False

#export VERSIONER_PYTHON_PREFER_32_BIT=yes

class ControlFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(640,480))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		
		self.CreateStatusBar() #A statusbar in the bottom of the window
		
		# Setting up the menu
		filemenu = wx.Menu()
		
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
		
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
		
		#Create the menubar
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		
		self.SetMenuBar(menuBar)
		
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		
		self.Show(True)
		
	def OnAbout(self, e):
		dialog = wx.MessageDialog(self, "A small text editor", "About Simple Text editor", wx.OK)
		dialog.ShowModal()
		dialog.Destroy()
	
	def OnExit(self, e):
		self.Close(True)

class LyricFrame(wx.Frame):
	def __init__(self, parent, title, displayNumber):
		#Hash out the multimonitor stuff. Fullscreen lyrics on selected monitor.
		display = wx.Display(displayNumber)
		geometry = display.GetGeometry()
		wx.Frame.__init__(self, parent, title=title, pos=geometry.GetTopLeft(),
			size=geometry.GetSize())
			
		self.canvas = LyricPanel(self)
		#self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
		self.Show()
	
	def OnExit(self, e):
		self.Close(True)
		
class LyricPanel(wx.Panel):
	def __init__(self, parent):
		#wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
		wx.Panel.__init__(self, parent, style=wx.BORDER_NONE)
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.text = ['Our God is an awesome God', 'He reigns from heaven above', 'with wisdom, power, and love', 'our God is an awesome God']
		self.x = 10
		self.y = 10
		self.ySpacing = 12
		
		self.windowWidth = 800
		self.windowHeight = 600

	#Draw the lyrics using Cairo and such
	def OnPaint(self, evt):
		dc = wx.PaintDC(self)
		
		dc.BeginDrawing()
		dc.SetBackgroundMode(wx.SOLID)
		dc.SetTextBackground(wx.BLACK)
		dc.SetTextForeground(wx.WHITE)
		
		#dc.SetBackgroundColor("black")
		dc.SetPen(wx.Pen(wx.BLACK, 1))
		dc.SetBrush(wx.Brush("black"))

		dc.DrawRectangle(0, 0, 800, 600) #dc.size.width, dc.size.height)
		dc.SetBackground(wx.Brush("black"))
				
		dc.Clear()
		dc.SetPen(wx.Pen(wx.BLACK, 4))
		dc.DrawLine(0,0,50,50)
		spacing = dc.GetCharHeight()
		for i in range(len(self.text)):
			dc.DrawText(self.text[i], self.x, self.y * i * spacing)
		
		#dc.DrawTextList(self.text, ((10, 10), (20, 20), (10, 10), (10, 10)), wx.WHITE, wx.BLACK)
		dc.EndDrawing()

	"""
		dc = wx.PaintDC(self)
		
		width, height = self.GetClientSize()
		cr = wx.lib.wxcairo.ContextFromDC(dc)
		
		#Here's actual Cairo drawing
		size = min(width, height)
		cr.scale(size, size)
		
		cr.set_source_rgb(0, 0, 0) #black
		cr.rectangle(0, 0, width, height)
		cr.fill()
		
		cr.set_source_rgb(1, 1, 1) #white
		
		cr.set_line_width (0.04)

		cr.select_font_face ("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
		textFontSize = 0.07
		cr.set_font_size (textFontSize)

		textPosY = 0.1
		textPosX = 0.1
		for line in self.text:
			cr.move_to (textPosX, textPosY)
			cr.show_text (line)
			textPosY += textFontSize + 0.01
		
		#cr.move_to (0.27, 0.65)
		#cr.text_path ("void")
		#cr.set_source_rgb (0.5,0.5,1)
		#cr.fill_preserve ()
		#cr.set_source_rgb (0,0,0)
		#cr.set_line_width (0.01)
		
		cr.stroke ()
	"""	

	#Change what lyrics are shown
	def SetLyrics(self, text):
		self.text = text
		self.Refresh()

app = wx.App(False)
num_displays = wx.Display.GetCount()
#if num_displays < 2:
#	print 'Fewer than two screens detected. Please connect a projector'
#else:
lyricFrame = LyricFrame(None, 'Lyrical', 0)
#controlFrame = ControlFrame(None, 'Lyrical')
app.MainLoop()