#Prints half pyramid of numbers

num = int(input("Enter the pyramid length : "))

for i in range(1, num+1):
    for j in range (1, i+1):
        print("",j, end="")
    print("\r")
