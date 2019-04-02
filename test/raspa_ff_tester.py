import os
import subprocess
#get the files names in the testfolder, then split them at the . and keep the first (0th) entry to remove extenstions
testset = os.listdir('/home/c662h070/Software/raspa2/share/raspa/molecules/Roeselova_O3') 
testsplit = [f.split('.')[0] for f in testset]
print(testsplit)

for f in testsplit:
	subprocess.run(['mkdir '+f], shell=True)
	subprocess.run(['cp simulation.input raspajob '+f], shell=True)
	subprocess.run(['cd '+f], shell=True)
	with open("simulation.input", "rt") as in_file:
		file = in_file.read()
		for line in in_file:
			if line.find("Component 1 MoleculeName") != -1:
				words = line.split()
				solute = words[3]
				file = file.replace(solute, f)
	with open("simulation.input", "w") as in_file:
		in_file.write(file)						
	subprocess.run(['sbatch raspajob', 'cd ../'], shell=True)

