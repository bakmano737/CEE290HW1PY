############################################################
# ----------- University of California, Irvine ----------- #
# ------------- CEE 290 Mergin Models & Data ------------- #
# --------------- Homework #1 - Problem #1 --------------- #
# ---- Temperature Dependence of Viscosity of a Fluid ---- #
# --------------- James V. Soukup 85841994 --------------- #
############################################################

# Import the usual suspects
import numpy as np
import matplotlib.pyplot as plt

##############
# Initialize #
##############

## Measured Values
# Measured Temperature [degrees Celsius]
measTemp = np.matrix([0.0, 5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0])
# Measured Viscosity (10^-3) [Pa*s]
measVisc = np.matrix([1.79, 1.52, 1.31, 1.00, 0.80, 0.65, 0.55, 0.47, 0.40, 0.35, 0.31])

## System Invariant
# Ambient Temperature
ambTemp = 20.0