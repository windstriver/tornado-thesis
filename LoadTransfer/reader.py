# reader.py
# 20161221 by Yong Wang

import numpy as np

apdlDir = "apdl/"
# Read CFD Pressure Data (x[m], y[m], z[m], pres[Pa])
cfdPresFile = apdlDir+"cfd_pressure.csv"
cfdPresM = np.genfromtxt(cfdPresFile, delimiter=',', skip_header=6)
cfdPresM[:,0:3] = cfdPresM[:,0:3]*1000
cfdPresM[:,3] = cfdPresM[:,3]/10**6

# Read Node List File (nodeNum, nodeX[m], nodeY[m], nodeZ[m])
nodeFile = apdlDir+"node_list.txt"
nodeM = np.genfromtxt(nodeFile, delimiter=',')

# Read Element List File (eleNum, eleI, eleJ, eleSecn)
eleFile = apdlDir+"ele_list.txt"
eleM = np.genfromtxt(eleFile, delimiter=',')

# Read Section List File (secNum, Ro[m])
secFile = apdlDir+"sec_list.txt"
secM = np.genfromtxt(secFile, delimiter=',')

presCount = np.size(cfdPresM, 0)    # total num. of cfd pressure points
nodeCount = np.size(nodeM, 0)    # total num. of nodes
elemCount = np.size(eleM, 0)    # total num. of elements
secCount = np.size(secM, 0)    # total num. of sections
