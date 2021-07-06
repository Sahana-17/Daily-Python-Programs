def permute(data, i, length):
    if i==length:
    	if data[0] == 0:
			print("error")
	else:
			print(''.join(data) )
    else:
        for j in range(i,length):
            #swap
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]


string = input("Enter string of different numbers : ")
n = len(string)
data = list(string)
permute(data, 0, n)
