import numpy as np

import reader as rd
import crossSele as cs

loadDir = 'load3.csv'

rho = 1.25

def eseln(nodeNum):
    EI = rd.eleM[rd.eleM[:, 1] == nodeNum][:, 0]
    EJ = rd.eleM[rd.eleM[:, 2] == nodeNum][:, 0]
    return np.append(EI, EJ)

nodeForce2 = np.zeros((rd.veloCount, 4))
nodeForce2[:, 0] = rd.cfdV[:, 0]

for i in range(rd.veloCount):

    eleList = eseln(rd.cfdV[i, 0])

    for elem in eleList:
        xi = cs.XIE(int(elem))
        xj = cs.XJE(int(elem))
        Ax = np.sqrt((xi[1]-xj[1])**2+(xi[2]-xj[2])**2)*cs.RoE(int(elem))
        Ay = np.sqrt((xi[0]-xj[0])**2+(xi[2]-xj[2])**2)*cs.RoE(int(elem))
        Az = np.sqrt((xi[0]-xj[0])**2+(xi[1]-xj[1])**2)*cs.RoE(int(elem))
        nodeForce2[i, 1] = nodeForce2[i, 1] + 0.5*rho*Ax*rd.cfdV[i, 1]*np.abs(rd.cfdV[i, 1])
        nodeForce2[i, 2] = nodeForce2[i, 2] + 0.5*rho*Ay*rd.cfdV[i, 2]*np.abs(rd.cfdV[i, 2])
        nodeForce2[i, 3] = nodeForce2[i, 3] + 0.5*rho*Ax*rd.cfdV[i, 3]*np.abs(rd.cfdV[i, 3])


flag = ~(nodeForce2[:, 1:] == 0)
index = np.logical_and(flag[:, 0], flag[:, 1], flag[:, 2])
nodeForce2 = nodeForce2[index, :]

print("Sum FX is {:6.3f} N.".format(sum(nodeForce2[:, 1])))
print("Sum FY is {:6.3f} N.".format(sum(nodeForce2[:, 2])))
print("Sum FZ is {:6.3f} N.".format(sum(nodeForce2[:, 3])))

loadCount = np.size(nodeForce2, 0)

with open(loadDir, 'w') as f:
    for n in range(loadCount):
        f.write('{NODE:6d}, {Fx:9.3f}, {Fy:9.3f}, {Fz:9.3f}\n'.format(\
            NODE=int(nodeForce2[n, 0]), \
            Fx=nodeForce2[n, 1], \
            Fy=nodeForce2[n, 2], \
            Fz=nodeForce2[n, 3]))

f.close()