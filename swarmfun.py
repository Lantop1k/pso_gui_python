import numpy as np

#list of functions to evaluate from
# The following functions are 2D Functions for testing global optimization

#Ackley Function
def Ackley(x):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x[0]**2+x[1]**2)))-np.exp(.5*(np.cos(2*np.pi*x[0]+np.cos(2*np.pi*x[1]))))+20

#Booth Function
def Booth(x):
    return (x[0]+2*x[1]-7)**2 + (2*x[0]+x[1]-5)**2

#Matyas Function
def Matyas(x):
    return 0.26*(x[0]**2+x[1]**2)-.48*x[0]*x[1]

#Himmelblau Function
def Himmelblau(x):
    return (x[0]**2+x[1]-11)**2 + (x[0] + x[1]**2-7)**2

#Beale Function
def Beale(x):
    return (1.5-x[0]+x[0]*x[1])**2 + (2.25 -x[0] +x[0]*(x[1]**2))**2 + (2.625 -x[0] + x[0]*(x[1]**3))**2
