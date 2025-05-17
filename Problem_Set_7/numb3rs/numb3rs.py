import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for num in matches.groups():
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()