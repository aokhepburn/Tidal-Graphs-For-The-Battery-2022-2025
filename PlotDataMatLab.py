import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import make_interp_spline
import numpy as np
from TidalPlottingInputDateRetrieveData import RetrieveData

class PlotData:
    def __init__(self, data_1: RetrieveData):
        self.dates_1 = data_1.dates
        self.heights_1 = data_1.heights
        # self.dates_2 = data_2.dates
        # self.heights_2 = data_2.heights
        # self.dates_3 = data_3.dates
        # self.heights_3 = data_3.dates

#methods for adding extra dates
    # def setting_data_for_plotting_x(self, data_2 = None, data_3 = None):
        # x = []
        # if data_2 is not None:
        #     x.extend(self.dates_1)
        #     x.extend(data_2.dates)
        # elif data_3 is not None:
        #     x.extend(data_3.dates)
        # else:
        #     x.extend(self.dates_1)
        # return x
    # def setting_data_for_plotting_y(self, data_2 = None, data_3 = None):
    #     y = []
    #     if data_2.heights is not None:
    #         y.extend(self.heights_1)
    #         y.extend(data_2.heights)
    #     elif data_3.heights is not None:
    #         y.extend(data_3.heights)
    #     else:
    #         y.extend(self.heights_1)
    #     return y

    def plot_water_heights(self):
        date = self.dates_1
        tides = self.heights_1
        x = date
        y = tides

        #logic for trying to curve line
        # X_Y_Spline = make_interp_spline(x, y)

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