#Prints inverted half pyramid of alphabets

num = int(input("Enter the pyramid size : "))
for i in range(num+1,0, -1):
    for j in range (0, i-1):
        print(chr(ord('A')+i-2), end="")

    print("\r")
