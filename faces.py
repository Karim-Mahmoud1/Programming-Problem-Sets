def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input("Input : ")
    print(convert(user_input))

main()

