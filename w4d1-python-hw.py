import re

with open("names.txt") as x:
    data = x.readlines()

        
pattern_name_twitter = re.compile(r'([\w\s-]+), ([\w\s-]+)\s+([\w+@]+\w+)\s+.*\s+@([\w]+)$')


for line in data:
    match = pattern_name_twitter.search(line)
    if match:
        first_name = match.group(2)
        last_name = match.group(1)
        twitter_handle = "@" + match.group(4)
        full_name = f"{first_name} {last_name}" 
        print(f"{full_name} / {twitter_handle}")




# Regex project
# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)
# Hint: use with open() and readlines()


"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""



# import re

with open("regex_test.txt") as x:
    data = x.readlines()

pattern_name = re.compile(r'([A-Z][a-z]+) ([A-Z][a-z]*)(?: ([A-Z][a-z]+))?$')

for line in data:

    match = pattern_name.search(line)

    if match:

        first_name = match.group(1)

        middle_name = match.group(2) 

        last_name = match.group(3) if match.group(3) else " "

        print(f"{first_name} {middle_name} {last_name}")

       

    else:

        print("None")
