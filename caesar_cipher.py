def cipher(plain_text, shift):
	result = ""

	y = len(plain_text)
	for i in range(y):  
		char = plain_text[i]  
		flag = char.isalpha() 

		if flag == True:

			if (char.isupper()):  
				result += chr((ord(char) + shift - 64) % 26 + 64)  
			else:  
				result += chr((ord(char) + shift - 96) % 26 + 96)  

		else:
			result += char
	return result  
  
plain_text = input("Enter string : ")  
shift = int(input("Enter shift value : "))

print("Cipher: " + cipher(plain_text, shift))  
