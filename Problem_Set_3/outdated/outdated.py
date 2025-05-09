months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    
    if "," in date:
        try:
            rest, year = date.split(", ")
            month, day = rest.split(" ")
            month = str(months.index(month) + 1)
            if int(year) > 0 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except ValueError:
            pass     
    elif "/" in date:
        try:
            month, day, year = date.split("/")
            if int(year) > 0 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except ValueError:
            pass

print(f"{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}")