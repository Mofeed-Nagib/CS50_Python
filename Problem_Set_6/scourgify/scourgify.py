import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as file:
        students = []
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(students)