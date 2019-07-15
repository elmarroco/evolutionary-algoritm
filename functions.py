import math


def f1(agent):
    agent.f = 0
    for x in agent.x:
        agent.f += pow(x - math.pi, 2)


def f2(agent):
    agent.f = 0
    for i, x in enumerate(agent.x):
        for j in range(0, i):
            agent.f += pow(x - math.pi, 2)


def f3(agent):
    agent.f = 0
    for i, x in enumerate(agent.x):
        agent.f += 100 * pow(agent.x[i+1] - pow(x, 2), 2) + pow(1 - x, 2)
