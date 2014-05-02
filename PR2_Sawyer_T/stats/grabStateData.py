import csv

# Pull our state population data from our CSV into a list of dictionaries.
openFile = open("data/State-Population.csv", 'r')
listOfStates = []

# Iterate through the csv file and save all data to our dict.
# Then, we'll add this dict to our list of dictionaries.
csvData = csv.DictReader(openFile)
for row in csvData:
    stateInformation = {}
    # Clean our State Name information
    stateInformation['State']=row['State'].replace("_", " ")[:-1]
    # Slap Population Info into our Dictionary.
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


# Attempt to get a US map showing up.
from mpl_toolkits.basemap import Basemap # For GeoPlotting locations of users
import matplotlib.pyplot as plt
import numpy as np
# For adding heat map to the US Map.
from matplotlib.colors import rgb2hex

# Grab all of the population info.
population1960 = {}
population1970 = {}
population1980 = {}
population1990 = {}
population2000 = {}
population2010 = {}
for state in listOfStates:
    population1960[state['State']]=state['1960 Population']
    population1970[state['State']]=state['1970 Population']
    population1980[state['State']]=state['1980 Population']
    population1990[state['State']]=state['1990 Population']
    population2000[state['State']]=state['2000 Population']
    population2010[state['State']]=state['2010 Population']

def buildHeatmap(dataDictionary,title,bartitle,barcolor,barmin,barmax):
    # Lambert Conformal map of USA lower 48 states
    geoMap = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,
    urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45,
    lon_0=-95, resolution='i', area_thresh=10000)
    # Uses a Shape File from the US Census Bureau
    # http://www2.census.gov/geo/tiger/GENZ2010/
    shapeInfo = geoMap.readshapefile('data/shape_files/gz_2010_us_040_00_500k','states',drawbounds=False)
    
    # Process based off an example from our professor's lecture slides,
    # James Bagrow - UVM Spring 2014
    # http://bagrow.com/dsv/
    # I took the base idea and modified it heavily for the needs 
    # of this project.
    # Color each state based on Population
    colors={}
    statenames=[]
    # Use the Green color map.
    # Others may be found here : http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
    colorMap = barcolor
    heatmapMinAmt = barmin; heatmapMaxAmt = barmax # Range for Heatmap (Valuewise)
    scalarMapping = plt.cm.ScalarMappable(cmap=colorMap,norm=plt.normalize(vmin=heatmapMinAmt, vmax=heatmapMaxAmt))
    
    for shapedict in geoMap.states_info:
        statename = shapedict['NAME']
        # Grab population info for each state
        try:
            population = float(dataDictionary[statename])
        except KeyError:
            population = 0.0
            
        # Define the color for this state.
        # Population / Max Color Amt.
        colors[statename] = colorMap((population-heatmapMinAmt)/(heatmapMaxAmt-heatmapMinAmt))
        statenames.append(statename)
    
    # Actually color each state in this structure.
    for nshape, seg in enumerate(geoMap.states):
        xx, yy = zip(*seg)
        color = rgb2hex(colors[statenames[nshape]]) 
        plt.fill(xx,yy,color,edgecolor=color)
    
    # Bound our map to the continental US.
    # otherwise, we'll have some weird display issues
    # with Alaska and Hawaii.
    geoMap.drawparallels(np.arange(25,65,20),labels=[0,0,0,0],zorder=-1,color="w")
    geoMap.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,0],zorder=-1,color="w")
    
    # Build the Color Bar at the bottom of the graph
    mm = plt.cm.ScalarMappable(cmap=colorMap)
    mm.set_array([heatmapMinAmt,heatmapMaxAmt])
    plt.colorbar(mm, label=bartitle,ticks=[0,5000,10000,15000,20000,25000],
    orientation="horizontal",fraction=0.05)
                
    # Adjust size of image
    plt.gcf().set_size_inches(12.0,8.0)
    plt.gca().axis("off")
    # Add Title and show.
    plt.title(title)
    plt.show()
    
buildHeatmap(population1960,"US Population - 1960","Population (1,000)",plt.cm.BuGn_r,0,25000)
buildHeatmap(population1970,"US Population - 1970","Population (1,000)",plt.cm.BuGn_r,0,25000)
buildHeatmap(population1980,"US Population - 1980","Population (1,000)",plt.cm.BuGn_r,0,25000)
buildHeatmap(population1990,"US Population - 1990","Population (1,000)",plt.cm.BuGn_r,0,25000)