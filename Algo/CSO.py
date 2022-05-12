from copy import deepcopy
from random import sample, choice
import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt
from tqdm import tqdm
import math
seed = 1990 #123 #1234 #69
np.random.seed(seed)
# Global variables
epoch = 500
self_pos_con = True
seek_mem_pool = 50
problem_size = 2
dim_change = 0.8
seeking_range = 0.15
c1 = 0.4
w_min = 0.4
w_max = 0.9
lower_bound = -1
upper_bound = 1
pop_size = 100
mixing_ratio = 0.15  # mixing seeking with tracing mode
function_name = 'egg_crate'


def f(solution, shift=0):
    if function_name == 'rosenbrock':
        """
        Ackley's function
        :param solution:
        :param shift:
        :return:
        """
        x = solution - shift
        dim = len(solution)
        A = 0
        B = 0
        A += -0.2 * np.sqrt(np.sum(np.square(x)) / dim)
        B += np.sum(np.cos(2 * np.pi * x)) / dim
        res = -20 * np.exp(A) - np.exp(B) + 20 + np.e
        return res

    elif function_name == 'rosenbrock':
        x = solution - shift
        res = 0
        for iter in range(len(solution) - 1):
            res += (100 * np.square(x[iter] ** 2) - x[iter + 1]) + np.square(x[iter] - 1)
        return abs(res)
        
    elif function_name == 'egg_crate':
        x = solution - shift
        return (x[0]) ** 2 + (x[1]) ** 2 + 25 * (np.sin(x[0]) ** 2 + np.sin(x[1])) ** 2
    elif function_name == "t1":
        x = solution - shift
        f = x[1]
        g = 11 + x[1]**2 - 10*np.cos(2*np.pi*x[1])
        if f <= g:
            return 1 - np.sqrt(abs(f/g))
        else:
            return 0

def seeking_mode(cat):
    candidate_cats = []
    cat_clone = [deepcopy(cat) for _ in range(seek_mem_pool)]
    if self_pos_con:
        candidate_cats.append((deepcopy(cat)))
        cat_clone = [deepcopy(cat) for _ in range(seek_mem_pool - 1)]
    for clone in cat_clone:
        index = sample(range(0, problem_size), int(dim_change * problem_size))
        for i in index:
            if uniform() >= 0.5:
                clone[0][i] -= clone[0][i] * seeking_range
            else:
                clone[0][i] += clone[0][i] * seeking_range
        clone[2] = f(clone[0])
        candidate_cats.append(clone)

    cat = sorted(candidate_cats, key=lambda cat: cat[2])[0]  # cat with best fitness

    return cat


def tracing_mode(cat, best_cat, weight):
    temp = weight * cat[1] + np.random.random() * c1 * (best_cat[0] - cat[0])
    cat[0] += np.where(temp > upper_bound, upper_bound, temp)
    return cat


def create_solution():
    """
            x: vi tri hien tai cua con meo
            v: vector van toc cua con meo (cung so chieu vs x)
            flag: trang thai cua meo, seeking hoac tracing
    """
    x = np.random.uniform(lower_bound, upper_bound, problem_size)
    v = np.random.uniform(lower_bound, upper_bound, problem_size)
    fitness = f(x)
    flag = False  # False: seeking mode , True: tracing mode
    if np.random.random() < mixing_ratio:
        flag = True
    return [x, v, fitness, flag]


def get_best_cat(cats, fitness, cat_best):
    sort_temp = sorted(cats, key=lambda temp: temp[fitness])
    return deepcopy(sort_temp[cat_best])


def solution():
    cats = [create_solution() for _ in range(pop_size)]
    best_cat = get_best_cat(cats, 2, 0)
    iteration = []
    best_value = []
    for i in tqdm(range(epoch)):
        w = ((w_max - w_min) * ((epoch - i) / epoch)) + w_min
        for q in range(pop_size):
            if not cats[q][3]:
                cats[q] = seeking_mode(cats[q])
            else:
                cats[q] = tracing_mode(cat=cats[q], best_cat=best_cat, weight=w)
        for q in range(pop_size):
            if uniform() >= mixing_ratio:
                cats[q][3] = True
            else:
                cats[q][3] = False

        current_cat_best = get_best_cat(cats, 2, 0)
        if best_cat[2] < current_cat_best[2]:
            continue
        else:
            if current_cat_best[2] >= 0:
                best_cat = current_cat_best
        iteration.append(i+1)
        best_value.append(best_cat[2])
    return iteration,best_value


