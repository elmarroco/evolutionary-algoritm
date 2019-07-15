from sys import argv
import numpy as npy
import time
from random import seed

# Local imports
from classes import Agent, Population

# Input data from arguments
gmax = int(argv[1])
n_population = int(argv[2])
n_agent = int(argv[3])
upper_bound = float(argv[4])
lower_bound = float(argv[5])
num_funcion = int(argv[6])
P = Population([Agent(0, [0] * n_agent)] * n_population)
P.initialize(upper_bound, lower_bound)
P.print_population()
P.evaluate(num_funcion)

for t in range(1, 30 + 1):
    print(f'Iteracion {t}')
    b = P.get_best()
    b.print_agent()
    r1 = 2 - (2 * t / gmax)
    Q = P.create_new_population(b, upper_bound, lower_bound, r1)
    Q.evaluate(num_funcion)
    P = P.update_population(Q)
    P.agents.sort(key=lambda agent: agent.f)
    P.agents = P.agents[0:n_population]
