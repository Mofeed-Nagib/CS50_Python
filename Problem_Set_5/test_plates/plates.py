def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0:2].isalpha():
        return False
    elif len(s) > 2 and not s[2:].isalnum():
        return False
    
    flag = False
    for char in s[2:]:
        if not flag and char == "0":
            return False
        elif flag and char.isalpha():
            return False
        elif char.isdigit():
            flag = True
    return True


if __name__ == "__main__":
    main()