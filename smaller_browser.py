import wx
import wx.html2 as webview
from urlparse import urlparse

class BrowseDaNet(wx.Frame):

  def __init__(self, parent=None, id=-1, window_title="Me da browsa"):
    super(BrowseDaNet, self).__init__(parent, id, window_title)
    self.InitGUI()

  def InitGUI(self):
    self.InitMenu()
    self.InitStatusBar()
    self.DrawApp()
    #self.Maximize()
    self.SetSize((1200,500))
    self.Centre()

  def DrawApp(self):
    self.web_view = webview.WebView.New(self)
    self.web_view.LoadURL("about:blank")
    self.address_bar = wx.TextCtrl(self, name="URL", style=wx.TE_PROCESS_ENTER)
    self.Bind(wx.EVT_TEXT_ENTER, self.ChangeURL, self.address_bar)
    v_sizer = wx.BoxSizer(wx.VERTICAL)
    v_sizer.Add(self.address_bar, 0, wx.EXPAND)
    v_sizer.Add(self.web_view, 1, wx.EXPAND)
    self.SetSizerAndFit(v_sizer)

  def ChangeURL(self, event):
    user_input = self.address_bar.GetValue()
    url = urlparse(user_input)
    load_url = url.geturl()
    if url.scheme != "http":
      load_url = "http://" + load_url
    self.web_view.LoadURL(load_url)
    self.address_bar.SetValue(load_url)

  def InitMenu(self):
    menu_bar = wx.MenuBar()
    file_menu = wx.Menu()
    quit_item = file_menu.Append(wx.ID_EXIT, "Quit", "Quit the browser")
    menu_bar.Append(file_menu, "&File")
    self.Bind(wx.EVT_MENU, self.OnQuit, quit_item)
    self.SetMenuBar(menu_bar)

  def InitStatusBar(self):
    self.status_bar = self.CreateStatusBar()
    self.status_bar.Show()

  def OnQuit(self, event):
    self.Close()

if __name__=="__main__":
  app = wx.App()
  browser = BrowseDaNet(window_title="IE 12.0")
  browser.Show()
  app.MainLoop()
