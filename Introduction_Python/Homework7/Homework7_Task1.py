import re

# Step 1

string = 'Hi. My name is Unurtuvshin. I am 18 years old.'

pattern = '[a-zA-Z0-9]'  # every alphanumeric character
result = re.findall(pattern, string)
print(result)

pattern = '[a-z]'  # every lowercase letters
result = re.findall(pattern, string)
print(result)

pattern = '[A-Z]'  # every uppercase letters
result = re.findall(pattern, string)
print(result)

pattern = '[0-9]'  # every digits
result = re.findall(pattern, string)
print(result)

# Step 2

pattern = '\d'  # every digits
result = re.findall(pattern, string)
print(result)

pattern = '\D'  # every nondigits
result = re.findall(pattern, string)
print(result)

pattern = '\w'  # every alphanumeric characters
result = re.findall(pattern, string)
print(result)

pattern = '\W'  # every nonalphanumeric characters
result = re.findall(pattern, string)
print(result)

pattern = '\s'  # every whitespace
result = re.findall(pattern, string)
print(result)

# Step 3

pattern = '^\w{2}'  # first 2 alphanumeric character
result = re.search(pattern, string)
print(result.group())

pattern = '\w{4}$'  # last 4 alphanumeric character
result = re.search(pattern, "There is a loooong striiiing")
print(result.group())

# consists of a nonspace character and at least length of 4 or 5 alhpanumeric character
pattern = '\S\w\w\w\w\w?'
result = re.findall(pattern, "There is a string consists123 of 70 characters.")
print(result)

pattern = '\S\w*'  # consist of a nonspace character and any length of alhpanumeric character
result = re.findall(pattern, "There is a string consists123 of 70 characters.")
print(result)

# consists of a nonspace character and at least length of 1 alhpanumeric character
pattern = '\S\w+'
result = re.findall(pattern, "There is a string consists123 of 70 characters.")
print(result)

# consists of any character, a nonspace character and an alhpanumeric character
pattern = '.\S\w'
result = re.findall(
    pattern, "There is a string consists123 \n of 70 characters.")
print(result)

# Step 4

pattern = "\w{2,4}"  # alphanumeric string of length 2 to 4
result = re.findall(pattern, "Hi. My name is Unurtuvshin.")
print(result)

pattern = "\w{,4}"  # alphanumeric string of length 0 to 4 \ Space included
result = re.findall(pattern, "Hi. My name is Unurtuvshin.")
print(result)

pattern = "\w{2,}"  # alphanumeric string of length more than 2
result = re.findall(pattern, "Hi. My name is Unurtuvshin.")
print(result)

pattern = "\w{2}"  # alphanumeric string of length 2
result = re.findall(pattern, "Hi. My name is Unurtuvshin.")
print(result)

# Step 5

# lookbehind

pattern = "(?<=\d{2})\s\w*"  # string after 2 digit
result = re.findall(pattern, "Hi. My name is Unurtuvshin. I am 18 years old.")
print(result)

# lookahead

pattern = "(?<=\s)\w*(?=\s\d{2})"  # string before a space and 2 digit
result = re.findall(pattern, "Hi. My name is Unurtuvshin. I am 18 years old.")
print(result)

# negative lookbehind

pattern = "(?<!\d{2})\s\w*"  # string after non 2 digit
result = re.findall(pattern, "Hi. My name is Unurtuvshin. I am 18 years old.")
print(result)

# lookahead

pattern = "(?<=\s)\w*(?!\s\d{2})"  # string before a space and non 2 digit
result = re.findall(pattern, "Hi. My name is Unurtuvshin. I am 18 years old.")
print(result)
