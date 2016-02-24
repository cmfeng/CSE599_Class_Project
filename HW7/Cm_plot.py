"""
Changming's function for HW7
creates a graphic user interface
generating time series with column chosen by user
"""
import pandas as pd
import matplotlib
matplotlib.use('WX')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx


class interface(wx.Frame):
    def __init__(self):
        # ids for panel and widgets in frame
        frame_id = 0
        panel_id = 1
        panel_id2 = 2
        cmbox_id = 2
        bt_id = 3
        # building new frame
        wx.Frame.__init__(self, None, frame_id, 'TimePlot', size=(1000, 500))
        """
        the file name or path( if not in the same folder with py file)
        of the data file
        """
        csvfile = 'pool82014-10-02cleaned.csv'
        self.data = pd.read_csv(csvfile, low_memory=False)
        self.time = pd.DatetimeIndex(self.data['time'])
        # get the column names for comobox
        columns = []
        for x in self.data.columns:
            columns.append(x)
        self.panel = wx.Panel(self, panel_id, style=wx.BORDER)
        self.panel2 = wx.Panel(self, panel_id2, style=wx.BORDER)
        self.cb = wx.ComboBox(self.panel, cmbox_id, choices=columns[2:])
        self.bt = wx.Button(self.panel, bt_id, label='plot')
        # add the figure to panel2
        self.figure = Figure()
        self.canvas = FigureCanvas(self.panel2, -1, self.figure)

        # sizer for panel1
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(self.cb, 1, wx.ALIGN_CENTER)
        vSizer.Add(self.bt, 1, wx.ALIGN_CENTER)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        hSizer.Add(vSizer, 1, wx.ALIGN_CENTER)
        self.panel.SetSizer(hSizer)

        # sizer for panel2
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(self.canvas, 1, wx.EXPAND)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        hSizer.Add(vSizer, 1, wx.EXPAND)
        self.panel2.SetSizer(hSizer)

        # sizer for frame
        vSizer1 = wx.BoxSizer(wx.VERTICAL)
        vSizer1.Add(self.panel, 2, wx.EXPAND)
        vSizer1.Add(self.panel2, 8, wx.EXPAND)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        hSizer.Add(vSizer1, 1, wx.EXPAND)
        self.SetSizer(hSizer)

        # button event to trigger plot function
        wx.EVT_BUTTON(self, bt_id, self.plot)
        self.Show()

    # function to plot series
    def plot(self, e):
        y = self.cb.GetValue()
        self.figure.add_subplot(111).plot(self.time, self.data[y])

# main function
ftApp = wx.App()
ftFrame = interface()
ftApp.MainLoop()
