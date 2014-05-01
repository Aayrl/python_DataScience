import collections 
import matplotlib, matplotlib.pyplot as plt

ageList = [d for d in ageList if 10 < d < 80]

ageCounts = collections.Counter(ageList)

ageCountsSorted = sorted(ageCounts.items())

ageValue, countValue = zip(*ageCountsSorted)

# The next few lines build a histogram of the age distribution
ageHistFigure = plt.figure(1)
plt.hist(ageList, bins = 30)
plt.xlabel("age")
plt.ylabel("number of people")
plt.gcf().set_size_inches(9.0, 6.0)
