camelCase = input("camelCase: ")
snake_case = ""

for i in camelCase:
    if i.isupper():
        snake_case += "_"
    snake_case += i.lower()

print(f"snake_case: {snake_case}")