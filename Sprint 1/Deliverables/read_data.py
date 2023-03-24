"""
Theodore Preaus CMS-380

Work with data.txt file

Practice opeing and looping through a file 
"""
import math
# add mediean, quarltile, standered Deviation

def calc_mean(values):
  """
  Calculate the mean of a list of float
  """
  return sum(values) / len(values)

def calc_median(values):
  values.sort()
  length = len(values)
  mid = length // 2
  if length % 2 == 0:
    num_one = values[mid]
    num_two = values[mid + 1]
    return (num_one + num_two) / 2
  else:
    return values[mid + 1]


def calc_variance(values):
  mean = calc_mean(values)
  sum = 0
  for num in values:
    variance = (num - mean) * (num - mean)
    sum += variance
  return sum / len(values)


def calc_std_dev(values):
  mean = calc_mean(values)
  sum = 0
  for num in values:
    variance = (num - mean) * (num - mean)
    sum += variance
  return math.sqrt(sum / len(values))
#To open a file use open

f = open('data.txt', 'r')

# make a list 
#
# List v array
#
# arrays are fixed size and single type 
#
# list can be mixed and dynamicly resizable

data = []

for line in f:
  data.append(float(line))

data_mean = calc_mean(data)
print("Mean: ", data_mean)
data_median = calc_median(data)
print ("Median: ", data_median)
data_variance = calc_variance(data)
print ("Variance: ", data_variance)
data_std_diviation = calc_std_dev(data)
print ("Standed div: ", data_std_diviation) 


# Import matplotlib and configure it to save files in the web IDE
#
# These three lines should be at the start of any script that uses matplotlib on Mimir
import matplotlib
matplotlib.use('Agg')  # <-- Required if you're using matplotilb in Mimir, see below
from matplotlib import pyplot as plt

# Example data

# Create a new figure -- you must do this before calling a plotting function
plt.figure()

# Create a histogram with 15 bins
plt.hist(data, 20)

# Title and axis labels
plt.title('More Calculation Histogram')
plt.xlabel('Data value')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('more_calculation_hist.pdf', bbox_inches='tight')


plt.figure()

plt.boxplot(data)

plt.savefig('more_calculation_box.pdf', bbox_inches='tight')
