import os
import pandas as pd
import numpy as np

rootdir = os.getcwd()
with open("simulation.input", "rt") as in_file:
    for line in in_file:
        if line.find("Component 1 MoleculeName") != -1:
            words = line.split()
            solute = words[3]
            print(solute)
henrystat = open("HenryStat.txt", "a")
henrystat.write("mol/kg/Pa kg/m^3\n")
#print(os.listdir())



for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if os.path.join(subdir,file).find("output") != -1:
            with open(os.path.join(subdir,file), "r") as out_file:
                lines = out_file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if line.find("["+str(solute)+"] Average Henry coefficient: ") != -1:
                        henryline = line.split()
                        henry = henryline[4]
                    elif line.find("Average Density") != -1:
                        dline = lines[i+8].split()
                        densline = dline[1]
            henrystat.write(str(henry)+" "+str(densline)+"\n")
henrystat.close()


file = "HenryStat.txt"

data = pd.read_csv(file, delim_whitespace = True)
print(data)

raspahenry = data["mol/kg/Pa"]
dens = data["kg/m^3"]
data = data.assign(molLbar=data['mol/kg/Pa']*data['kg/m^3']*(1/1000)*(1/0.00001))
data = data.assign(MPa=(data['mol/kg/Pa']*0.15382)**-1*1E-6)
henry = data["MPa"]
print(data)

#Choose block size such that it divides evenly into N data points
print('Number of blocks for set 1:')
n1 = int(input())
print('Number of blocks for set 2:')
n2 = int(input())
print('Number of blocks for set 3:')
n3 = int(input())
#print('Number of blocks for set 4:')
#n4 = int(input())
#print('Number of blocks for set 5:')
#n5 = int(input())
#print('Number of blocks for set 6:')
#n6 = int(input())

def henrycalc(a):
    henry1 = henry
    henry2 = []
    
    #block size that will be used
    x1 = int(henry.size/a)
    
    #no. of leftover data points
    xmod = henry.size % x1
      
    #slices remainder from the beginning of the run
    henry1 = henry1[xmod:]
   
#iterates through henry1 and appends the average of the first x1 data points to henry2 then deletes them from henry1
    while henry1.size > 0:
        henry2.append(np.mean(henry1.head(x1)))
        henry1 = henry1[x1:]

#NOT USED combines all data points that are < 2*x1 into the last block that is always >= x1    
#this guarantees that the mean of the sample is always equal to the mean of the population at the expense of evenness of block size   
    #henry2.append(np.mean(henry1))
    #henry1 = henry1[x1:]
    #else:
        #henry2.append(np.mean(henry1.head(x1)))
        #henry1 = henry1[x1:]
#Test    
    #print(henry1.size)
    #print(henry2)
    #print(len(henry2)) 
    s1 = np.std(henry2, ddof = 1)/(a)**0.5
    out_file = open("HenryBA.txt", "a")
    out_file.write('Set for ' + str(a) + ' blocks.\n'+'Count\n')
    #out_file.write('Set for ' + str(a) + ' blocks.\n')
    #out_file.write("Count\n"+str(len(henry2)+"\n"+"Data points sliced: " + str(xmod)+'\n'+'Mean\n'+np.mean(henry2)+'\n'+'S_m\n'+s1+'\n')
    #print("hello world")
    #out_file.close()
    out_file.write(str(len(henry2))+"\n" )
    out_file.write("Data points removed: " + str(xmod)+'\n')
    out_file.write('Mean\n')
    out_file.write(str(np.mean(henry2))+'\n')
    #s1 = np.std(henry2, ddof = 1)/(a)**0.5
    out_file.write('S_m\n')
    out_file.write(str(s1)+'\n\n')
    out_file.close()
        #stddev of std. dev.^ /might use later
        #ss1 = s1/(2*(a-1))**0.5
        #print('s(S_m)')
        #print(ss1)
henrycalc(n1)
henrycalc(n2)
henrycalc(n3)
#henrycalc(n4)
#henrycalc(n5)
#henrycalc(n6)
