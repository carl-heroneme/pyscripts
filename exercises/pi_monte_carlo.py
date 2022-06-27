from random import uniform

n = int(input("How many iterations?: "))

test = []

total = 0
accept = 0

for i in range(n): 

	random_x = uniform(0.000, 1.000)

	random_y = uniform(0, 1)

#if y <= sqrt(1-x^2) then the value is accepted, otherwise it is rejected and the total is updated	

	if random_y <= (1 - random_x ** 2) ** 0.5:
		accept = accept + 1
		total = total + 1
	else:
		total = total + 1 
#the ratio of the area of a circle to a square containing it is pi/4, so pi = the ratio * 4

pi = ((accept / total) * 4)
print("Pi is approximately equal to: ")
print(str(pi))

with open("monte.txt", "a") as my_file:
	my_file.write(str(pi) + " " + str(n) + " ")
	my_file.write("\n")
	my_file.close()
