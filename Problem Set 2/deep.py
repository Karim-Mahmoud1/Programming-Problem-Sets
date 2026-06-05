Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

if Answer == "42" or Answer.lower() == "forty-two" or Answer.lower() == "forty two":
    print("Yes")
else:
    print("No")
