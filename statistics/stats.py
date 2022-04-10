def computeStatistics(trials):
    '''
    In this function we take a list of all the 30 trial values and compute its mean and standard deviation.
    :param trials: List
    :return: Float,Float
    '''
    mean = np.mean(trials)
    std = np.std(trials)
    return mean,std
