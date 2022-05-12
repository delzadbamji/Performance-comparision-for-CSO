
import matplotlib.pyplot as plt
from Algo.CSO import solution as cso_sol
from Algo.SA import solution as sa_sol
from Algo.DE import solution as de_sol
from Algo.PSO import solution as pso_sol
from Algo.FA import solution as fa_sol
from Algo.BA import solution as bat_sol


"""
#########################################
Runner File
@author Delzad Bamji 
@author Anuj K
#########################################
"""



algo = "PSO"

c_iteration, c_best_value = cso_sol()

if algo == "BAT":
  best_value = bat_sol()
elif algo == "FA":
  best_value = fa_sol()
elif algo == "SA":
  best_value = sa_sol()
elif algo == "DE":
  best_value = de_sol()
else:
  best_value = pso_sol()

function = ["Egg_crate","T1","Ackley","Rosenbrock"]

plt.plot(c_iteration, c_best_value, label="CSO")
plt.plot([i for i in range(500)], best_value, label=algo)
plt.ylabel('best fitness value')
plt.xlabel('iteration')
plt.legend()
plt.title('Best fitness value over generations:' + function[0] + ' function')
plt.show()
