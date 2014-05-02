# For anyone that needs a map of Vermont .. ~Tyler J. Sawyer
from mpl_toolkits.basemap import Basemap # For GeoPlotting.
import matplotlib.pyplot as plt

# Lambert Conformal map of Vermont
# LL: 42.611417, -73.672795
# UR: 45.086798, -71.244816
# Center: 43.8491075, -72.4588055
geoMap = Basemap(llcrnrlon=-73.672795, llcrnrlat=42.611417, urcrnrlon=-71.244816,
urcrnrlat=45.086798, projection='lcc', lat_0=43.8491075, lon_0=-72.4588055,
resolution='i', area_thresh=100)
# Draw the coastlines of continental area
geoMap.drawcoastlines()
# Draw country boundaries
geoMap.drawcountries(linewidth=2)
# Draw states boundaries (America only)
geoMap.drawstates(linewidth=2)
# Draw State county Boundaries
geoMap.drawcounties(linewidth=1)
# Fill the background (the oceans)
geoMap.drawmapboundary(fill_color='aqua')
# Fill the continental area
geoMap.fillcontinents(color='#70B870',lake_color='aqua')

# For Loop to add user locations.
state2LatLong = [['VT',44.0407,-72.7093]]

for i in range(len(state2LatLong)):
    # Get the x,y coordinate for the geoplot. For whatever reason, it's Long / Lat instead
    # of the standard Lat / Long.
    x, y = geoMap(state2LatLong[i][2],state2LatLong[i][1])
    plt.plot(x,y,'ro')
    plt.text(x+10000,y+10000,state2LatLong[i][0], bbox=dict(facecolor='yellow',alpha=0.5))

# Adjust size of image
plt.gcf().set_size_inches(12.0,8.0)
# Add Title and show.
plt.title("Map of Vermont")
plt.show()
