text = input("Input: ")
result = ""

for letter in text:
    if letter not in "aioueAIOUE":
        result += letter

print("output: ", result)

