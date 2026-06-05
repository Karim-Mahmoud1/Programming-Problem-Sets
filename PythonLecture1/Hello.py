name = input("Enter a name : ")
age = input("Enter an age : ")
print ("Hello my name is " + name + ", My age is " + '"' + age + '"' , sep="SSS", end="\n")
print("This is a string")
print(f"Hello my name is {name} and my age is {age}") #formatted string
print(f'Hello my name is {name} and my age is "{age}"')
print(f"Hello my name is {name} and my age is \"{age}\"")
name = name.strip()
print(name)
first, last = input("Enter name : ").split()

print(first)
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

sum = num1 + num2
print(sum)
