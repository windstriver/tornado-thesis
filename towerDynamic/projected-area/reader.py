# reader.py
# 20161221 by Yong Wang

import numpy as np

inputDir = "input/"

# Read Node List File (nodeNum, nodeX[m], nodeY[m], nodeZ[m])
nodeFile = inputDir+"node_list.txt"
nodeM = np.genfromtxt(nodeFile, delimiter=',')

# Read Element List File (eleNum, eleI, eleJ, eleSecn)
eleFile = inputDir+"ele_list.txt"
eleM = np.genfromtxt(eleFile, delimiter=',')

# Read Section List File (secNum, Ro[m])
secFile = inputDir+"sec_list.txt"
secM = np.genfromtxt(secFile, delimiter=',')

nodeCount = np.size(nodeM, 0)    # total num. of nodes
elemCount = np.size(eleM, 0)    # total num. of elements
secCount = np.size(secM, 0)    # total num. of sections
