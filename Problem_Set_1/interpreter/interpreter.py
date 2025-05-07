expression = input("Expression: ")

x, y, z = expression.split()

x = int(x)
z = int(z)

if y == "+":
    x += z
elif y == "-":
    x -= z
elif y == "*":
    x *= z
else:
    x /= z

print(f"{x:.1f}")