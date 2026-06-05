#house.py
# name = Harry, Hermoine, Ron, Draco
# house = Gryffindor, Gryffindor, Gryffindor, Slytherin
name = input("Enter name: ").strip().title()

if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

match name:  #this is called a match case statement, it's like a switch case statement in other languages
    case "Harry" | "Hermoine" | "Ron":  #this is called a pattern, it checks if the name is Harry, Hermoine, or Ron
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")