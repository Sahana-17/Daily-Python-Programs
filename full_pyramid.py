num = int(input("Enter the pyramid size : "))
symbol = input("Enter a symbol : ")
space = num -1

for i in range(1, num+1):
	for j in range(1, space+1):
		print(end=" ")
	space = space -1

	for j in range (1, i+1):
		print("",symbol, end="")
	print("\r")
