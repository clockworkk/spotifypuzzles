#Philip Middleton
#Spotify Programming Puzzle
#Problem ID: reversebinary
#Reverse Binary with python

import sys

'''
reverse_numbers:
Takes in the binary number and converts it to a string.
Reverses the order of the string and then converts the new
reversed binary value into an integer and returns that integer.
'''
def reverse_numbers(number):
	number = str(number)
	number = number[::-1]
	number = int(number, 2)
	return number

'''
format_numbers:
Takes in a string representation of a number and converts it to an integer.
Converts the integer into the binary representation of that number.
Strips '0b' from the front of the binary number and returns the binary number.
'''
def format_numbers(number):
	number_to_int = int(number)
	binary_of_number = bin(number_to_int)
	binary_of_number = binary_of_number.replace('0b', '')
	return binary_of_number

'''
Read input from stdin
Send input to format_numbers
Send input to reverse_numbers
print results
'''
def main():
	number = sys.stdin.readline()
	number = format_numbers(number)
	number = reverse_numbers(number)
	print(number)
	

if __name__ == '__main__':
	main()