from numpy import random

def randomArrayGenerator(lower_bound, upper_bound, size):
    return random.uniform(lower_bound, upper_bound, size)
