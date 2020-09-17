# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sqlite3


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_txtId = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_txtId, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer2.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_txtName = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_txtName, 0, wx.ALL, 5)

        self.m_bntInsert = wx.Button(self.m_panel1, wx.ID_ANY, u"추가", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_bntInsert, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_lstList = wx.ListCtrl(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer3.Add(self.m_lstList, 1, wx.ALL | wx.EXPAND, 5)

        self.m_lstList.InsertColumn(0, "id", width=200)
        self.m_lstList.InsertColumn(1, "name", width=200)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bntInsert.Bind(wx.EVT_BUTTON, self.onInsert)

        # DB 생성자
        self.dbLoad()

    def __del__(self):
        pass


    # DB 연결! 윈도우 창에서 DB 내용을 showing
    def dbLoad(self):

        # 결과 화면에 누적되지 않게끔.(중복되지 않게끔)
        self.m_lstList.ClearAll()
        # 그리고 다시 생성
        self.m_lstList.InsertColumn(0, "id", width=200)
        self.m_lstList.InsertColumn(1, "name", width=200)

        conn = sqlite3.connect("nice.db")
        cur = conn.cursor()

        cur.execute("select * from emp")
        for row in cur:
            # print(row[0], ",", row[1])

            i = self.m_lstList.InsertItem(1000, row[0])
            self.m_lstList.SetItem(i, 0, str(row[0]))
            self.m_lstList.SetItem(i, 1, str(row[1]))

        cur.close()
        conn.close()



    # Virtual event handlers, overide them in your derived class
    def onInsert(self, event):
        # 윈도우 창에서 값을 입력받아서 변수에 저장 후 튜플로 묶기
        id = self.m_txtId.GetValue()
        name = self.m_txtName.GetValue()
        ins_data = (id, name)

        # 입력받은 값을 DB에 Insert
        conn = sqlite3.connect("nice.db")
        cur = conn.cursor()
        cur.execute("insert into emp values(?,?)", ins_data)
        conn.commit()

        # DB close
        cur.close()
        conn.close()

        # DB에 저장된 데이터 목록 화면에 showing
        self.dbLoad()


if __name__ == "__main__":
    app = wx.App()
    MyFrame1(None).Show(True)
    app.MainLoop()