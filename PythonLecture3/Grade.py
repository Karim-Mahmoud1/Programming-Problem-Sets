#grade.py
#score (input)
# 90 - 100 : A
# 80 - 89 : B
# 70 - 79 : C 
# 60 - 69 : D
# 50 - 59 : E
# Less than 50 : F

score = int(input("Enter score:")) #make it so user can't input a score less than 0 or greater than 100
while score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    score = int(input("Enter score:"))

if  90 <= score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
elif score >= 50 and score < 60:
    print("Grade: E")
else:
    print("Fail: F")


