print ("Program to print all prime numbers within a range")

a = int(input("Enter min value : "))
b = int(input("Enter max value : "))

prime = False

if a < b :
	for i in range (a,b+1):
		if i > 1:

			for j in range(2, i):
				if (i % j) == 0:
					prime = False
					break

			else :
				prime = True
			if prime == True:
				print(i)
			
else :
	print("Error!")
