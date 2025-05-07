def main():
    x = convert(input("What time is it? "))
    
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    return float(hour) + float(minute) / 60


if __name__ == "__main__":
    main()