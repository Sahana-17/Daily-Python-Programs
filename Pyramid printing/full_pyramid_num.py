num = int(input("Enter the pyramid size : "))
space = (num*2)-1

for i in range(1, num+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space -2
    i = (2*i) -1
    for j in range (1, i+1):
        print("",i, end="")

    print("\r")
