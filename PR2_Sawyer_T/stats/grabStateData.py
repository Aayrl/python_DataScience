import csv
import datetime

# Pull our state population data from our CSV into a list of dictionaries.
openFile = open("data/State-Population.csv", 'r')
listOfStates = []

# Iterate through the csv file and save all data to our dict.
# Then, we'll add this dict to our list of dictionaries.
csvData = csv.DictReader(openFile)
for row in csvData:
    stateInformation = {}
    stateInformation['State']=row['State']
    stateInformation['1960 Population']=row['1960_Population']
    stateInformation['1970 Population']=row['1970_Population']
    stateInformation['1980 Population']=row['1980_Population']
    stateInformation['1990 Population']=row['1990_Population']
    stateInformation['2000 Population']=row['2000_Population']
    stateInformation['2010 Population']=row['2010_Population']
    stateInformation['1960-1970 Change']=row['%Change_1960-1970']
    stateInformation['1970-1980 Change']=row['%Change_1970-1980']
    stateInformation['1980-1990 Change']=row['%Change_1980-1990']
    stateInformation['1990-2000 Change']=row['%Change_1990-2000']
    stateInformation['2000-2010 Change']=row['%Change_2000-2010']
    stateInformation['1960 Density']=row['PopSqMile_1960']
    stateInformation['1970 Density']=row['PopSqMile_1970']
    stateInformation['1980 Density']=row['PopSqMile_1980']
    stateInformation['1990 Density']=row['PopSqMile_1990']
    stateInformation['2000 Density']=row['PopSqMile_2000']
    stateInformation['2010 Density']=row['PopSqMile_2010']
    listOfStates.append(stateInformation)
openFile.close()

print listOfStates
