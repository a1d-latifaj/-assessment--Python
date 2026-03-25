"""
    values = ["12", "25","error","40","None","60"]

    Write code to:
        - Convert valid numeric values to integeres
        - Skip invalid entries
        - Return the cleaned list
"""

values = ["12", "25","error","40","None","60"]
new_list = [] 

for value in map(lambda v: int(v) ,filter(str.isnumeric, values)):
    new_list.append(value)

print(f"Values list: {values}")
print(f"New list:    {new_list}")

print(f"\nElementi 0 ne Values: {type(values[0])}")
print(f"Elementi 0 ne New_list: {type(new_list[0])}")
