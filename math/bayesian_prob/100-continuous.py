#!/usr/bin/env python3

"""

Calculate the posterior probability that the probability of developing severe 
side effects is within the range [p1, p2]

"""

import numpy as np

from scipy import special

def posterior(x, n, p1, p2):

    # Validate inputs
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer >= 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not all(isinstance(p, float) and 0 <= p <= 1 for p in [p1, p2]):
        raise ValueError("p1 and p2 must be floats in [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    # Beta distribution parameters
    alpha, beta = x + 1, n - x + 1

    # Calculate the posterior probability
    return special.beta.cdf(p2, alpha, beta) - special.beta.cdf(p1, alpha, beta)

