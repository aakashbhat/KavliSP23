# import mesa_reader
import mesa_reader as mr
import matplotlib.pyplot as plt
import numpy as np
# load and plot data
h = mr.MesaData('LOGS_relaxed_ni56_normalh_he4/profile1.data')
plot="rhoT"
if plot=="composition":
    h2 = np.genfromtxt('composition.dat',skip_header=1)
    h4 = mr.MesaData('../../Test1/make_co_wd/LOGS/profile34.data')

    plt.plot(h4.xq, np.log10(h4.h1))
    plt.plot(h4.xq, np.log10(h4.he4))
    plt.plot(h4.xq, np.log10(h4.c12))
    plt.plot(h4.xq, np.log10(h4.n14))
    plt.plot(h4.xq, np.log10(h4.o16))
    #plt.plot(h4.xq, np.log10(h4.ni56))
    plt.ylim(-5,0)
    plt.plot(h2[:,0],np.log10(h2[:,3]))
    plt.plot(h2[:,0],np.log10(h2[:,4]))
    plt.plot(h2[:,0],np.log10(h2[:,5]))
    plt.plot(h2[:,0],np.log10(h2[:,6]))
    plt.plot(h2[:,0],np.log10(h2[:,12]))

    # set axis labels
    plt.legend(("h1o","he4o","c12o","n14o","o16o","he4r","c12r","n14r","o16r","ni56r"))

    plt.xlabel(r'$X_q$')
    plt.ylabel(r'$X_n$')

    # invert the x-axis
    #plt.gca().invert_xaxis()
    plt.savefig("Plots/composition_comparison_withWD.pdf")
    plt.savefig("Plots/composition_comparison_withWD.png")


elif plot=="rhoT":
    #h2 = np.genfromtxt('donor_entropy.dat',skip_header=1)
    fig,ax=plt.subplots()
    plt.rcParams["font.size"]=20
    plt.rcParams["axes.labelsize"]=20
    plt.rcParams["legend.fontsize"]=15
    plt.rcParams['lines.linestyle']="--"
    plt.rcParams['lines.linewidth']=4
    #img = plt.imread("eos_regions.jpg")
    #ax.imshow(img,extent=[])
    plt.plot(h.logRho, h.logT)
    h3 = np.genfromtxt('entropy.dat',skip_header=1)
    h4 = mr.MesaData('../../Test1/make_WD_model/LOGS/profile2.data')
    plt.plot(h4.logRho, h4.logT)

    #plt.plot(np.log10(h2[:,1]),np.log10(h2[:,2]))
    plt.plot(np.log10(h3[:,1]),np.log10(h3[:,2]))
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.xlabel(r"log$\rho$ (gcm$^{-3}$)",fontsize=18)
    plt.ylabel("logT (K)",fontsize=18)
    plt.legend(['Relaxed WD','Original WD','Arepo Model'])
    plt.tight_layout()
    plt.savefig("/userdata/data/bhat/D6/KavliSP23/Report/Plots/entropy_comparison_relaxation.pdf")
    plt.savefig("/userdata/data/bhat/D6/KavliSP23/Report/Plots/entropy_comparison_relaxation.png")

        #plt.gca().invert_xaxis()

elif plot=="profile":

        h2 = np.genfromtxt('composition.dat',skip_header=1)
        gravity=G*h2[:,0]
