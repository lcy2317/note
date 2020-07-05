import wx
import wx.grid
from Global import Global


class ShowFrame(wx.Frame):
    def __init__(self, parent, title, value):
        super(ShowFrame, self).__init__(parent, title=title, size=(300, 230))
        self.Centre()
        self.value = value
        panel = wx.Panel(self, -1)
        self.TextValue = wx.TextCtrl(panel, -1, size=(300, 150), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.TextValue.SetValue(value)
        self.button_add = wx.Button(panel, -1, "复制到剪贴板", pos=(90, 160))
        self.Bind(wx.EVT_BUTTON, self.cp, self.button_add)

    def cp(self, event):
        clip_data = wx.TextDataObject()
        clip_data.SetText(self.value)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clip_data)
        wx.TheClipboard.Close()
        self.Close()
