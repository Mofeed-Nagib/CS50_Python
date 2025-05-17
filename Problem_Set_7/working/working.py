import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"((?:\d|1[0-2])(?::[0-5][0-9])?) ([AP]M) to ((?:\d|1[0-2])(?::[0-5][0-9])?) ([AP]M)", s):
        if ":" in matches.group(1):
            start_hour, start_minute = matches.group(1).split(":")
        else:
            start_hour, start_minute = matches.group(1), "00"
        
        if ":" in matches.group(3):
            end_hour, end_minute = matches.group(3).split(":")
        else:
            end_hour, end_minute = matches.group(3), "00"
        
        if matches.group(2) == "PM" and start_hour != "12" or matches.group(2) == "AM" and start_hour == "12":
            start_hour = (int(start_hour) + 12) % 24
        
        if matches.group(4) == "PM" and end_hour != "12" or matches.group(4) == "AM" and end_hour == "12":
            end_hour = (int(end_hour) + 12) % 24

        return f"{int(start_hour):02}:{start_minute} to {int(end_hour):02}:{end_minute}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()