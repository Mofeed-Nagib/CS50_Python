import random


def main():
    level = get_level()
    correct = 10

    for _ in range(10):
        guesses = 0
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        total = num1 + num2

        while guesses < 3:
            try:
                guess = int(input(f"{num1} + {num2} = "))
                if guess == total:
                    break
            except ValueError:
                pass

            print("EEE")
            guesses += 1

        if guesses == 3:
            print(f"{num1} + {num2} = {total}")
            correct -= 1

    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                break
        except ValueError:
            pass
    return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()