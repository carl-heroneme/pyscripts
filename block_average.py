import pandas as pd
import numpy as np
file = input('Enter the file name you wish to analyze: ')

data = pd.read_csv(file, engine='python', delim_whitespace = True, skiprows=2, names = ["sweep", "energy", "pressure", "volume", "density", "mass_density"])

mass_density = data.loc[:,"mass_density"]

#Choose block size such that it divides evenly into N data points
print('Number of blocks for set 1:')
n1 = int(input())
print('Number of blocks for set 2:')
n2 = int(input())
print('Number of blocks for set 3:')
n3 = int(input())
print('Number of blocks for set 4:')
n4 = int(input())
print('Number of blocks for set 5:')
n5 = int(input())
print('Number of blocks for set 6:')
n6 = int(input())

def mass_dense(a):
    mass_density1 = mass_density
    mass_density2 = []
    
    #block size that will be used
    x1 = int(mass_density.size/a)
    
    #no. of leftover data points
    xmod = mass_density.size % x1
      
    #slices remainder from the beginning of the run
    mass_density1 = mass_density1[xmod:]
   
#iterates through mass_density1 and appends the average of the first x1 data points to mass_density2 then deletes them from mass_density1
    while mass_density1.size > 0:
        mass_density2.append(np.mean(mass_density1.head(x1)))
        mass_density1 = mass_density1[x1:]

#NOT USED combines all data points that are < 2*x1 into the last block that is always >= x1    
#this guarantees that the mean of the sample is always equal to the mean of the population at the expense of evenness of block size   
    #mass_density2.append(np.mean(mass_density1))
    #mass_density1 = mass_density1[x1:]
    #else:
        #mass_density2.append(np.mean(mass_density1.head(x1)))
        #mass_density1 = mass_density1[x1:]
#Test    
    #print(mass_density1.size)
    #print(mass_density2)
    #print(len(mass_density2)) 


    print('Set for ' + str(a) + ' blocks.' )
    print("Count")
    print(len(mass_density2))
    print('Data points sliced: ' + str(xmod))
    print('Mean')
    print(np.mean(mass_density2))
    s1 = np.std(mass_density2, ddof = 1)/(a)**0.5
    print('S_m')
    print(s1)
    #stddev of std. dev.^ /might use later
    #ss1 = s1/(2*(a-1))**0.5
    #print('s(S_m)')
    #print(ss1)
    #print( )
   
mass_dense(n1)
mass_dense(n2)
mass_dense(n3)
mass_dense(n4)
mass_dense(n5)
mass_dense(n6)

