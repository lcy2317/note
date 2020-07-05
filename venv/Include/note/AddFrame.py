import wx
from Global import Global
import math


class AddFrame(wx.Frame):
    def __init__(self, parent, title):
        super(AddFrame, self).__init__(parent, title=title, size=(400, 230))
        self.Centre()
        panel = wx.Panel(self, -1)
        self.LabelKey = wx.StaticText(panel, -1, "key:", (20, 13), size=(40, -1))
        self.LabelValue = wx.StaticText(panel, -1, "value:", (20, 40), size=(40, -1))
        self.TextKey = wx.TextCtrl(panel, -1, pos=(60, 10), size=(300, -1))
        self.TextValue = wx.TextCtrl(panel, -1, pos=(60, 40), size=(300, 100), style=wx.TE_MULTILINE)
        self.Button = wx.Button(panel, -1, "添加", pos=(150, 155))
        self.Bind(wx.EVT_BUTTON, self.add, self.Button)
        self.Button.SetDefault()

    def add(self, event):

        if str(self.TextKey.GetValue()).strip() == '':
            fail = wx.MessageDialog(None, u"添加失败, key不能为空", u"添加", wx.ICON_EXCLAMATION)
            fail.ShowModal()
            return
        if self.TextKey.GetValue() in Global.records.keys():
            # 添加失败
            fail = wx.MessageDialog(None, u"添加失败, key已存在", u"添加", wx.ICON_EXCLAMATION)
            fail.ShowModal()
            return
        Global.records[self.TextKey.GetValue()] = self.TextValue.GetValue()
        self.Close()