# import mesa_reader
import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np
# load and plot data
h = mr.MesaData('LOGS_evolved_1D8years_nomaxtimestep_burning/profile12.data')
plot="time_evolution"
if plot=="composition":
    h2 = np.genfromtxt('composition.dat',skip_header=1)
    plt.plot(h.xq, np.log10(h.he4))
    plt.plot(h.xq, np.log10(h.c12))
    plt.plot(h.xq, np.log10(h.n14))
    plt.plot(h.xq, np.log10(h.o16))
    plt.plot(h.xq, np.log10(h.fe56))
    plt.ylim(-15,0)
    plt.plot(h2[:,0],np.log10(h2[:,3]))
    plt.plot(h2[:,0],np.log10(h2[:,4]))
    plt.plot(h2[:,0],np.log10(h2[:,5]))
    plt.plot(h2[:,0],np.log10(h2[:,6]))
    plt.plot(h2[:,0],np.log10(h2[:,12]))

    # set axis labels
    plt.legend(("he4","c12","n14","o16","fe56","he4R","c12r","n14r","o16r","fe56r"))

    plt.xlabel(r'log$X_q$')
    plt.ylabel(r'$X_n$')

    # invert the x-axis
    #plt.gca().invert_xaxis()
    plt.savefig("Plots_burning/composition_comparison_evolved_1d8.pdf")
    plt.savefig("Plots_burning/composition_comparison_evolved_1d8.png")


elif plot=="rhoT":
    h3 = np.genfromtxt('entropy.dat',skip_header=1)
    plt.plot(h.logRho, h.logT)
    plt.plot(np.log10(h3[:,1]),np.log10(h3[:,2]))
    plt.xlabel(r"log$\rho$")
    plt.ylabel("logT")
    plt.show()
        #plt.gca().invert_xaxis()

lif plot=="HR":
    # load and plot data
    h = mr.MesaData('LOGS_evolved_1D8years_nomaxtimestep_burning/history.data')
    plt.plot(h.log_Teff, h.log_L)

    # set axis labels
    plt.xlabel('log Effective Temperature')
    plt.ylabel('log Luminosity')

    # invert the x-axis
    plt.gca().invert_xaxis()
    plt.savefig("Plots_burning/HR_1d8.pdf")
    plt.savefig("Plots_burning/HR_1d8.png")
elif plot=="time_evolution":
    
     # load and plot data
    h = mr.MesaData('LOGS_evolved_1D8years_nomaxtimestep_burning/history.data')
    figs, axs=plt.subplots(3,1,figsize=(8,14))
    axs[0].plot(np.log10(h.star_age), h.log_L)
    axs[0].set_ylabel("logL",fontsize=12)
    axs[1].plot(np.log10(h.star_age), h.log_R)
    axs[1].set_ylabel("logR",fontsize=12)
    axs[2].plot(np.log10(h.star_age), h.log_Teff)
    axs[2].set_ylabel("logTeff",fontsize=12)

    # set axis labels
    plt.xlabel('log(Star Age)',fontsize=12)
    #plt.ylabel('log Luminosity')

    # invert the x-axis
    #plt.gca().invert_xaxis()
    plt.savefig("Plots_burning/time_evolved_1d8.pdf")
    plt.savefig("Plots_burning/time_evolved_1d8.png")
elif plot=="radial_profile":
    h = mr.MesaData('LOGS_evolved_1D8years/profile3.data')
    plt.plot(h.logR,np.log10(h.mass))
    plt.savefig("Plots_burning/mass_radial_profile_1d8_profile3.png")
