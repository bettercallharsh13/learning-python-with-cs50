expression = input("expression : ")
x, y, z = expression.split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(round(float(x + z), 1))

elif y == "/":
    print(round(float(x / z), 1))

elif y == "*":
    print(round(float(x * z) ,1))

else:
    print(round(float(x - z) ,1))

