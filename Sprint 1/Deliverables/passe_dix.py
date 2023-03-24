"""
Theodore Preaus CMS-380

Write a sim to estimate the prob of winning at 
passe dix

Roll 3 6 sided dice 
Player wins if the sum is > 10 
"""

# Basic Stratagy: Write a simulate() method that plays 1 round 
# and returns True if player wins or False if player loses


from random import randint

def simulate():
  """
  Simulate one round of passe dix
  """
  die_one = randint(1, 6)
  die_two = randint(1, 6)
  die_three = randint(1, 6)
  total = die_one + die_two + die_three

  return total > 10

### Main 

num_trials = 1000
num_wins = 0

# Call simulate in a loop

for trial in range(num_trials):
  if simulate():
    num_wins += 1
  
frac_wins = num_wins / num_trials

print('%.4f' % frac_wins)
