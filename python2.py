#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max(a, b, c)

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

#Write a Python function called rev_string() to reverse a string.
def rev_string(s):
    return s[::-1]


#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(num, start, end):
    return start <= num <= end

# Example usage for max_num
print(max_num(1, 2, 3))  # Output: 3

# Example usage for mult_list
print(mult_list([1, 2, 3, 4]))  # Output: 24

# Example usage for rev_string
print(rev_string("hello"))  # Output: "olleh"

# Example usage for num_within
print(num_within(3, 2, 4))  # Output: True
print(num_within(3, 1, 3))  # Output: True
print(num_within(10, 2, 5)) # Output: False

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal():
	#your code here

pascal(1)
'''
output:
1
'''

pascal(5)
'''
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''                                                              