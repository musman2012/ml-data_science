import pandas as pd
import io
import requests
import numpy
import math
import itertools


flares = pd.read_csv(r"E:\Term 1 Bradford\Big Data Visualization\CW-2\flares.csv")
sunspots = pd.read_csv(r"E:\Term 1 Bradford\Big Data Visualization\CW-2\Sunspot time.csv")
length = 271883


flare_type_day = {}
counter = 0
counter2 = 0

x_flares_day = {}

flares.NOAA = flares.NOAA[:].astype(numpy.float)
flares.date = flares.date[:].astype(numpy.float)

for noaa in flares.NOAA:
    if math.isnan(flares.date[counter]) or math.isnan(noaa):
        counter += 1
        continue
    if flares.type[counter] == 'X':
        if noaa in x_flares_day:
            x_flares_day[noaa].append(flares.date[counter])
        else:
            x_flares_day[noaa] = [flares.date[counter]]
    counter += 1


counter = 0
prev_noaa = sunspots.NOAA[0]
prev_day = sunspots.date[0]
prev_size = sunspots.Size[0]
rates = []

for counter in range(1,len(sunspots.NOAA)) :
    
    if math.isnan(sunspots.Size[counter]):
        continue
    if sunspots.NOAA[counter] == prev_noaa:  # the same sunspot, check different date
        if sunspots.date[counter] == prev_day:
            continue
        else:
            if sunspots.NOAA[counter] in x_flares_day: # the same sunpot is present in x flares
                temp = x_flares_day[sunspots.NOAA[counter]]
                for day in temp:
                    if day == prev_day or day == sunspots.date[counter]:
                        diff = abs(sunspots.Size[counter] - prev_size)
                        #diff = (diff / prev_size)*100
                        rates.append(diff)
    prev_noaa = sunspots.NOAA[counter]
    prev_day = sunspots.date[counter]
    prev_size = sunspots.Size[counter]

counter1_25 = 0
counter25_50 = 0
counter51_75 = 0
counter75_100 = 0

for rate in rates:
    if 0.0 <= rate < 25.0:
        counter1_25 += 1
    elif 25.0 <= rate < 50.0:
        counter25_50 += 1
    elif 50.0 <= rate < 75.0:
        counter51_75 += 1
    else:
        counter75_100 += 1
        
print("{} {} {} {}".format(counter1_25, counter25_50, counter51_75, counter75_100))