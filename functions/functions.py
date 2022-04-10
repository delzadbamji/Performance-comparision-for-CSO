import math

def rosenbrock(x):
    '''
    rosenbrock function to compute cost
    :param x: vector <List>
    :return: cost value <number>
    '''
    index = 0
    total_cost = math.pow((x[0][index] - 1),2) + 100 * math.pow((x[0][index+1] - math.pow(x[0][index],2)),2)
    return total_cost


def Ackley(x, D):
    '''
    Ackley function for cost computation
    :param x: vector <List>
    :return: cost value <number>
    '''
    x_sq = 0
    forPartB = 0
    for i in range(len(x[0])):
        x_sq += x[0][i] * x[0][i]
        forPartB += math.cos(2*math.pi* x[0][i] )
    partOne =  -20.0 * math.exp(-0.02 * ( math.pow( (x_sq / D), 0.5) ))
    partTwo = math.exp( forPartB / D)
    return partOne - partTwo + 20.0 + math.e
