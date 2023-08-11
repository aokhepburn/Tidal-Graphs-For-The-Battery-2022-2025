import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import csv

class RetrieveData:
    def __init__(self, user_date_input):
        self.user_date_input = user_date_input

        #setting up lists to be populated with selected dates and their respective heights
        self.heights = []
        self.dates = []

    #ensuring user input is in correct date format 
    # @property
    # def user_date_input(self):
    #     return self.user_date_input
    # @user_date_input.setter
    # def user_date_input(self, user_date_input):
    #     if user_date_input.MinYear >= 2022 and user_date_input.MaxYear <= 2025:
    #         self._user_date_input = user_date_input
    #     else:
    #         raise Exception('Please submit your date request in yyyy/mm/dd')


    #open csv file to populate dates and heights
    @property
    def dates(self):
        return self._dates
    @dates.setter
    def dates(self, dates):
        #must set all data in this method so that heights is matched appropriatley
        with open('data/NOAA-tide-predictions-battery-yr2022-2025.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')

            #assigning data to dates and heights respectively
            for row in plots:
                if (self.user_date_input) in row [0]:
                    dates.append(row[0] + row[2])
                    self.heights.append(int(row[4]))
                    # self.times.append(row[2])
        
        self._dates = dates