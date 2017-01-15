import numpy as np
import pandas as pd

# Case: theta=0
resDir0 = '../towerStatic-RS-WB-theta-0/res_axial_force.out'
res0 = np.genfromtxt(resDir0, delimiter=',', skip_header=2)

# Case: theta=45
resDir45 = '../towerStatic-RS-WB-theta-45/res_axial_force.out'
res45 = np.genfromtxt(resDir45, delimiter=',', skip_header=2)

# Case: theta=90
resDir90 = '../towerStatic-RS-WB-theta-90/res_axial_force.out'
res90 = np.genfromtxt(resDir90, delimiter=',', skip_header=2)

# Combine these results to Pandas Data Frame
elem_index = pd.Series(res0[:, 0].astype('int32'))
columns_name = pd.Series(['FSI_0', 'CODE_0', 'FSI_45', 'CODE_45', 'FSI_90', 'CODE_90'])

df = pd.DataFrame(index=elem_index, columns=columns_name)
df['FSI_0'] = res0[:, 1]
df['CODE_0'] = res0[:, 2]
df['FSI_45'] = res45[:, 1]
df['CODE_45'] = res45[:, 2]
df['FSI_90'] = res90[:, 1]
df['CODE_90'] = res90[:, 2]

df.to_csv('post.csv', sep=',', encoding='utf-8')
