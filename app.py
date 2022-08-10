def decimal_to_binary(decimal):
	result = bin(decimal).replace("0b", "")
	return result

if __name__ == "__main__":
	binary = decimal_to_binary(23)
	print(binary)

def exclusive_or(num1, num2):
	pass