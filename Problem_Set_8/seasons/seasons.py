from datetime import date, datetime
import inflect
import sys


def main():
    print(age_minutes(input("Date of Birth: ")))


def age_minutes(dob):
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")

    if birth_date > date.today():
        sys.exit("Invalid date")

    age = date.today() - birth_date
    minutes = age.days * 24 * 60

    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


if __name__ == "__main__":
    main()
