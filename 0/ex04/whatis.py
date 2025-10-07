import sys

try:
	assert len(sys.argv) == 2, "Assertion Error: more than one argument is provided"
	number = sys.argv[1]
	assert type(number) is not int, "Assertion Error: argument is not an integer"
	if int(number) % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")

except AssertionError as error:
	print(error)	