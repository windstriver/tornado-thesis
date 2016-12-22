import numpy as np

import reader as rd
import crossSele as cs
import pNormIJ as pIJ

epsilon = 0.01

# Initiate Matrix elePres to hold pressure on elemnt (eleNum, presX, presY, presZ)
elePres = np.zeros((rd.elemCount, 5))
elePres[:, 0] = range(1,rd.elemCount+1)

for p in range(rd.presCount):
    # p iterate all the cfd pressure points
    XP = rd.cfdPresM[p, 0:3]    # Coordinates of point p+1
    pres = -1.0*rd.cfdPresM[p, 3]    # pressure of point p+1
    
    # decide cfd pressure point (p+1) belongs to which element
    for e in range(rd.elemCount):
        # e interate all elements, e refers element (e+1)
        (dist, normVec, flag) = pIJ.pNormIJ(XP, cs.XIE(e+1), cs.XJE(e+1), distEpsilon=cs.RoE(e+1)*(1+epsilon))    # compute the distance from point (p+1) to element (e+1)
        if flag:
            # cfd pressure point (p+1) belongs to element (e+1)
            elePres[e, 1:4] = elePres[e, 1:4] + pres*normVec
            elePres[e, 4] = elePres[e, 4] + 1
            break

print("CFD Pressure Points mapping ratio: {:6.3%}.".format(sum(elePres[:,4])/rd.presCount))


# Transfer the element pressures to element node force
# Init nodeForce matrix to hold force on nodes (nodeNum, Fx, Fy, Fz)
nodeForce = np.zeros((rd.nodeCount, 4))
nodeForce[:, 0] = range(1,rd.nodeCount+1)

for e in range(rd.elemCount):
    # (e+1) interate all elements
    if elePres[e, 4] == 0:
        presMean = np.zeros((3,))
    else:
        presMean = elePres[e, 1:4] / elePres[e, 4]

    forceTotal = presMean * cs.AoE(e+1)
    nodeI = int(rd.eleM[e, 1])
    nodeJ = int(rd.eleM[e, 2])
    nodeForce[nodeI-1, 1:4] = nodeForce[nodeI-1, 1:4] + forceTotal/2
    nodeForce[nodeJ-1, 1:4] = nodeForce[nodeJ-1, 1:4] + forceTotal/2


print("Sum FX is {:6.3f} N.".format(sum(nodeForce[:, 1])))
print("Sum FY is {:6.3f} N.".format(sum(nodeForce[:, 2])))
print("Sum FZ is {:6.3f} N.".format(sum(nodeForce[:, 3])))

# Write APDL code to apply node force
with open('load.mac', 'w') as f:
    for n in range(rd.nodeCount):
        f.write('F,{NODE:6d},{Lab}, {VALUE:9.3f}\n'.format(NODE=n+1, Lab='FX', VALUE=nodeForce[n, 1]))
        f.write('F,{NODE:6d},{Lab}, {VALUE:9.3f}\n'.format(NODE=n+1, Lab='FY', VALUE=nodeForce[n, 2]))
        f.write('F,{NODE:6d},{Lab}, {VALUE:9.3f}\n'.format(NODE=n+1, Lab='FZ', VALUE=nodeForce[n, 3]))


f.close()

