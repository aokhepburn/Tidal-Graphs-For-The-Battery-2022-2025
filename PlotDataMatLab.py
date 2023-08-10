import matplotlib.pyplot as plt
import pandas as pd

class PlotData:
    def __init__(self, data):
        self.dates = data.dates
        self.heights = data.heights

    def plot_water_heights(self):
        x = self.dates
        y = self.heights
        plt.plot(x, y, color ="g", linestyle = 'dashed', marker = 'o',label = "Water Height")
        plt.xticks(rotation = 25)
        plt.xlabel('Date')
        plt.ylabel('Water Height')
        plt.title(('Tidal Heights At The Battery'), fontsize = 20)
        plt.grid()
        plt.legend()
        plt.show()