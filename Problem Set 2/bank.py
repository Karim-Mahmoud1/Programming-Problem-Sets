Greeting = input("Greeting: ").strip()
if Greeting.lower().startswith("hello"):
    print("$0")
elif Greeting.lower().startswith("h"):
    print("$20")
else:
    print("$100")