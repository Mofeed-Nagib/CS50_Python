while True:
    fraction = input("Fraction: ")
    fraction = fraction.split("/")
    try:
        x = int(fraction[0])
        y = int(fraction[1])
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if x <= y:
            break

percentage = round(x / y * 100)

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")