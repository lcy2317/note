import wx
import wx.grid
from Global import Global


class AllFrame(wx.Frame):
    def __init__(self, parent, title):
        super(AllFrame, self).__init__(parent, title=title, size=(500, 400))
        self.Centre()

        panel = wx.Panel(self, -1)
        self.listbox = wx.ListBox(panel, size=(250, 360))
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.checked, self.listbox)
        self.h_box = wx.BoxSizer(wx.HORIZONTAL)
        self.h_box.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        for key in Global.records:
            self.listbox.Append(key)
        self.TextValue = wx.TextCtrl(panel, -1, pos=(250, 0), size=(250, 150), style=wx.TE_MULTILINE)

        self.button_save = wx.Button(panel, -1, "保存", pos=(330, 160))
        self.Bind(wx.EVT_BUTTON, self.save, self.button_save)

    def checked(self, event):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        self.TextValue.SetValue(Global.records[text])

    def save(self, event):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        Global.records[text] = self.TextValue.GetValue()
        fail = wx.MessageDialog(None, u"保存成功", u"保存", wx.ICON_INFORMATION)
        fail.ShowModal()
