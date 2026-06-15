import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

secret_number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue 
            
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break 
            
    except ValueError:
        pass