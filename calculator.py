

import sys

def sum ( a, b ):
	return a+b

def substraction ( a,  b):
	return a-b

def multiplication ( a, b):
	return a*b

def divide ( a, b):
	return a/b

def main ():
	i=0
	while i==0 :
		number_1 = int(input ( "Enter the first number:" ))

		operation = input ( "Enter an operation:" )

		number_2 = int(input ( "Enter the second number:" ))

		if operation == "+":
			result = sum (number_1, number_2)
		elif operation == "-":
			result = substraction ( number_1, number_2)
		elif operation == "*":
			result = multiplication ( number_1, number_2 )
		elif operation == "/":
			result = divide ( number_1, number_2 )
		else:
			print ( "invalid operation" )

		print("Eredmény: ", result)

		Exit = input( "Exit : Press e letter " )

		if Exit == "e":
			i=1
			sys.exit()
main()
