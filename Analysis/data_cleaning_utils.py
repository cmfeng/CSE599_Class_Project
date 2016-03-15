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
        infer_datetime_format=True, thousands=",", encoding='cp1252')

    print(raw_data.columns)
    global datecol        # Needed to make datetime column global
    datecol = input('What is your datetime column?')
    # Need to add code to catch errors and ensure this is in datetime format

    raw_data[datecol] = pd.to_datetime(raw_data[datecol])
    raw_data.index = raw_data[datecol]
    #Need to add code to catch errors and ensure this is in datetime format

    return raw_data

"""
Defining the first function to smooth the data
This will return the dataframe with the smoothed data overwriting the raw
it will also return a plot of the smoothed data overlaid on the raw data
"""
def test_smooth_data(column, raw_input):
    #This asks the user for what size window to average over
    window = int(input("What size windows do you want for the moving average? "))
    columns = []
    data = raw_input.copy()
    for x in data.columns[1:]:
        columns.append(x)
    for x in columns:
        if (type(data[x][0]) != str):
            try:
                moving = pd.rolling_mean(data[x], window)
                data[x] = moving
            except ValueError:
                print("Value Error")
                
    fig, ax = plt.subplots(2, figsize=(14, 6), sharex=True)
    raw_input[column].plot(ax=ax[0], title="RAW")
    data[column].plot(ax=ax[1], title=str(window) + " s moving average")
    return data


"""
Defining the function to reuce the size of the data
"""
def reducer(data):
    freq = input("What frequency would you like to resample to? Format = XS(seconds), XT(minutes)")
    #This will resample the data.  If downsampling, it will take the mean of the
    #points.  If upsampling, it will fill backwards
    columns = []
    for x in data.columns[:]:
        columns.append(x)
    for x in columns:
        if (type(data[x][0]) is str):
            try:
                for i in range(len(data[x])):
                    print(data[x][i])
                    data[x][i] = float(data[x][i].replace(',',''))
            except ValueError:
                print('Value Error')
    resampled = data.resample(freq)

    print('Num Samples Before: ' + str(data.size))
    print('Num Samples After: ' + str(resampled.size))
    return resampled


"""
Remove null values
"""

def nullRemover(datainput):
    
    cleanedoutput = datainput.dropna()
    print(datainput.shape)
    print(cleanedoutput.shape)
    return cleanedoutput






