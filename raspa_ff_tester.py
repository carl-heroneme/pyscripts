import os
import sys
import fileinput
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
	for i, line in enumerate(fileinput.input(f+'/simulation.input', inplace=1)):		
		if line.find("Component 1 MoleculeName") != -1:
			words = line.split()
			solute = words[3]
			sys.stdout.write(line.replace(solute, f))
		else:
			sys.stdout.write(line)
	subprocess.run(['sbatch raspajob', 'cd ../'], cwd=f, shell=True)

