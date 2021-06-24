num = int(input("Enter the pyramid size : "))
symbol = input("Enter a symbol : ")
for i in range(num+1,0, -1):
    for j in range (0, i-1):
        print("",symbol,end="")

    print("\r")
