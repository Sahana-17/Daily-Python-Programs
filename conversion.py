#Python program to convert input form (decimal, binary, hexadecimal, octal) to another output form

input_form = input("Choose the form of input- d/b/o/h : ")

form = False

while form == False :

	output_form = input("Choose a different form to convert the input to : ")
	if output_form != input_form:
		form = True

value = input("Enter input value : ")
if input_form == 'd':
	value_d = int(value)
	if output_form == 'b':
		output = bin(value_d).replace ("0b", "")
	
	if output_form == 'h':
		output = hex(value_d).split('x')[-1]		

	if output_form == 'o':
		output = oct(value_d)

if input_form == 'b':
	num = int(value, 2)
	if output_form == 'd':
		output = num
	if output_form == 'h':
		output = hex(num).split('x')[-1]
	if output_form == 'o':
		output = oct(num)

if input_form == 'h':
	num = int(value, 16)
	if output_form == 'd':
		output = num
	if output_form == 'b':
		output = bin(num).replace ("0b", "")

	if output_form == 'o' :
		output = oct(num)

if input_form == 'o':
	num = int(value, 8)
	if output_form == 'd':
		output= num
	if output_form == 'h':
		output = hex(num).split('x')[-1]
	if output_form == 'b':
		output = bin(num).replace ("0b", "")
print(output)
