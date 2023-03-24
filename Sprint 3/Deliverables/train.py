"""
Theodore Preaus CMS-380

Simulate the odds the 100th passanger sits in there assigned seat
"""

import random

def simulate():

  # Initialize a list of empty seats
  seats = [0] * 100
  # Assign seat 1 to passenger 1
  seats[0] = 1
  # Loop through passengers 2 to 100
  for i in range(2, 101):
    assigned_seat = i - 1
    if seats[assigned_seat - 1] == 0:  # If assigned seat is unoccupied
      seats[assigned_seat - 1] = i
    else:  # If assigned seat is occupied, find another unoccupied seat
      unoccupied_seats = []
      for j in range(100):
        if seats[j] == 0:
          unoccupied_seats.append(j)
      chosen_seat = random.choice(unoccupied_seats)
      seats[chosen_seat] = i
  # Check if passenger 100 sits in her assigned seat
  if seats[99] == 100:
    return True
  else:
    return False


# Run the simulation for a large number of trials (100,000 in this case)
num_trials = 1000
num_successes = 0
for i in range(num_trials):
  if simulate():
    num_successes += 1

# Calculate the estimated probability that the 100th passenger gets her assigned seat
probability = num_successes / num_trials

# Print the estimated probability
print(
  "Probability that passenger 100 gets to sit in her originally assigned seat:",
  probability)
