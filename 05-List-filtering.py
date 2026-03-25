"""
- Return only numbers greater than 15    
"""

numbers = [5,10,15,20,25,30]

greater_than_15 = list(filter(lambda n: n>15, numbers))


print(f"All numbers: {numbers}")
print(f"Greater than 15 from numbers list: {greater_than_15}")
