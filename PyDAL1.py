#Python script to post-process ExploRAM results

import numpy as np
import matplotlib.pyplot as plt

#Read a folder and construct a list of Cases
Cases = ['P05_A_deck']
case = cases[0]

NPressureCategory = 100
CFs = np.zeros((1,NPressureCategory))

for case in Cases:
    for fdr in ['Gas','Oil']:
        for forl in ['F','L']:
            #_pressure_frequency_cumulative_F                
            f = open('.\\'+fdr+'\\'+case+'_pressure_frequency_cumulative_'+forl+'.txt','r')
            pressure_category  = f.readline().split(';')[1:-1]
            upper_bound  = f.readline().split(';')[1:-1]
            if NPressureCategory  != len(pressure_category ):
                break
            #Read Cumultative frequency from all segments        
            PFC  = np.zeros((5,NPressureCategory ))        
            for i in range(0,5):
                N = f.readline().split(';')[:-1]
                # N[0] should bene of small, mediu, major, large, or total
                PFC [i,:] = [float(x) for x in N[1:]]
            #Read Cumultative frequency from each segment
            # PFC_segment = np.zeros((NSeg,NPressureCategory ))
            # for i in range(0,NSeg):
            #     N = f.readline().split(';')[:-1]            
            #     PFC_segment[i,:] = [float(x) for x in N[1:]]
            f.close()

            CFs += PFC[4,:]

    Ps = np.array([float(x) for x in upper_bound_F])
    #왜 그런지는 모르겠지만 CFs의 [0]을 선정해야 차원이 맞네...
    CFs = CFs[0]

    #Interpolation for the dimensioning scenario
    #Save to add a 
    
    masscolor = 'tab:blue'
    fig,ax1 = plt.subplots()
    ax1.set_xlabel(case+' Pressure[barg]')
    ax1.set_ylabel('Cumulative Frequency [#/year]',color=masscolor)
    ax1.semilogy(Ps,CFs,color=masscolor)
    ax1.set_ylim(top=5E-4,bottom=1E-6)
    ax1.set_xlim(left=0, right=2)
    ax1.tick_params(axis='y',labelcolor=masscolor)
    ax1.xaxis.set_major_locator(plt.FixedLocator([0.1, 0.5, 1, 1.5, 2]))
    # ax1.annotate(scn,xy=(di,1.0E-4),xytext=(di,2E-4),horizontalalignment='left',verticalalignment='top',arrowprops = dict(facecolor='black',headwidth=4,width=2,headlength=4))
    ax1.grid(True,which="major")

    if InterpolationSuccess:
        plt.title("Cube {:10s} - {:5s} fire from {:30} for {:8.1f} [sec]".format(id,weather_fire[6:],pv+"_"+hole+"_"+weather_fire[:5],di))            
    else:
        plt.title("Cube {:10s} - No dimensioning fire".format(id))            
    plt.tight_layout()
    plt.show()

    fig.savefig("{}.png".format(id))
    plt.close()

#Open a DOCX file
#Draw DOCX header & Table header
for case in Cases:
    #Insert a DAL
for case in Cases:
    #Insert Exceedance curves
