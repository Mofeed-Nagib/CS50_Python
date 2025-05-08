tweet = input("Input: ")
output = ""

for char in tweet:
    if char.lower() in ["a", "e", "i", "o", "u"]:
        continue
    output += char

print(f"Output: {output}")