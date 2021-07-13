#def cipher(plain_text, shift):
	result =""

	y = len(plain_text)
	for i in range(y):  
		char = plain_text[i]  
        
		if (char.isupper()):  
			result += chr((ord(char) + shist - 64) % 26 + 65)  
		else:  
			result += chr((ord(char) + shift - 96) % 26 + 97)  
	return result  
  
plain_text = input("Enter string : ")  
shift = int(input("Enter shift value : "))

print("Cipher: " + cipher(plain_text, shift))  
