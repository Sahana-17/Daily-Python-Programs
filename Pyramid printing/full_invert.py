num = int(input("Enter the pyramid size : "))
symbol = input("Enter a symbol : ")
space = 2

for i in range(num+1, 0, -1):
    for j in range(1, space-1):
        print(end=" ")
    space = space +2
    i = (2*i) -1
    for j in range (1, i-1):
        print("",symbol, end="")

    print("\r")
