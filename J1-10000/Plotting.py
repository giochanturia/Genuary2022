from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

app = pg.mkQApp("Plotting Example")
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsLayoutWidget(show=True, title="Genuary 2022")
win.resize(600,600)
win.setWindowTitle('Genuary 2022: J1')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="J1: Draw 10,000 of something.", y=np.random.normal(size=100))

if __name__ == '__main__':
    pg.exec()