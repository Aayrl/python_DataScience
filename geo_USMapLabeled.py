from mpl_toolkits.basemap import Basemap # For GeoPlotting locations of users
import numpy as np # For GeoPlotting locations of users
import re # For GeoPlotting user locations.

# GEOPLOT
# TYLER J. SAWYER - 2/10/14
# Updated: 16:20 on May 01, 2014 (Thursday)
# Thanks : http://www.packtpub.com/article/plotting-geographical-data-using-basemap

# Lambert Conformal map of USA lower 48 states
geoMap = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,
urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45,
lon_0=-95, resolution='i', area_thresh=10000)
# Draw the coastlines of continental area
geoMap.drawcoastlines()
# Draw country boundaries
geoMap.drawcountries(linewidth=2)
# Draw states boundaries (America only)
geoMap.drawstates()
# Fill the background (the oceans)
geoMap.drawmapboundary(fill_color='aqua')
# Fill the continental area
geoMap.fillcontinents(color='white',lake_color='aqua')

# For Loop to add state labels
state2LatLong = [['AK',47.1700,-128.5708],
['AL',32.7990,-86.8073],
['AR',34.9513,-92.3809],
['AZ',33.7712,-111.3877],
['CA',36.1700,-119.7462],
['CO',39.0646,-105.3272],
['CT',41.5834,-72.7622],
['DC',38.8964,-77.0262],
['DE',39.3498,-75.5148],
['FL',27.8333,-81.7170],
['GA',32.9866,-83.6487],
['HI',30.1700,-120.6475],
['IA',42.0046,-93.2140],
['ID',44.2394,-114.5103],
['IL',40.3363,-89.0022],
['IN',39.8647,-86.2604],
['KS',38.5111,-96.8005],
['KY',37.6690,-84.6514],
['LA',31.1801,-91.8749],
['MA',42.2373,-71.5314],
['MD',39.0724,-76.7902],
['ME',44.6074,-69.3977],
['MI',43.3504,-84.5603],
['MN',45.7326,-93.9196],
['MO',38.4623,-92.3020],
['MS',32.7673,-89.6812],
['MT',46.9048,-110.3261],
['NC',35.6411,-79.8431],
['ND',47.5362,-99.7930],
['NE',41.1289,-98.2883],
['NH',43.4108,-71.5653],
['NJ',40.3140,-74.5089],
['NM',34.8375,-106.2371],
['NV',38.4199,-117.1219],
['NY',42.1497,-74.9384],
['OH',40.3736,-82.7755],
['OK',35.5376,-96.9247],
['OR',44.5672,-122.1269],
['PA',40.5773,-77.2640],
['RI',41.6772,-71.5101],
['SC',33.8191,-80.9066],
['SD',44.2853,-99.4632],
['TN',35.7449,-86.7489],
['TX',31.1060,-97.6475],
['UT',40.1135,-111.8535],
['VA',37.7680,-78.2057],
['VT',44.0407,-72.7093],
['WA',47.3917,-121.5708],
['WI',44.2563,-89.6385],
['WV',38.4680,-80.9696],
['WY',42.7475,-107.2085]]

for i in range(len(state2LatLong)):
    # Get the x,y coordinate for the geoplot. Note: It's Long / Lat.
    x, y = geoMap(state2LatLong[i][2],state2LatLong[i][1])
    geoMap.plot(x,y,'ro')
    geoMap.text(x+10000,y+10000,state2LatLong[i][0], bbox=dict(facecolor='yellow',alpha=0.5))
    

# Adjust size of image
geoMap.gcf().set_size_inches(12.0,8.0)
# Add Title and show.
geoMap.title("Location Distribution of Users")
geoMap.show()