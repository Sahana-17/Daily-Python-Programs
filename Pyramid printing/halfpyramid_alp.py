#Prints half pyramid of alphabets
num = int(input("Enter the pyramid size : "))
for i in range(1, num+1):
    for j in range (1, i+1):
        print(chr(ord('A')+i-1), end="")
    print("\r")
