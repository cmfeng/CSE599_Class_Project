import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Importing the data.
This step is key, as we have to ensure that the time format 
of the data is recognized
"""
datecol = ""

def import_data(datafile):
    raw_data = pd.read_csv(datafile, parse_dates=True, 
        infer_datetime_format=True, thousands=",")
    print(raw_data.columns)
    global datecol        # Needed to make datetime column global
    datecol = input("datetime column name? ")

    raw_data[datecol] = pd.to_datetime(raw_data[datecol])
    #Need to add code to catch errors and ensure this is in datetime format
    return raw_data

"""
Defining the first function to smooth the data
This will return the dataframe with the smoothed data overwriting the raw
it will also return a plot of the smoothed data overlaid on the raw data
"""
def smooth_data(column, raw_input):
    data = raw_input
    #This asks the user for what size window to average over
    window = int(input("What size windows do you want for the moving average? "))
    moving = pd.rolling_mean(data[column], window)

    fig, ax = plt.subplots(2, figsize=(14, 6), sharex=True)

    data[column].plot(ax=ax[0], title="RAW")
    moving.plot(ax=ax[1], title=str(window) + " s moving average")

## Eventually, I want to make this iterative so that the user can change this
## it will overwrite the original column when the user is happy
    data[column] = moving
    return data

"""
Defining the function to reuce the size of the data
"""
def reducer(datainput):
    freq = input("What frequency would you like to resample to? Format = XS(seconds), XT(minutes)")
    #This will resample the data.  If downsampling, it will take the mean of the
    #points.  If upsampling, it will fill backwards

    datainput.index = datainput[datecol]
    resampled = datainput.resample(freq, fill_method='bfill')

    print(datainput.size)
    print(resampled.size)
    return resampled







