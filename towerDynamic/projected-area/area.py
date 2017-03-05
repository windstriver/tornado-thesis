import numpy as np

import reader as rd
import crossSele as cs

output = 'area.csv'

def eseln(nodeNum):
    EI = rd.eleM[rd.eleM[:, 1] == nodeNum][:, 0]
    EJ = rd.eleM[rd.eleM[:, 2] == nodeNum][:, 0]
    return np.append(EI, EJ)


area = np.zeros((rd.nodeCount, 3))

for node in range(rd.nodeCount):
    area[node, 0] = node+1
    eleList = eseln(node+1)
    # print(eleList)
    for elem in eleList:
        xi = cs.XIE(int(elem))
        xj = cs.XJE(int(elem))
        area[node, 1] = area[node, 1] + np.sqrt((xi[1]-xj[1])**2+(xi[2]-xj[2])**2)*cs.RoE(int(elem))
        area[node, 2] = area[node, 2] + np.sqrt((xi[0]-xj[0])**2+(xi[2]-xj[2])**2)*cs.RoE(int(elem))

flag = ~(area[:, 1:] == 0)
index = np.logical_or(flag[:, 0], flag[:, 1])
area = area[index, :]
areaCount = np.size(area, 0)

with open(output, 'w') as f:
    for n in range(areaCount):
        f.write('{NODE:6d}, {Ax:12.6f}, {Ay:12.6f}\n'.format(\
            NODE=int(area[n, 0]), \
            Ax=area[n, 1], \
            Ay=area[n, 2]))

f.close()
