import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

rand_int = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess <= 0:
            pass
        elif guess == rand_int:
            print("Just right!")
            break
        elif guess > rand_int:
            print("Too large!")
        else:
            print("Too small!")