
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def AnalyzeSeatsOfUKAirports():
    plt.figure(figsize=(5,5))
    lstAirport = ['cambridge','Black Pool','Tees valley','London Oxford Airport','Inverness Airport']
    totalseats = [4368,110595,83345,5633,73895]

    clr = sns.color_palette('muted')[0:5]
    plt.pie(totalseats, labels = lstAirport, colors = clr, autopct='%.0f%%')

    plt.title("which airport is more busy in UK")

    plt.show()


AnalyzeSeatsOfUKAirports()



