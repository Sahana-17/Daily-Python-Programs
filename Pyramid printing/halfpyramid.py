#Prints half pyramid of inputted symbol
num = int(input("Enter the pyramid size : "))
symbol = input("Enter a symbol : ")
for i in range(1, num+1):
	
	for j in range (1, i+1):
		
			print("",symbol, end=" ")
		
	print("\r")
	
