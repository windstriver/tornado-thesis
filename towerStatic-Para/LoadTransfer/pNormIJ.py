# pNormIJ.py
# 20161221 by Yong Wang

import numpy as np

def pNormIJ(CoordP=(0.0, 0.0, 0.0), CoordI=(1.0, 0.0, 0.0), CoordJ=(0.0, 1.0, 0.0), distEpsilon=1.0):
    """ Return the distance of point P to line IJ and the norm vector PP', where P' is the projection of P to IJ.

    Keyword arguments:
    CoordP -- the coordinates of point P, default (0.0, 0.0, 0.0)
    CoordI -- the coordinates of point I, default (0.0, 1.0, 0.0)
    CoordJ -- the coordinates of point J, default (0.0, 0.0, 1.0)
    distEpsilon -- distance criterion

    Return:
    dist -- distance from point P to line IJ
    normVec -- norm vector of PP'
    """
    CoordP = np.array(CoordP)
    CoordI = np.array(CoordI)
    CoordJ = np.array(CoordJ)
    CoordPPrime = np.zeros((3,))
    flag = False

    normIJ = np.linalg.norm(CoordI - CoordJ)
    CoordPPrime = CoordI + np.dot(CoordI-CoordP, CoordI-CoordJ)/(normIJ**2)*(CoordJ-CoordI)
    dist = np.linalg.norm(CoordP-CoordPPrime)
    normVec = (CoordPPrime-CoordP)/dist

    if (np.dot(CoordPPrime-CoordI, CoordPPrime-CoordJ) < 0 and dist < distEpsilon):
        flag = True

    return (dist, normVec, flag)


# test
# (dist, normVec, flag) = pNormIJ(CoordP=(1.0, 0.0, 0.0), CoordI=(0.0, 1.0, 0.0), CoordJ=(0.0, 0.0, 1.0))
# print(dist)
# print(normVec)
# print(flag)
