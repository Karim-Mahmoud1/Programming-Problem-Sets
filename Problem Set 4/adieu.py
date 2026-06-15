import inflect
import sys

p = inflect.engine()
names = []

while True:
    try:
        name = input()
        names.append(name)
    except EOFError:
        
        print()
        break


formatted_names = p.join(names)

print(f"Adieu, adieu, to {formatted_names}")