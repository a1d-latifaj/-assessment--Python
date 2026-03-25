"""
Use .map() to transform a list of numbers 
"""

numbers = [1,2,3,4,5,6,7,8,9]

squared_numbers = list(map(lambda n: n**2, numbers))

print(f"List of numbers: {numbers}")
print(f"List of squared numbers: {squared_numbers}")
