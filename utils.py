import numpy as np
import math

# def ackley(solution,shift=0):
#     """
#     Ackley's function
#     :param solution:
#     :param shift:
#     :return:
#     """
#     x = solution - shift
#     dim = len(solution)
#     A = 0
#     B = 0
#     A += -0.2 * np.sqrt(np.sum(np.square(x)) / dim)
#     B += np.sum(np.cos(2 * np.pi * x)) / dim
#     res = -20 * np.exp(A) - np.exp(B) + 20 + np.e
#     return res


def ackley(x,D=10):
    '''
    Ackley function for cost computation
    :param x: vector
    :return: cost value
    '''
    x_sq = 0
    forPartB = 0

    for i in range(len(x[0])):
        x_sq += x[0][i] * x[0][i]
        forPartB += math.cos(2*math.pi* x[0][i] )
    partOne =  -20.0 * math.exp(-0.02 * ( math.pow( (x_sq / D), 0.5) ))
    partTwo = math.exp( forPartB / D)
    return partOne - partTwo + 20.0 + math.e

def four_peak(x):
    '''
    4 peak objective function
    :param x: List[List[float]]
    :return: int
    '''
    x1, x2 = x[0]
    power1 = -1 * ((x1 - 4) ** 2 + (x2 - 4) ** 2)
    power2 = -1 * ((x1 + 4) ** 2 + (x2 - 4) ** 2)
    power3 = -1 * (x1 ** 2 + x2 ** 2)
    power4 = -1 * (x1 ** 2 + (x2 + 4) ** 2)
    return math.exp(power1) + math.exp(power2) + 2 * (math.exp(power3) + math.exp(power4))

def egg_crate(x):
    '''
        egg crate objective function
        :param x: List[List[float]]
        :return: int
        '''
    x1,x2 = x[0]
    return x1**2 + x2**2 + 25 * ((math.sin(x1))**2 + (math.sin(x2))**2)

def rosenbrock(x):  # returns a scalar
    '''
    rosenbrock function to compute cost
    :param x: vector
    :return: cost value <number>
    '''
    index = 0
    total_cost = math.pow((x[0][index] - 1), 2) + 100 * math.pow((x[0][index + 1] - math.pow(x[0][index], 2)), 2)
    return total_cost
