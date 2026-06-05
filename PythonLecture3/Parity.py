#parity.py
#Checks if a number is even or odd


def is_even(num):
    return True if num % 2 == 0 else False

def main():
    num = int(input("Enter a number: "))

    if is_even(num):
        print("Even")
    else:
        print("odd")

main()

