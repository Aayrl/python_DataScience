import csv

# Pull our state population data from our CSV into a list of dictionaries.
openFile = open("data/unemployment_by_state.csv", 'r')
stateUnemploymentLists = []

# Iterate through the csv file and save all data to our dict.
# Then, we'll add this dict to our list of dictionaries.
csvData = csv.DictReader(openFile)
for row in csvData:
    stateInformation = {}
    # Clean our State Name information
    stateInformation['State']=row['State'].replace("_", " ")
    # Place Unemployment Rates into Dictionary
    stateInformation['1980 Unemployment']=row['1980']
    stateInformation['1990 Unemployment']=row['1990']
    stateInformation['2000 Unemployment']=row['2000']
    stateInformation['2001 Unemployment']=row['2001']
    stateInformation['2002 Unemployment']=row['2002']
    stateInformation['2003 Unemployment']=row['2003']
    stateInformation['2004 Unemployment']=row['2004']
    stateInformation['2005 Unemployment']=row['2005']
    stateInformation['2006 Unemployment']=row['2006']
    stateInformation['2007 Unemployment']=row['2007']
    stateInformation['2008 Unemployment']=row['2008']
    stateInformation['2009 Unemployment']=row['2009']
    stateInformation['2010 Unemployment']=row['2010']
    stateUnemploymentLists.append(stateInformation)
openFile.close()

print stateUnemploymentLists
