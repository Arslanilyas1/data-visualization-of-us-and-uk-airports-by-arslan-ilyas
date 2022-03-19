
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def histogramOfTop10Airports(totalseatUK):
    top10UK = totalseatUK[0:20]
    sns.histplot(top10UK, color = "purple", kde = True, bins = 20)

    plt.title("top 10 airports of UK")

    plt.xlabel('Airports')
    plt.ylabel('Seats booking')
    plt.show()

# dataset
dataset = pd.read_csv("airport.csv")
mydata = dataset.iloc[:,1:7]

# filtering
airport_lat_long_data = mydata[["Name", "TotalSeats","Airport1Latitude","Airport1Longitude","color code"]]

airport_lat_long_dataUK = airport_lat_long_data[0:107]
set1 = airport_lat_long_dataUK['Airport1Latitude']
set2 = airport_lat_long_dataUK['Airport1Longitude']
names = airport_lat_long_dataUK['Name']

# total seats
totalseats = airport_lat_long_dataUK['TotalSeats']

# color
clr = airport_lat_long_dataUK['color code']
c = clr[0:50]

# total seats of uk
totalseatUK = totalseats[0:100]


# for us
airport_lat_long_dataUS = airport_lat_long_data[107:207]
totalseatUS = airport_lat_long_dataUS['TotalSeats']

# method calling
histogramOfTop10Airports(totalseatUK)



