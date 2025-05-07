def main():
    print(convert(input()))

def convert(text: str):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()