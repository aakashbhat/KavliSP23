# import mesa_reader
import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np
# load and plot data
h = mr.MesaData('LOGS/profile1.data')
h2 = np.genfromtxt('composition.dat',skip_header=1)
plt.plot(h.mass, h.he4)
#plt.plot(np.flip(h2[:,0]),h2[:,3])#,np.log10(h2[:,2]))
# set axis labels
plt.xlabel(r'log$\rho$')
plt.ylabel('logT')

# invert the x-axis
#plt.gca().invert_xaxis()
plt.show()
