print ("Program to print all prime numbers within a range")

a = int(input("Enter min value : "))
b = int(input("Enter max value : "))

if a < b :
	for i in range (a,b+1):
		if i > 1:

			for j in range(2, i):
				if (i % j) == 0:
					break
			else:
				print(i)
else :
	print("Error!")
