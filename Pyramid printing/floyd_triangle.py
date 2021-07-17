#Prints Floyd's triangle

line = int(input("Enter number of lines : "))
num = 1

for i in range(1, line + 1):
    for j in range(1, i + 1):        
        print(num, end = '  ')
        num = num + 1
    print()
