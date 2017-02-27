import numpy as np

import reader as rd

def XIE(eleNum=1):
    """ Get the coordinates of I node of Element eleNum.

    Keyword argument:
    eleNum -- element number
    """
    eINum = int(rd.eleM[eleNum-1][1])
    return rd.nodeM[eINum-1][1:]


def XJE(eleNum=1):
    """ Get the coordinates of J node of Element eleNum.

    Keyword argument:
    eleNum -- element number
    """
    eJNum = int(rd.eleM[eleNum-1][2])
    return rd.nodeM[eJNum-1][1:]


def RoE(eleNum=1):
    """ Get the Ro of section of Element eleNum.

    Keyword argument:
    eleNum -- element number
    """
    secNum = int(rd.eleM[eleNum-1][3])
    return rd.secM[secNum-1][1]

def AoE(eleNum=1):
    """ Get the surface area of Element eleNum.

    Keyword argument:
    eleNum -- element number    
    """
    length = np.linalg.norm(XIE(eleNum)-XJE(eleNum))
    return 2*np.pi*RoE(eleNum)*length
