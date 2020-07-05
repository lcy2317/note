from AddFrame import AddFrame
from AllFrame import AllFrame
from ShowFrame import ShowFrame
from Global import Global
import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(350, 350))
        self.Centre()
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_LEFT_DOWN, self.resize)
        self.button_add = wx.Button(panel, -1, "添加", pos=(50, 60))
        self.Bind(wx.EVT_BUTTON, self.add, self.button_add)
        self.button_all = wx.Button(panel, -1, "数据管理", pos=(150, 60))
        self.Bind(wx.EVT_BUTTON, self.all, self.button_all)

        # 临时添加一些
        Global.records['百度'] = 'asdas12312das'
        Global.records['百度123'] = 'asd123asdas'
        Global.records['百1231度'] = 'asd123asdas'
        Global.records['百123度'] = 'asda23sdas'
        Global.records['百34度'] = 'asdas31sdas'
        Global.records['百65度'] = 'asda1231233sdas'
        Global.records['百1度'] = 'asdasd123as'
        Global.records['百412度'] = 'asda123sdas'
        # ================

        # 添加搜索框
        self.text_box = wx.TextCtrl(panel, -1, pos=(30, 10), size=(280, -1))
        self.Bind(wx.EVT_SET_FOCUS, self.search_hint, self.text_box)
        self.Bind(wx.EVT_TEXT, self.search_hint, self.text_box)
        # 添加搜索提示框
        self.listbox = wx.ListBox(panel, pos=(30, 36), size=(280, 150))
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.checked, self.listbox)
        self.hbox.Hide(False)

        # 搜索图标
        image = wx.Image(r'note\search.png', wx.BITMAP_TYPE_PNG)
        my_pic = image.ConvertToBitmap()
        wx.StaticBitmap(panel, -1, bitmap=my_pic, pos=(8, 15))

    def add(self, event):
        frame = AddFrame(None, title='Note')
        frame.Show()

    def all(self, event):
        frame = AllFrame(None, title='查看所有数据')
        frame.Show()

    def search_hint(self, event):
        self.listbox.Clear()
        self.hbox.Show(False)
        self.button_add.Hide()
        self.button_all.Hide()
        for key, value in Global.records.items():
            if self.text_box.GetValue() in key:
                self.listbox.Append(key)

    def checked(self, event):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        s = ShowFrame(None, title='Note', value=Global.records[text])
        s.Show()

    def resize(self, event):
        self.hbox.Hide(False)
        self.button_add.Show()
        self.button_all.Show()


if __name__ == '__main__':
    app = wx.App()
    ex = MainFrame(None, title='Note')
    ex.Show()
    app.MainLoop()
