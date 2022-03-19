import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plotting(x, y):
    plt.plot(x)
    plt.plot(y)

    plt.title("Longitude and Latitude of airports in Uk")

    plt.xlabel('Airports')
    plt.ylabel('Latitude & Longitude')
    plt.show()



# dataset
dataset = pd.read_csv("airport.csv")
mydata = dataset.iloc[:,1:7]

# filtering
airport_lat_long_data = mydata[["Name", "TotalSeats","Airport1Latitude","Airport1Longitude","color code"]]

airport_lat_long_dataUK = airport_lat_long_data[0:107]
set1 = airport_lat_long_dataUK['Airport1Latitude']
set2 = airport_lat_long_dataUK['Airport1Longitude']

# method calling
plotting(set1,set2)

