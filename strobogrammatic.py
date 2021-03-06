# Strobogrammatic number : number remains the same after a rotation of 180 degrees. Eg. 101

def gen_strobogrammatic(n):
	"""
	:type n: int
	:rtype: List[str]
	"""
	result = helper(n, n)
	return result


def helper(n, length):

	if n <= 0:
		return ["Error"]
	if n == 1:
		return ["1", "0", "8"]
	middles = helper(n-2, length)
	result = []
	
	for middle in middles:
		if n != length:
			result.append("0" + middle + "0")
		result.append("8" + middle + "8")
		result.append("1" + middle + "1")
		result.append("9" + middle + "6")
		result.append("6" + middle + "9")
	return result

n = int(input("enter length of num : "))

print(gen_strobogrammatic(n))
