# Generate a histogram of state distribution of users.
# Some regex is used here to parse the addresses we collected from the CSV file
# and retrieve the State Abbreviation. Thanks @John Ring.
adrs = []
REGEX = re.compile(',\s([A-Z]{2})\s(\d{5})')
for adr in addresses:
    adr = re.search(REGEX,adr)
    if adr != None:
        adrs.append(adr.group()[2:4]) 
# Plot the States as a Descending Order bar-graph.
# Tyler J. Sawyer
# Now, count the number of times a state appears and sort them based on their count value in DESCENDING order.
addressesCounted = [(i, adrs.count(i)) for i in set(adrs)]
addressesCounted.sort(key=lambda x: x[1], reverse=True)
# Unzip these values into two lists - labels and values.
labels,values = zip(*addressesCounted)
# Generate the indexes of our graph using the numpy arange method.
indexes = np.arange(len(addressesCounted))
# Width of 1.0 to make the graph display nicely.
width=1.0
# Plot our graph!
plt.bar(indexes, values, width)
# Note our x-labels are rotated for readability.
plt.xticks(indexes+width * 0.5, labels, rotation=90)
# General axis labels
plt.xlabel("State")
plt.ylabel("Number of Users")
plt.title("Number of Users by State")
# This helps fill the graph window a bit more.
plt.margins(0.02, 0)
# Sizing
plt.gcf().set_size_inches(12.0,8.0)