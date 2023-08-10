import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import csv

class RetrieveData:
    def __init__(self, user_input_date):
        self.user_date_input = user_input_date

        #setting up lists to be populated with selected dates and their respective heights
        self.heights = []
        self.dates = []

    #ensuring user input is in correct date format
    @property
    def user_input_data(self):
        return self._user_input_data
    @user_input_data.setter
    def user_input_data(self, user_input_date):
        if user_input_date == datetime.strptime(user_input_date, '%Y/%m/%d'):
            self._user_input_data = user_input_date
        else:
            raise Exception('Please submit your date request in yyyy/mm/dd')


    #open csv file to populate dates and heights
    @property
    def dates(self):
        return self._dates
    @dates.setter
    def dates(self, dates):
        #must set all data in this method so that heights is matched appropriatley
        with open('NOAA-tides-date-and-time-same.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')

            #assigning data to dates and heights respectively
            for row in plots:
                if (self.user_date_input) in row [0]:
                    dates.append(row[0])
                    self.heights.append(int(row[2]))
        
        self._dates = dates