grocery = {}

while True:
    try:
        item = input().strip().upper()
        grocery[item] += 1
    except KeyError:
        grocery[item] = 1
    except EOFError:
        print()
        break            

for key in sorted(grocery):
    print(f"{grocery[key]} {key}")