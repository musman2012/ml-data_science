import pandas as pd
import io
import requests
import numpy

# reading data from the csv files 
c=pd.read_csv(r"E:\Term 1 Bradford\Big Data Visualization\CW-2\Sunspots.csv")
flares = pd.read_csv(r"E:\Term 1 Bradford\Big Data Visualization\CW-2\flares.csv")
time = pd.read_csv(r"E:\Term 1 Bradford\Big Data Visualization\CW-2\Sunspot time.csv")
length = 271883
#print(c)


# finding total change in size for each of the sunspots
sunspot_change = {}
sunspot_number = {}
prev_sunspot = {}
length = 271883

c.NOAA = c.NOAA[:].astype(numpy.float)
c.Size = c.Size[:].astype(numpy.float)

for x in range(0,9):
    print(c.NOAA[x], "   ", c.Size[x])

for i in range(0,length):
    sunspot = c.NOAA[i]
    if math.isnan(sunspot) or math.isnan(c.Size[i]):
        continue
    if sunspot in sunspot_number:
        sunspot_number[sunspot] = sunspot_number[sunspot] + 1
        sunspot_change[sunspot] = sunspot_change[sunspot] + abs(prev_sunspot[sunspot] - c.Size[i])
        prev_sunspot[sunspot] = c.Size[i]
    else:
        prev_sunspot[sunspot] = c.Size[i]
        sunspot_number[sunspot] = 1
        sunspot_change[sunspot] = c.Size[i]


# finding number of X and M flares
flares_type_x = dict()
flares_type_m = dict()

for i in range(0,len(flares.type)):
    flare = flares.NOAA[i]
    if math.isnan(flare):
        continue
        
    if flares.type[i] == "X":
        if flare in flares_type_x:
            flares_type_x[flare] = flares_type_x[flare] + 1
        else:
            flares_type_x[flare] = 1
    elif flares.type[i] == "M":
        if flare in flares_type_m:
            flares_type_m[flare] = flares_type_m[flare] + 1
        else:
            flares_type_m[flare] = 1
            
# averaging sunspot change with total number 
for key in sunspot_number:
    prev_sunspot[key] = sunspot_change[key] // sunspot_number[key]
    print(key, prev_sunspot[key])

# sorting the list wrt to total change in size
sorted_x = sorted(prev_sunspot.items(), key=operator.itemgetter(1), reverse = True)

sorted_dict = collections.OrderedDict(sorted_x)

# calculating total number of flares for both halves
counter = 1
sum_first = 0
sum_second = 0

for key in sorted_dict:
    if key in flares_type_x:
        if counter < len(sorted_dict) // 2:
            sum_first = sum_first + flares_type_x[key]
        else:
            sum_second = sum_second + flares_type_x[key]
    
    counter = counter + 1

print("X Flares Result ", sum_first, " ", sum_second)

sum_first = 0
sum_second = 0
counter = 1

for key in sorted_dict:
    if key in flares_type_m:
        if counter < len(sorted_dict) // 2:
            sum_first = sum_first + flares_type_m[key]
        else:
            sum_second = sum_second + flares_type_m[key]
    
    counter = counter + 1

print("M Flares Result ", sum_first, " ", sum_second)

