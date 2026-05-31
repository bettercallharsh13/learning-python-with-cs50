camel = input("camel case: ")
snake = ""

for letter in camel:
    if letter.isupper():
        snake += "_"
        snake += letter.lower()
    else:
        snake += letter


print("snake_case: ", snake)
