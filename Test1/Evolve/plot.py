# import mesa_reader
import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np
# load and plot data
h = mr.MesaData('LOGS_evolved_1year/profile4.data')
plot="composition"
if plot=="composition":
    h2 = np.genfromtxt('composition.dat',skip_header=1)
    plt.plot(h.xq, np.log10(h.he4))
    plt.plot(h.xq, np.log10(h.c12))
    plt.plot(h.xq, np.log10(h.n14))
    plt.plot(h.xq, np.log10(h.o16))
    plt.plot(h.xq, np.log10(h.fe56))
    plt.ylim(-5,0)
    #plt.plot(h2[:,0],np.log10(h2[:,3]))
    #plt.plot(h2[:,0],np.log10(h2[:,4]))
    #plt.plot(h2[:,0],np.log10(h2[:,5]))
    #plt.plot(h2[:,0],np.log10(h2[:,6]))
    #plt.plot(h2[:,0],np.log10(h2[:,12]))

    # set axis labels
    plt.legend(("he4","c12","n14","o16","fe56"))
    #,"he4R","c12r","n14r","o16r","fe56r"))

    plt.xlabel(r'log$X_q$')
    plt.ylabel(r'$X_n$')

    # invert the x-axis
    #plt.gca().invert_xaxis()
    plt.savefig("Plots/composition_comparison_evolved_1.pdf")
    plt.savefig("Plots/composition_comparison_evolved_1.png")


elif plot=="rhoT":
    h3 = np.genfromtxt('entropy.dat',skip_header=1)
    plt.plot(h.logRho, h.logT)
    plt.plot(np.log10(h3[:,1]),np.log10(h3[:,2]))
    plt.xlabel(r"log$\rho$")
    plt.ylabel("logT")
    plt.show()
        #plt.gca().invert_xaxis()
