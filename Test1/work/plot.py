# import mesa_reader
import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np
# load and plot data
h = mr.MesaData('LOGS/profile1.data')
h2 = np.genfromtxt('entropy.dat',skip_header=1)
plt.plot(h.logRho, h.logT)
plt.plot(np.log10(h2[:,1]),np.log10(h2[:,2]))
# set axis labels
plt.xlabel(r'log$\rho$')
plt.ylabel('logT')

# invert the x-axis
#plt.gca().invert_xaxis()
plt.show()
