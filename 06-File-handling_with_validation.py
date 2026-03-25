"""
    Write a script that:
        - Reads a file
        - Finds 
            *total number of lines
            *longest line
        - Handles
            *file not found error
            *empty file
"""

try:
    with open(r"C:\Users\a1d-latifaj\OneDrive\Desktop\assessment\0-theoretical-questions.txt") as f:
        total_lines = f.readlines()
        if len(total_lines) == 0:
            print(f"File is empty")
        else:
            longest_line = "".strip()
            for line in total_lines:
                if len(line) > len(longest_line):
                    longest_line = line.strip()

            print(f"\nFile have {len(total_lines)} lines")
            print(f'The longest line have {len(longest_line)} characters')
            print(f'\n"{longest_line.strip()}"')
except:
    print('File not found')

