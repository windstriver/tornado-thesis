import numpy as np

loadDir = 'load3.csv'
loadAPDL = 'load3.mac'
# theta = -28.35
theta = 0

loadData = np.genfromtxt(loadDir, delimiter=',')
flag = ~(loadData[:, 1:] == 0)
index = np.logical_or(flag[:, 0], flag[:, 1], flag[:, 2])
loadData = loadData[index, :]
loadCount = np.size(loadData, 0)

print("Before Rotation: Sum FX is {:6.3f} N.".format(sum(loadData[:, 1])))
print("Before Rotation: Sum FY is {:6.3f} N.".format(sum(loadData[:, 2])))
print("Before Rotation: Sum FZ is {:6.3f} N.".format(sum(loadData[:, 3])))

# Rotate Load based on theta

loadRot = np.zeros((loadCount, 4))
loadRot[:, 0] = loadData[:, 0]
loadRot[:, 1] = np.cos(np.deg2rad(theta))*loadData[:, 1] \
    - np.sin(np.deg2rad(theta))*loadData[:, 2]
loadRot[:, 2] = np.sin(np.deg2rad(theta))*loadData[:, 1] \
    + np.cos(np.deg2rad(theta))*loadData[:, 2]
loadRot[:, 3] = loadData[:, 3]

print("\nAfter Rotation: Sum FX is {:6.3f} N.".format(sum(loadRot[:, 1])))
print("After Rotation: Sum FY is {:6.3f} N.".format(sum(loadRot[:, 2])))
print("After Rotation: Sum FZ is {:6.3f} N.".format(sum(loadRot[:, 3])))

print('\nWrite APDL code to apply node force.\n')
with open(loadAPDL, 'w') as f:
    for n in range(loadCount):
        f.write('F,{NODE:6d},{Lab}, {VALUE:9.3f}\n'.format(\
            NODE=int(loadRot[n, 0]), Lab='FX', VALUE=loadRot[n, 1]))
        f.write('F,{NODE:6d},{Lab}, {VALUE:9.3f}\n'.format(\
            NODE=int(loadRot[n, 0]), Lab='FY', VALUE=loadRot[n, 2]))
        f.write('F,{NODE:6d},{Lab}, {VALUE:9.3f}\n'.format(\
            NODE=int(loadRot[n, 0]), Lab='FZ', VALUE=loadRot[n, 3]))

f.close()
print('Done.\n')
