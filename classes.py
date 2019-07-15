import math
import time
import numpy as npy

from functions import f1, f2, f3


class Agent:
    def __init__(self, f, x):
        self.f = f
        self.x = x

    def initialize(self, inf_lim, sup_lim):
        npy.random.seed()
        for i, sol in enumerate(self.x):
            self.x[i] = npy.random.uniform(inf_lim, sup_lim)

    def print_agent(self):
        print("f =", self.f)
        for sol in self.x:
            print(sol, end=' ')
        print()


class Population:
    def __init__(self, agents):
        self.agents = agents

    def initialize(self, inf_lim, sup_lim):
        for i, a in enumerate(self.agents):
            self.agents[i].initialize(inf_lim, sup_lim)

    def evaluate(self, numFuncion):
        if numFuncion == 1:
            for agent in self.agents:
                f1(agent)
        elif numFuncion == 2:
            for agent in self.agents:
                f2(agent)
        else:
            for agent in self.agents:
                f3(agent)

    def get_best(self):
        idx = -1
        minimum = float("inf")
        for i, agent in enumerate(self.agents):
            if agent.f < minimum:
                minimum = agent.f
                idx = i
        assert idx > -1
        return self.agents[idx]

    def create_new_population(self, agent, start, end, r1):
        new_population = Population(
            [Agent(0, [0]*len(self.agents[0].x))]*len(self.agents)
        )
        for i, agent in enumerate(new_population.agents):
            r4 = npy.random.uniform(0, 1)
            t1 = npy.random.uniform(0, 1)
            t2 = npy.random.uniform(0, 1)
            r2 = 2 * math.pi * t1
            r3 = 2 * t2
            for j, x in enumerate(agent.x):
                if r4 < 0.5:
                    agent.x[j] = self.agents[i].x[j] + r1 * \
                        math.sin(r2) * \
                        abs(r3 * agent.x[j] - self.agents[i].x[j])
                else:
                    agent.x[j] = self.agents[i].x[j] + r1 * \
                        math.cos(r2) * \
                        abs(r3 * agent.x[j] - self.agents[i].x[j])
                if(start < x < end):
                    agent.x[j] = max(min(x, end), start)
        return new_population

    def update_population(self, population):
        return Population(self.agents + population.agents)

    def print_population(self):
        for a in self.agents:
            a.print_agent()
        print()
