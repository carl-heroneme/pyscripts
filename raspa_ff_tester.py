import os
import subprocess
#get the files names in the testfolder, then split them at the . and keep the first (0th) entry to remove extenstions
testset = os.listdir('/home/c662h070/Software/raspa2/share/raspa/molecules/Roeselova_O3') 
testsplit = [f.split('.')[0] for f in testset]
print(testsplit)
#remember to edit jobarrays 1-n%i in your submit script to limit the # of runs based on how many FF's you are testing!
#does bash things. edits each input file and spawns an array of raspa runs for each of your test ff's. 
#raspajob is your submit script, simulation.input your input file, and component 1 is your solute
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

