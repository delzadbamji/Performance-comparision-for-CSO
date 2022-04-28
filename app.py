from tqdm import tqdm
from CSO import solution as cso
from matplotlib import pyplot as plt
import sys
sys.path.insert(0, '...')
from hw2.hw2_csci633_ago.hw2_release.db3765_hw2_q4b import solve as sa,f as saf
from hw4.hw4_csci633_ago.hw4_release.db3765_hw4_q4b import solve as ba

CSO_list = []
SA_list = []

# CSO on ackley 1x10
for i in tqdm(range(30)):
    cso_position,cso_fitness = cso()
    CSO_list.append((cso_position,cso_fitness))

# SA on ackley 1x2
for i in tqdm(range(30)):
    SA_position,SA_fitness = sa(f=saf,lower_bound=-35, upper_bound=35, T_initial=10, T_final=0, N=100, alpha=0.2)
    SA_list.append((SA_position,SA_fitness))

# Bat algo on ackley 1x2
BA_list = []
for i in tqdm(range(30)):
    BA_position,BA_fitness = ba(N=100, minFreq=0, maxFreq=2, alpha=0.01, gamma=0.3)
    BA_list.append((BA_position,BA_fitness))

# print("SA: ",SA_list)
# print("CSO: ", CSO_list)

# CSO plot
plt.plot([x[0] for x in CSO_list], [x[1] for x in CSO_list],color="orange")
# SA plot
plt.plot([x[0] for x in SA_list], [x[1] for x in SA_list],color="blue")
# BA plot
# plt.plot([x[0] for x in BA_list], [x[1] for x in BA_list],color="green")

plt.xlabel('positions')
plt.ylabel('fitness')
plt.title('CSO vs SA')
plt.legend()
plt.show()
