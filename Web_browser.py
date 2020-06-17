import wx
import wx.html2 as webview
import wx.grid as grid
import urllib.request
import code_TEST_file


class OtherFrame(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Show()

        My_GridView = grid.Grid(self)  # grid is an Module or Package Which import above
        My_GridView.CreateGrid(1000, 10)
        My_GridView.SetColLabelValue(0, 'Email ID')
        My_GridView.SetColSize(0, 120)
        My_GridView.SetColLabelValue(1, 'Address')
        My_GridView.SetColSize(1, 120)
        My_GridView.SetColLabelValue(2, 'Country')
        My_GridView.SetColSize(2, 120)
        My_GridView.SetColLabelValue(3, 'Purchaser')
        My_GridView.SetColSize(3, 120)
        My_GridView.SetColLabelValue(4, 'Tender No')
        My_GridView.SetColSize(4, 120)
        My_GridView.SetColLabelValue(5, 'Tender Details')
        My_GridView.SetColSize(5, 120)
        My_GridView.SetColLabelValue(6, 'Title')
        My_GridView.SetColSize(6, 120)
        My_GridView.SetColLabelValue(7, 'Submission Date')
        My_GridView.SetColSize(7, 120)
        My_GridView.SetColLabelValue(8, 'Tender Link')
        My_GridView.SetColSize(8, 120)
        My_GridView.SetColLabelValue(9, 'Source Name')
        My_GridView.SetColSize(9, 120)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(My_GridView, 10, wx.EXPAND)
        self.SetSizer(sizer)


class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        url_list = ['http://lpse.depkes.go.id/eproc4/lelang','http://lpse.depkes.go.id/eproc4/lelang']
        for test_url in url_list:
            self.current = str(test_url)  # http://lpse.depkes.go.id/eproc4/lelang

            self.frame = self.GetTopLevelParent()
            self.titleBase = self.frame.GetTitle()

            sizer = wx.BoxSizer(wx.VERTICAL)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            self.wv = webview.WebView.New(self)

            self.Bind(webview.EVT_WEBVIEW_NAVIGATING, self.OnWebViewNavigating,self.wv)
            self.Bind(webview.EVT_WEBVIEW_NAVIGATED, self.OnWebViewNavigated, self.wv)
            self.Bind(webview.EVT_WEBVIEW_LOADED, self.OnWebViewLoaded, self.wv)
            self.Bind(webview.EVT_WEBVIEW_TITLE_CHANGED, self.OnWebViewTitleChanged, self.wv)

            My_GridView = grid.Grid(self)  # grid is an Module or Package Which import above
            My_GridView.CreateGrid(10, 10)
            My_GridView.SetColLabelValue(0, 'Email ID')
            My_GridView.SetColSize(0, 120)
            My_GridView.SetColLabelValue(1, 'Address')
            My_GridView.SetColSize(1, 120)
            My_GridView.SetColLabelValue(2, 'Country')
            My_GridView.SetColSize(2, 120)
            My_GridView.SetColLabelValue(3, 'Purchaser')
            My_GridView.SetColSize(3, 120)
            My_GridView.SetColLabelValue(4, 'Tender No')
            My_GridView.SetColSize(4, 120)
            My_GridView.SetColLabelValue(5, 'Tender Details')
            My_GridView.SetColSize(5, 120)
            My_GridView.SetColLabelValue(6, 'Title')
            My_GridView.SetColSize(6, 120)
            My_GridView.SetColLabelValue(7, 'Submission Date')
            My_GridView.SetColSize(7, 120)
            My_GridView.SetColLabelValue(8, 'Tender Link')
            My_GridView.SetColSize(8, 120)
            My_GridView.SetColLabelValue(9, 'Source Name')
            My_GridView.SetColSize(9, 120)

            # # My_GridView.SetRowSize(0, 10)  # Size OF The ROW IF You Wanna See The Result uncomment The Code
            # # My_GridView.SetColSize(0, 20)  # Size OF The COL IF You Wanna See The Result uncomment The Code
            # # =====================================================================================================
            # # EMAIL ID
            # # My_GridView.SetCellValue(0, 0, 'Email ID')  # Insert The Value on Grid For Result
            # # My_GridView.SetCellBackgroundColour(0, 0, wx.LIGHT_GREY)  # Gave the BG color to cell
            # # =====================================================================================================
            # # ADDRESS & CONTACT PERSON
            # My_GridView.SetCellValue(0, 1, 'Address')  # Insert The Value on Grid For Result
            # My_GridView.SetCellBackgroundColour(0, 1, wx.LIGHT_GREY)  # Gave the BG color to cell
            # # =====================================================================================================
            # # COUNTRY
            # My_GridView.SetCellValue(0, 2, 'Country')
            # My_GridView.SetCellBackgroundColour(0, 2, wx.LIGHT_GREY)
            # # =====================================================================================================
            # # Purchaser
            # My_GridView.SetCellValue(0, 3, 'Purchaser')
            # My_GridView.SetCellBackgroundColour(0, 3, wx.LIGHT_GREY)
            # # =====================================================================================================
            # # Tender No
            # My_GridView.SetCellValue(0, 4, 'Tender No')
            # My_GridView.SetCellBackgroundColour(0, 4, wx.LIGHT_GREY)
            # # =====================================================================================================
            # # Tender Details
            # My_GridView.SetCellValue(0, 5, 'Tender Details')
            # My_GridView.SetCellBackgroundColour(0, 5, wx.LIGHT_GREY)
            # # =====================================================================================================
            # # Tender Title
            # My_GridView.SetCellValue(0, 6, 'Title')
            # My_GridView.Center(0)
            # My_GridView.SetCellBackgroundColour(0, 6, wx.LIGHT_GREY)

            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(My_GridView,0, wx.EXPAND)
            self.SetSizer(sizer)

            btn = wx.Button(self, -1, "Open", style=wx.BU_EXACTFIT)
            self.Bind(wx.EVT_BUTTON, self.OnOpenButton, btn)
            btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

            btn = wx.Button(self, -1, "Show Grid Data", style=wx.BU_EXACTFIT)
            self.Bind(wx.EVT_BUTTON, self.on_new_frame, btn)
            # self.Bind(wx.EVT_BUTTON, self.getHTMLCode, btn)
            btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
            self.frame_number = 1

            btn = wx.Button(self, -1, "<--", style=wx.BU_EXACTFIT)
            self.Bind(wx.EVT_BUTTON, self.OnPrevPageButton, btn)
            btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
            self.Bind(wx.EVT_UPDATE_UI, self.OnCheckCanGoBack, btn)

            btn = wx.Button(self, -1, "-->", style=wx.BU_EXACTFIT)
            self.Bind(wx.EVT_BUTTON, self.OnNextPageButton, btn)
            btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
            self.Bind(wx.EVT_UPDATE_UI, self.OnCheckCanGoForward, btn)

            btn = wx.Button(self, -1, "Stop", style=wx.BU_EXACTFIT)
            self.Bind(wx.EVT_BUTTON, self.OnStopButton, btn)
            btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

            btn = wx.Button(self, -1, "Refresh", style=wx.BU_EXACTFIT)
            self.Bind(wx.EVT_BUTTON, self.OnRefreshPageButton, btn)
            btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

            txt = wx.StaticText(self, -1, "Location:")
            btnSizer.Add(txt, 0, wx.CENTER|wx.ALL, 2)

            self.location = wx.ComboBox(
                self, -1, "", style=wx.CB_DROPDOWN|wx.TE_PROCESS_ENTER)
            self.location.AppendItems(['http://wxPython.org',
                                       'http://wxwidgets.org',
                                       'http://google.com'])
            # print(self.location)
            # for url in ['http://wxPython.org',
            #            'http://wxwidgets.org',
            #            'http://google.com']:
            #    item = webview.WebViewHistoryItem(url, url)
            #    self.wv.LoadHistoryItem(item)

            self.Bind(wx.EVT_COMBOBOX, self.OnLocationSelect, self.location)
            self.location.Bind(wx.EVT_TEXT_ENTER, self.OnLocationEnter)
            btnSizer.Add(self.location, 1, wx.EXPAND|wx.ALL, 2)

            sizer.Add(btnSizer, 0, wx.EXPAND)
            sizer.Add(self.wv, 1, wx.EXPAND)
            self.SetSizer(sizer)
            self.wv.LoadURL(self.current)  # Load URL and show result on GUI Form

    def on_new_frame(self, event):
        title = 'SubFrame {}'.format(self.frame_number)

        frame = OtherFrame(title=title)
        frame.SetDimensions(0, 0, 800, 600)
        self.frame_number += 1

    def OnWebViewNavigating(self, evt):
        # this event happens prior to trying to get a resource
        if evt.GetURL() == 'http://www.microsoft.com/':
            if wx.MessageBox("Are you sure you want to visit Microsoft?",
                             style=wx.YES_NO|wx.ICON_QUESTION) == wx.NO:
                # This is how you can cancel loading a page.
                evt.Veto()

    def OnWebViewNavigated(self, evt):
        self.frame.SetStatusText("Loading %s..." % evt.GetURL())

    def OnWebViewTitleChanged(self, evt):
        # Set the frame's title to include the document's title
        self.frame.SetTitle("%s -- %s" % (self.titleBase, evt.GetString()))

    # Control bar events
    def OnLocationSelect(self, evt):
        url = self.location.GetStringSelection()
        print('OnLocationSelect: %s\n' % url)
        self.wv.LoadURL(url)
        # WebView events

    def OnLocationEnter(self, evt):
        url = self.location.GetValue()
        self.location.Append(url)
        self.wv.LoadURL(url)

    def OnWebViewLoaded(self, evt):
        # The full document has loaded
        self.current = evt.GetURL()
        # print(self.current)
        self.location.SetValue(self.current)
        self.frame.SetStatusText("Loaded")
        # =========================================================================================

        if code_TEST_file.value != 0:
            HTML_CODE = self.wv.GetPageSource()  # GET HTML SOURCE CODE OR HTML CODE
            print(HTML_CODE)
            code_TEST_file.value = 0
        else:
            code_TEST_file.value += 1
        # =========================================================================================

    def OnOpenButton(self, event):
        dlg = wx.TextEntryDialog(self, "Open Location",
                                "Enter a full URL or local path",
                                self.current, wx.OK|wx.CANCEL)
        dlg.CentreOnParent()

        if dlg.ShowModal() == wx.ID_OK:
            self.current = dlg.GetValue()
            self.wv.LoadURL(self.current)

        dlg.Destroy()

    def OnPrevPageButton(self, event):
        for i in self.wv.GetBackwardHistory():
            print("%s %s" % (i.Url, i.Title))
        self.wv.GoBack()

    def OnNextPageButton(self, event):
        for i in self.wv.GetForwardHistory():
            print("%s %s" % (i.Url, i.Title))
        self.wv.GoForward()

    def OnCheckCanGoBack(self, event):
        event.Enable(self.wv.CanGoBack())

    def OnCheckCanGoForward(self, event):
        event.Enable(self.wv.CanGoForward())

    def OnStopButton(self, evt):
        self.wv.Stop()

    def OnRefreshPageButton(self, evt):
        self.wv.Reload()


def main():
    app = wx.App()
    frm = wx.Frame(None, title="html2.WebView sample", size=(1520, 800))
    frm.CreateStatusBar()
    pnl = TestPanel(frm)
    frm.Show()
    app.MainLoop()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == '__main__':
    main()

