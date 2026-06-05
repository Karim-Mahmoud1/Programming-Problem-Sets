#taking the input of name from the user
name = input("Enter a name : ").split() #== means comparison, = means assignment

#saying hello to that name
print("Hello", name)

'''


This is a multi line comment


'''

#PSEUDOCODE
#1. Ask a person their name
#2. Increment count by +1
#3. Ask next person their name
#4. Increment count by +1

#5. Loops: Repeat step 1 and step 2 until no new name exists
#Write PSEUDOCODE FIRST, THEN CODE

Name = input("Enter name : ")
Age = input("Enter age : ")
Course = input("Enter course : ")
print("Hello",'"'+Name+'"'+", your age is " +Age+" and you are studying " +Course+".", sep="") #concatenation    

print(f"Hello my name is {Name} and my age is {Age} and I am studying {Course}") #string formatting

print("Hello, \"Friend\"") 
'''
syntax error, because of the double quotes inside the string
To fix this, we can use single quotes to define the string,
or we can escape the double quotes using a backslash (\)
 
'''

'''
String methods:
1. strip() - removes leading and trailing whitespace
2. title() - converts the first character of each word to uppercase and the rest to lowercase
3. capitalize() - converts the first character of the string to uppercase and the rest to lowercase
4. upper() - converts all characters in the string to uppercase
5. lower() - converts all characters in the string to lowercase
6. split() - splits the string into a list of substrings based on a specified delimiter (default is whitespace)
7. join() - joins a list of strings into a single string using a specified delimiter'''

#write a function like strip which will remove whitespaces between two words
#limit it to only one white space which exists between two words

first,middle,last = input("Enter name : ").split() #split the input into first, middle, and last name based on whitespace
print(middle)

#Write a function that adds two numbers

num1 = input("Enter num1 : ")
num2 = input("Enter num2 : ")
sum = num1 + num2
print(sum) #this will concatenate the two numbers as strings

#To fix this, we need to convert the input strings to integers before adding them

sum1= int(num1) + int(num2)
print(sum1)

num3 = int(input("Enter num3 : "))
num4 = int(input("Enter num4 : "))
sum2 = num3 + num4
print(sum2)

#it can all also be done in one line
print(int(input("Enter num5 : ")) + int(input("Enter num6 : ")))

print(int(input("Enter num7 : ") + input("Enter num8 : "))) #this will concatenate the two inputs as strings and then try to convert the concatenated string to an integer, which will result in a ValueError if the concatenated string is not a valid integer.

num9 = float(input("Enter num9 : ")) #int numbers can also be added to float numbers, but the result will be a float number. float = decimal numbers
num10 = float(input("Enter num10 : "))
sum5 = num9 + num10
print(sum5) 

#write function that adds two float numbers and rounds to 3rd decimal place
num11 = float(input("Enter num11 : "))
num12 = float(input("Enter num12 : "))
sum6 = num11 + num12
print(round(sum6, 3))

#why was the answer not rounded to 3 decimal places?
'''
The round() function rounds a number to a specified number of decimal places, but it does not 
change the underlying value of the number. The result of round(sum6, 3) is a float with 3 
decimal places, but when you print it, it may still display more than 3 decimal places due 
to the way floating-point numbers are represented in Python. To ensure that the output is 
displayed with only 3 decimal places, you can use string formatting:
'''
print(f"{round(sum6, 3):.3f}") #this will format the output to 3 decimal places

q = num11/num12
print(f"{q:.3f}") #this will format the output to 3 decimal places

def hello(name = "class"): #0x234
    print("Hello", name)

name = input("Enter name : ") #0x123

hello(name)

#add
def add(num15, num16):
    return num15 + num16

#sub
def sub(num15, num16):
    return num15 - num16
#mul
def mul(num15, num16):
    return num15 * num16
#div
def div(num15, num16):
    return num15 / num16
#modulus
def mod(num15, num16):
    return num15 % num16

num15 = int(input("Enter num15 : "))
num16 = int(input("Enter num16 : "))

sum = add(num15, num16)
diff = sub(num15, num16)
product = mul(num15, num16)
quotient = div(num15, num16)
remainder = mod(num15, num16)
print(sum)
print(diff)
print(product)
print(quotient)
print(remainder)

def main():
    num15 = int(input("Enter num15 : "))
    num16 = int(input("Enter num16 : "))

    sum = add(num15, num16)
    diff = sub(num15, num16)
    product = mul(num15, num16)
    quotient = div(num15, num16)
    remainder = mod(num15, num16)
    print(sum, diff, product, quotient, remainder) 

main()
   