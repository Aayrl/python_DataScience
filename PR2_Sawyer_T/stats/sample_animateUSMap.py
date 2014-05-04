# Sample GeoMap Animation Script
# Uses JSAnimation Library : https://github.com/jakevdp/JSAnimation
# Original code by Tyler J. Sawyer - 5/4/14
# You will need to tweak it for your liking, but the
# general idea should be fairly obvious and straight forward.

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from JSAnimation import IPython_display

listOfPopulationDicts = [population1960,population1970,population1980,
                         population1990,population2000,population2010]

state2LatLong = [['Alabama',32.7990,-86.8073],
['Alaska',47.1700,-128.5708],
['Arkansas',34.9513,-92.3809],
['Arizona',33.7712,-111.3877],
['California',36.1700,-119.7462],
['Colorado',39.0646,-105.3272],
['Connecticut',41.5834,-72.7622],
['Delaware',39.3498,-75.5148],
['District of Columbia',38.8964,-77.0262],
['Florida',27.8333,-81.7170],
['Georgia',32.9866,-83.6487],
['Hawaii',30.1700,-120.6475],
['Idaho',44.2394,-114.5103],
['Illinois',40.3363,-89.0022],
['Indiana',39.8647,-86.2604],
['Iowa',42.0046,-93.2140],
['Kansas',38.5111,-96.8005],
['Kentucky',37.6690,-84.6514],
['Louisiana',31.1801,-91.8749],
['Massachusetts',42.2373,-71.5314],
['Maryland',39.0724,-76.7902],
['Maine',44.6074,-69.3977],
['Michigan',43.3504,-84.5603],
['Minnesota',45.7326,-93.9196],
['Missouri',38.4623,-92.3020],
['Mississippi',32.7673,-89.6812],
['Montana',46.9048,-110.3261],
['North Carolina',35.6411,-79.8431],
['North Dakota',47.5362,-99.7930],
['Nebraska',41.1289,-98.2883],
['New Hampshire',43.4108,-71.5653],
['New Jersey',40.3140,-74.5089],
['New Mexico',34.8375,-106.2371],
['Nevada',38.4199,-117.1219],
['New York',42.1497,-74.9384],
['Ohio',40.3736,-82.7755],
['Oklahoma',35.5376,-96.9247],
['Oregon',44.5672,-122.1269],
['Pennsylvania',40.5773,-77.2640],
['Rhode Island',41.6772,-71.5101],
['South Carolina',33.8191,-80.9066],
['South Dakota',44.2853,-99.4632],
['Tennessee',35.7449,-86.7489],
['Texas',31.1060,-97.6475],
['Utah',40.1135,-111.8535],
['Virginia',37.7680,-78.2057],
['Vermont',44.0407,-72.7093],
['Washington',47.3917,-121.5708],
['Wisconsin',44.2563,-89.6385],
['West Virginia',38.4680,-80.9696],
['Wyoming',42.7475,-107.2085]]

def heatmapAnimate(listOfDataDictionaries,title,startyear,stepsize,frames=6, interval=1000):
    # Lambert Conformal map of USA lower 48 states
    geoMap = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,
    urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45,
    lon_0=-95, resolution='i', area_thresh=10000)
    # Uses a Shape File from the US Census Bureau
    # http://www2.census.gov/geo/tiger/GENZ2010/
    shapeInfo = geoMap.readshapefile('data/shape_files/gz_2010_us_040_00_500k','states',drawbounds=False)
    # Draw the coastlines of continental area
    geoMap.drawcoastlines()
    # Draw country boundaries
    geoMap.drawcountries(linewidth=2)
    # Draw states boundaries (America only)
    geoMap.drawstates(linewidth=1)
    # Fill the background (the oceans)
    geoMap.drawmapboundary(fill_color='aqua')
    # Fill the continental area
    geoMap.fillcontinents(color='#70B870',lake_color='aqua')

    # Bound our map to the continental US.
    # otherwise, we'll have some weird display issues
    # with Alaska and Hawaii.
    geoMap.drawparallels(np.arange(25,65,20),labels=[0,0,0,0],zorder=-1,color="w")
    geoMap.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,0],zorder=-1,color="w")
    
    # Add a Legend to the Animation
    colorLegend = Rectangle((0, 0), 1, 1, fc="#0000ff")
    legend([colorLegend],["Population (1 Radius = 250,000 people)"])
    
    # Adjust size of image
    plt.gcf().set_size_inches(12.0,8.0)
    plt.gca().axis("off")
    # Add Title and show.
    plt.title(title,fontsize=25)
    
    points = []
    pointData = []
    
    textx, texty = geoMap(-89,26.5)
    yearTitle = plt.text(textx,texty,"Year: "+str(startyear),fontsize=20,ha='center',va='top',color='r')
    
    def init():
        
        # Grab the initial year information and plot these circles
        # in the appropriate location on the map.
        dataDictionary = listOfDataDictionaries[0]
        for i in range(len(state2LatLong)):
            name = state2LatLong[i][0]
            x, y = geoMap(state2LatLong[i][2],state2LatLong[i][1])
            pointData.append(name)
            points.append(geoMap.plot(x,y,'bo',markersize=(25),alpha=0.50)[0])
            
        yearTitle.set_text("Year: "+str(startyear))
        
        return points, yearTitle,
    
    # Animation Function
    def animate(t):
        # For each 'step' in the animation, increment the year
        # and update the points on the plot.
        dataDictionary = listOfDataDictionaries[t]
        year = startyear + stepsize*t
        
        yearTitle.set_text("Year: "+str(year))

        j = 0
        for pt in points:
            name = pointData[j]
            population = dataDictionary[name]
            pt.set_markersize(int(population)/250.0)
            j = j + 1
            
        return points, yearTitle,

    
    # "Run" The animation function.
    return animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                                   frames=frames, interval=interval, blit=True)


heatmapAnimate(listOfPopulationDicts,"US Population - 1960 to 2010",1960,10)