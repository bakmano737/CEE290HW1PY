############################################################
# --------- Written in Matlab by Jasper A. Vrugt --------- #
# --------- Adapted to Python by James V. Soukup --------- #
# ----------- University of California, Irvine ----------- #
# --------------- CEE 290 : Models & Data ---------------- #
############################################################

import numpy as np
import matplotlib.pyplot as plt

def slugmodel():
    # Ummmmmm
    return

#####################################
# Define measurements and constants #
#####################################
# Define the measured head
headObs = [0.55, 0.47, 0.30, 0.22, 0.17, 0.14]
# Define the time
timeObs = [5.0, 10.0, 20.0, 30.0, 40.0, 50.0]
# Define the distance from injection
d = 10 
# Define amount of injected water
Q = 50

# default values for the parameters:
S = 0.15
T = 0.4


# make a big figure
bigfigure(1,1,1,'figureNumber',1001)
# prepare some arrays for the visualization 
hu = repmat(NaN,[1,6])
hl = repmat(NaN,[1,6])

for iSubplot in range(1,6):
    if iSubplot>1:
        strS = ['(Press Enter to accept previous value of ',str(S),')']
        strT = ['(Press Enter to accept previous value of ',str(T),')']
    else:
        strS = ['(Press Enter to accept default value of ',str(S),')']
        strT = ['(Press Enter to accept default value of ',str(T),')']
    tmp = input(['Enter a value for ''S'' ',strS,'. >> '])
    if ~isempty(tmp):
        S=tmp
    tmp = input(['Enter a value for ''T'' ',strT,'. >> '])
    if ~isempty(tmp):
        T=tmp

    ################### 
    # Make Prediction #
    ################### 
    # Concatentate the parameters into a 1xN vector
    pars = [S,T]
    # Define for which the forward model should give a prediction
    timeSim = timeObs
    # Run the forward model with the parameters etc.
    headSim = slugmodel(pars,timeSim,Q,d)


    ################# 
    # Visualization #
    ################# 
    # Re-run the slugmodel function to create a smooth interpolation 
    timeSimSmooth = linspace(timeObs(1),timeObs(end),200)
    # Run the forward model with the parameters etc.
    headSimSmooth = slugmodel(pars,timeSimSmooth,Q,d)

    # Do this in a convoluted way to deal with octave shizzle
    UWH=[0.27,0.35]
    LWH=[0.27,0.08]
    L = [0.05,0.38,0.72,0.05,0.38,0.72]
    UB = [0.64,0.64,0.64,0.14,0.14,0.14]
    LB = [0.55,0.55,0.55,0.05,0.05,0.05]

    if isnan(hu[iSubplot]):
        hu[iSubplot]=axes('position',[L[iSubplot],UB[iSubplot],UWH])
    else:
        axes(hu[iSubplot])
    #plot(timeObs,headObs,'om',
    #     timeSim,headSim,'b.',
    #     timeSimSmooth,headSimSmooth,'-b')
    legend('obs','sim','Location','NorthEast')
    set(gca,'ylim',[0,0.7],'xticklabel',[])
    text(30,0.6,['S = ',str(S),char(10),'T = ',str(T)],
         'fontsize',9,'horizontalalignment','center')
    ylabel('head [m]')
    if isnan(hl[iSubplot]):
        hl[iSubplot]=axes('position',[L[iSubplot],LB[iSubplot],LWH])
    else:
        axes(hl[iSubplot])
    stem(timeObs,headSim-headObs,'-r.')
    set(gca,'ylim',[-1,1]*0.2)
    xlabel('time')
    ylabel('residual')

    disp(['Results visualized in subplot ',str(iSubplot),char(10)])