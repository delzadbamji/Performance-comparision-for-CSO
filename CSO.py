from copy import deepcopy
from random import sample, choice
import numpy as np
from numpy.random import uniform

from utils import ackley as f
# from utils import egg_crate as f

"""
#########################################
Cat Swarm Optimization

@author Anuj K
@author Delzad Bamji
#########################################
"""

# hyperparameters
epoch = 50
self_pos_con = True
seek_mem_pool = 50
problem_size = 10
dim_change = 0.8
seeking_range = 0.15
c1 = 0.4
w_min = 0.4
w_max = 0.9
lower_bound = -1
upper_bound = 1
pop_size = 100
mixing_ratio = 0.15     #mixing seeking with tracing mode

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
                print("clone:",clone[0][i])
                print("see", seeking_range)
                clone[0][i] -= clone[0][i] * seeking_range
            else:
                clone[0][i] += clone[0][i] * seeking_range
        print("clone",f(clone[0]))
        clone[2] = f([clone[0]])
        candidate_cats.append(clone)

    # cat = choice(candidate_cats)  #Randomly choosing one cat from the pool

    fit_temp = candidate_cats[0][2]
    flag = True
    for candidates in candidate_cats:
        if candidates[2] != fit_temp:
            continue
        else:
            flag = False
            break

    if flag:
        cat = choice(candidate_cats)  # Randomly choosing one cat from the pool
    else:
        cat = sorted(candidate_cats,key = lambda cat:cat[2])[0] #cat with best fitness

    return cat

def tracing_mode(cat,best_cat,weight):
    temp = weight * cat[1] + np.random.random() * c1 * (best_cat[0] - cat[0])
    cat[0] += np.where(temp > upper_bound, upper_bound, temp)
    return cat

def create_solution():
    """
            x: position
            v: velocity
            flag: isSeeking?
    """
    x = np.random.uniform(lower_bound, upper_bound, problem_size)
    v = np.random.uniform(lower_bound, upper_bound, problem_size)
    print("x",x)
    fitness = f([x])
    flag = False  # False: seeking mode , True: tracing mode
    if np.random.random() < mixing_ratio:
        flag = True
    return [x, v,fitness, flag]

def get_best_cat(cats,fitness,cat_best):
    sort_temp = sorted(cats, key=lambda temp: temp[fitness])
    return deepcopy(sort_temp[cat_best])

def solution():
    cats = [create_solution() for _ in range(pop_size)]
    best_cat = get_best_cat(cats,2,0)
    for i in range(epoch):
        w = ((w_max - w_min) * ((epoch - i) / epoch))  + w_min
        for q in range(pop_size):
            if not cats[q][3]:
                cats[q] = seeking_mode(cats[q])
            else:
                cats[q] = tracing_mode(cat=cats[q],best_cat=best_cat,weight=w)
        for q in range(pop_size):
            if uniform() >= mixing_ratio:
                cats[q][3] = True
            else:
                cats[q][3] = False

        current_cat_best = get_best_cat(cats,2,0)
        if best_cat[2]< current_cat_best[2]:
            continue
        else:
            best_cat = current_cat_best
        # print("Generation : {0}, average MAE over population: {1}".format(i+1, best_cat[2]))
    print("f best", f([best_cat[0]]))
    return (best_cat[0],f(best_cat[0]))

    # print(x,fx)
