from TidalPlottingInputDateRetrieveData import RetrieveData
from PlotDataMatLab import PlotData

#create userinput for selected day (to be expanded to date range)
userdateinput = input("Enter date query YYYY/MM/DD:")

#set user input data by passing the input to the RetrieveData class
choice_1 = RetrieveData(userdateinput)
mapLabGraph = PlotData(choice_1)

mapLabGraph.plot_water_heights()

