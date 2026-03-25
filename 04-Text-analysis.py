"""
    - Count how many times each word appears
    - Output result as a dict
    - Ignore case sensitivity
"""

text = "Data pipeline are important because data is everywhere and data is growing"

lower_case = text.lower()

split_text = lower_case.split(' ')

new_list = {}
for word in split_text:
    if word in new_list:
        new_list[word] += 1
    else:
        new_list[word] = 1

print(new_list)
