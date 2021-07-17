#Prints invertted half pyramid of inputted symbol
num = int(input("Enter the pyramid size : "))
symbol = input("Enter a symbol : ")
for i in range(num+1,0, -1):
    for j in range (0, i-1):
        print(chr(ord('A')+i-1),end="")

    print("\r")
