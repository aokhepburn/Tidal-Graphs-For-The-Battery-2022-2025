import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import make_interp_spline
import numpy as np
from TidalPlottingInputDateRetrieveData import RetrieveData

class PlotData:
    def __init__(self, data_1: RetrieveData, data_2: RetrieveData, data_3: RetrieveData):
        self.dates_1 = data_1.dates
        self.heights_1 = data_1.heights
        self.dates_2 = data_2.dates
        self.heights_2 = data_2.heights
        self.dates_3 = data_3.dates
        self.heights_3 = data_3.heights

#methods for adding extra dates
    def setting_data_for_plotting_x(self):
        x = []
        if self.dates_2 is not None:
            x.extend(self.dates_1)
            x.extend(self.dates_2)
        elif self.dates_3 is not None:
            x.extend(self.dates_3)
        else:
            x.extend(self.dates_1)
        return x
    def setting_data_for_plotting_y(self):
        y = []
        if self.heights_2 is not None:
            y.extend(self.heights_1)
            y.extend(self.heights_2)
        elif self.heights_3 is not None:
            y.extend(self.heights_3)
        else:
            y.extend(self.heights_1)
        return y

    def plot_water_heights(self):
        date = self.setting_data_for_plotting_x()
        tides = self.setting_data_for_plotting_y()
        x = date
        y = np.array(tides)

        #logic for trying to curve line
        #X_Y_Spline = make_interp_spline(x, y)

        # X_ = np.linspace(x.min(), x.max(), 500)
        # Y_ = X_Y_Spline(X_)

        plt.plot(x, y, color ="blue", linestyle = 'dashed', marker = 'o',label = "Water Height")
        plt.xticks(rotation = 25)
        plt.xlabel('Date')
        plt.ylabel('Water Height')
        plt.title(('Tidal Heights At The Battery'), fontsize = 20)
        plt.grid()
        plt.legend()
        plt.show()