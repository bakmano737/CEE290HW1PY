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

#####################################
# Define Model Matrices and Vectors #
#####################################

x1 = np.matrix(np.ones(11))
x2 = (1/ambTemp)*measTemp
x3 = (1/ambTemp**2)*np.multiply(measTemp, measTemp)
X  = np.concatenate((x1.T,x2.T,x3.T),1)
d  = np.log(measVisc)

##########################
#      The Solution      #
##########################
# m = ((X^T)X)^-1)(X^T)d #
##########################
m = np.linalg.inv(X.T*X)*X.T*d.T
print(m)

####################################
# Plot the Model and Observed Data #
####################################

# Model
modelTemp = np.arange(100)
lnmu = m[0,0] + (m[1,0]/ambTemp)*modelTemp + (m[2,0]/(ambTemp**2))*np.multiply(modelTemp, modelTemp)

# Plot the simulation
fig, ax = plt.subplots()
ax.plot(modelTemp, np.exp(lnmu), 'r', label='Model')
# Plot the data
x = np.array(measTemp[0]).reshape(11)
y = np.array(measVisc[0]).reshape(11)
ax.plot(x, y, 'b+', label='Data')
# Axis labels and legend
plt.xlabel('Temperature [C]')
plt.ylabel('Viscosity [mPa*s]')
ax.legend()
plt.show()