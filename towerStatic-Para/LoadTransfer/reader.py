# reader.py
# 20161221 by Yong Wang

import numpy as np

inputDir = "Input/"
caseDir = "theta-0/"
# Read CFD Pressure Data (x[m], y[m], z[m], pres[Pa])
cfdPresFile = inputDir + caseDir + "cfd_pressure.csv"
cfdPresM = np.genfromtxt(cfdPresFile, delimiter=',', skip_header=17)
cfdPresM[:,3] = 1.0*cfdPresM[:,3]    # into the surface pressure +

# Read CFD velocity Data
# (nodeNum, x[m], y[m], z[m], pres[Pa], u[m/s], v[m/s], w[m/s])
cfdVeloFile = inputDir + caseDir + "cfd_velocity2.out"
cfdVeloM = np.genfromtxt(cfdVeloFile, delimiter=',')

# Remove the zero lines
cfdV = cfdVeloM[~np.all(cfdVeloM == 0.0, axis = 1)]
cfdV = cfdV[:, [0,5,6,7]]

# Read Node List File (nodeNum, nodeX[m], nodeY[m], nodeZ[m])
nodeFile = inputDir+"node_list.txt"
nodeM = np.genfromtxt(nodeFile, delimiter=',')

# Read Element List File (eleNum, eleI, eleJ, eleSecn)
eleFile = inputDir+"ele_list.txt"
eleM = np.genfromtxt(eleFile, delimiter=',')

# Read Section List File (secNum, Ro[m])
secFile = inputDir+"sec_list.txt"
secM = np.genfromtxt(secFile, delimiter=',')

presCount = np.size(cfdPresM, 0)    # total num. of cfd pressure points
nodeCount = np.size(nodeM, 0)    # total num. of nodes
elemCount = np.size(eleM, 0)    # total num. of elements
secCount = np.size(secM, 0)    # total num. of sections
veloCount = np.size(cfdV, 0)
