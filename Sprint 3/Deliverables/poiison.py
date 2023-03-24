"""
Theodore Preaus CMS-380

Show the connection between the Poiison and Binomial distribution

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def simulate_binomial_process():
  # Set number of trials and probability of success
  num_trials = 1000
  success_prob = 0.025

  # Simulate the binomial process
  binomial_outcomes = np.random.binomial(num_trials, success_prob, size=1000)

  # Count the number of outcomes for each possible number of successes
  success_counts = np.bincount(binomial_outcomes)

  # Calculate the fraction of trials that resulted in each outcome
  success_fractions = success_counts / 1000

  # Generate x-values for the Poisson pmf
  x_values = np.arange(0, 1001)

  # Calculate Poisson pmf with mean = 25
  poisson_pmf = poisson.pmf(x_values, mu=25)

  # Plot a bar chart of the binomial fractions and the Poisson pmf
  plt.bar(range(len(success_fractions)), success_fractions, label="Binomial")
  plt.plot(x_values, poisson_pmf, 'r-', label="Poisson")

  # Set x-axis limits to zoom in on part around 25
  plt.xlim([0, 75])

  # Add axis labels and title to the plot
  plt.xlabel("Number of Successes")
  plt.ylabel("Fraction of Trials / Probability")
  plt.title("Simulated Binomial Process and Poisson PMF")

  # Add a legend to the plot
  plt.legend()
  # Save the plot as a PDF file with a tight bounding box
  plt.savefig('binomial_and_poisson_simulation.pdf', bbox_inches="tight")


simulate_binomial_process()
