import numpy as np
import matplotlib.pyplot as plt

# set up constants
epsilon = 1.
sigma = 5.67e-8
input_selection=" "

# parameters for albedo linear fit to temperature
m = -0.01
c = 2.80



print("0=Calculate for single value of solar flux, albedo and iterations")
print("1=Calculate for range of solar fluxes")
print("Enter calculation selection: ")
input_selection = int(input())

if (input_selection == 0):
    """ Single value of solar flux L """
    print("Enter solar flux, start albedo estimate and number of iterations")
    L, albedo, nIters = input("").split()
    L, albedo, nIters = [ float(L), float(albedo), int(nIters) ]
    # set up arrays
    temp = np.zeros(nIters)
    Albedo_array = np.zeros(nIters)
    Albedo_array[0]= albedo
    plt_x = np.zeros(nIters)
    # Initialise temperature using user albedo start point and then update albedo based on linear regression fit
    temp[0] = (L * (1-Albedo_array[0]) / (4 * epsilon*sigma))** 0.25
    Albedo_array[0] = max(min(0.65, m *temp[0] +c), .15)
    # update temperature, albedo and iteration for nIters-1 iterations
    for i in range (1,nIters):
        # calculate new temperature using energy balance of solar flux in to IR out and then use linear regression fit to update albedo
        temp[i] = (L * (1-Albedo_array[i-1]) / (4 * epsilon*sigma))** 0.25
        Albedo_array[i] = max(min(0.65, m *temp[i] +c), .15)
        plt_x [i] = float(i)
    # print temperature and albedo after 100 iterations and plot Temperature against Iteration Number
    print("After ", nIters, "iterations, the temperature is ", temp[-1], "K and the albedo is ",Albedo_array[-1])
    plt.plot(plt_x, temp)
    plt.xlabel("Number of Iterations")
    plt.ylabel("Temperature")
    plt.show()
        
        
elif (input_selection ==1):
    # This section plots a range of solar fluxes
    print("Enter range for solar fluxes and increment")
    LRange = np.zeros(2, dtype=int)
    LRange[0], LRange[1], LInc = input("").split()
    LRange[0], LRange[1], LInc = [int (LRange[0]), int(LRange[1]), int(LInc)]
    albedo =0.15   # start from warm earth state
    nIters = 100   # fix 100 iterations for each value of L
    L = LRange[0]  # start from low solar flux
    # set up arrays
    temp = np.zeros(nIters)
    Albedo_array = np.zeros(nIters)
    Albedo_array[0]= albedo
    plt_x = np.zeros(nIters)
    
    # set up to plt
    plt.figure()

    
    while L < LRange[1]+1:
        temp[0] = (L * (1- albedo) / (4 * epsilon*sigma))** 0.25
        Albedo_array[0] = max(min(0.65, m *temp[0] +c), .15)
        for i in range (1,nIters):
        # calculate new temperature using energy balance of solar flux in to IR out and then use linear fit to update albedo
            temp[i] = (L * (1-Albedo_array[i-1]) / (4 * epsilon*sigma))** 0.25
            Albedo_array[i] = max(min(0.65, m * temp[i] + c), .15)
            plt_x [i] = float(i)
        plt.plot(plt_x, temp, label="L="+str(L))
        L = L + LInc
    plt.xlabel("Number of Iterations")
    plt.ylabel("Temperature")
    plt.legend()
    plt.show()    