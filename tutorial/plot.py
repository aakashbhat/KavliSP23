# import mesa_reader
import mesa_reader as mr
import matplotlib.pyplot as plt
# load and plot data
h = mr.MesaData('LOGS/history.data')
plt.plot(h.log_Teff, h.log_L)

# set axis labels
plt.xlabel('log Effective Temperature')
plt.ylabel('log Luminosity')

# invert the x-axis
plt.gca().invert_xaxis()
plt.show()
