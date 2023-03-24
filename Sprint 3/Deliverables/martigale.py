"""
Theodore Preaus CMS-380

Simulate the Martingale betting strategy in roulette
"""

import random
import matplotlib.pyplot as plt


def simulate_bankroll(starting_bankroll, num_spins):
  bankroll = starting_bankroll
  bet_size = 1
  outcomes = []
  for _ in range(num_spins):
    # Place bet on black
    if random.random() < 18 / 38:
      # Win
      bankroll += bet_size
      bet_size = 1
    else:
      # Lose
      bankroll -= bet_size
      bet_size *= 2
    outcomes.append(bankroll)
    if bankroll < 1:
      # Bankroll bankrupt
      break
  return outcomes


num_sessions = 1000
starting_bankroll = 255
num_spins = 100

results = []
for _ in range(num_sessions):
  final_bankroll = simulate_bankroll(starting_bankroll, num_spins)[-1]
  results.append(final_bankroll)

plt.hist(results, bins=range(-255, 500, 10))
plt.xlabel('Final bankroll')
plt.ylabel('Frequency')
plt.title("Average ending Bankroll")
plt.savefig("Martingale.pdf")
