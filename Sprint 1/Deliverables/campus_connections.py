"""
Theodore Preaus CMS-380

Campus connections 

Use the data to find the mean and median class sizes.

Find how many unique students does each Rollins student interact 
with in classes
"""

# Standard matplotlib import
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv


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


# Create an empty dictionary to record which students are in each course
students_per_course = {}
courses_per_student = {}

# Open the file and create a csv reader
f = open('enrollments.csv', 'rU')
reader = csv.reader(f)
reader_two = csv.reader(f)

# Reader automatically iterates through the lines in the file
for line in reader:
    
    # csv reader automatically turns the line into a list of fields
    student_id = line[0]
    course_id = line[1]
    
    if course_id not in students_per_course:
        students_per_course[course_id] = []
        
    students_per_course[course_id].append(student_id)
  
    if student_id not in courses_per_student:
        courses_per_student[student_id] = []
        
    courses_per_student[student_id].append(course_id)



    
# Here's an example of how to iterate through the keys in a dictionary
# Print the students in each course

num_in_class = []

for course_id in students_per_course:
    student_list = students_per_course[course_id]
    num = 0
    for student in student_list:
      num += 1
    
    num_in_class.append(num)
      

mean = calc_mean(num_in_class)
median = calc_median(num_in_class)

print("Mean: ", mean)
print("Median: ", median)
# Create a new figure -- you must do this before calling a plotting function
plt.figure()

# Create a histogram with 15 bins
plt.hist(num_in_class, 20)


plt.title('Campus Connections Histogram')
plt.xlabel('Class Size')
plt.ylabel('Num of Classes')


plt.savefig('campus_conections_hist.png', bbox_inches='tight')

plt.figure()

plt.boxplot(num_in_class)

plt.title('Campus Connections Box Plot')
plt.ylabel('Class Size')

plt.savefig('campus_conections_box.png', bbox_inches='tight')


num_of_same = []
# Get the key for the list of courses 
for student in courses_per_student:
  unique_id = []
  unique_id.append(student)
  # Get the course number and find the # of unique id
  for course_num in courses_per_student[student]:
    for other_student in students_per_course[course_num]:
      if other_student not in unique_id:
        unique_id.append(other_student)
  
    num_of_same.append(len(unique_id) - 1)

mean_conec = calc_mean(num_of_same)
print("Mean connections: ", mean_conec)

plt.figure()

# Create a histogram with 15 bins
plt.hist(num_of_same, 20)


plt.title('Unique Connections Histogram')
plt.xlabel('Num of Unique Connections')
plt.ylabel('Occurance')


plt.savefig('unique_conections_hist.png', bbox_inches='tight')

plt.figure()

plt.boxplot(num_of_same)

plt.title('Unique Connections Box Plot')
plt.ylabel('Unique Connections')

plt.savefig('unique_conections_box.png', bbox_inches='tight')
