from TidalPlottingInputDateRetrieveData import RetrieveData
from PlotDataMatLab import PlotData

#create userinput for selected day (to be expanded to date range)
userdateinput = input("Enter date query YYYY/MM/DD:     ")
# another_date_input = input("Would you like to enter another date (Y/N)?      ")
choice_1 = RetrieveData(userdateinput)
#mapLabGraph = PlotData(choice_1)

userdateinput2 = input("Enter date query YYYY/MM/DD:    ")
choice_2 = RetrieveData(userdateinput2)
userdateinput3 = input("Enter date query YYYY/MM/DD:    ")
choice_3 = RetrieveData(userdateinput3)

# create more userinputs for dates
# if another_date_input == "Y":
#     userdateinput2 = input("Enter date query YYYY/MM/DD:")
#     choice_2 = RetrieveData(userdateinput2)
#     mapLabGraph = PlotData(choice_1, choice_2)
#     another_date_input3 = input("Would you like to enter another date (Y/N)?      ")
#     if another_date_input3 == "Y":
#         userdateinput3 = input("Enter date query YYYY/MM/DD:")
#         choice_3 = RetrieveData(userdateinput3)
#         mapLabGraph = PlotData(choice_1, choice_2, choice_3)
            
#set user input data by passing the input to the RetrieveData class
mapLabGraph  = PlotData(choice_1, choice_2, choice_3)

mapLabGraph.plot_water_heights()

