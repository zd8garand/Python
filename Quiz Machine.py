import random

'''

David Belmont
00288849
Mini Project
Quiz Machine

'''

#FUNTION DEFINITIONS
def remainder(a, b):
    compAnswer1 = (a % b)
    return compAnswer1

def product(a, b):
    compAnswer2 = (a * b)
    return compAnswer2

def division(a, b):
    compAnswer3 = (a / b)
    return compAnswer3
    
def power(a, b):
    compAnswer4 = (a ** b)
    return compAnswer4

def computegrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
#VARIABLES
randomInt1 = random.randint(1, 10)
randomInt2 = random.randint(1, 10)
randomInt3 = random.randint(1, 10)
randomInt4 = random.randint(1, 10)
score = float(0.00)
correct = int(0)

#START QUIZ
name = str(input("Greetings! What is your name? "))
print("Hello", name)
answer = str(input("Would you like to take a quiz? (y,n) "))
if answer == 'n':
    print("Ok bye!")
    quit()
else:
    print("Ok let us begin!")
    
print("We are going to test your mathematics skills. \
Answer the following questions.")


print("What is the remainder of", randomInt1, "%", randomInt2, "?")#Question 1
userAnswer1 = int(input())
compAnswer1 = remainder(randomInt1, randomInt2)#Calls mod fuction test


if userAnswer1 == compAnswer1:#Will test user answer and award 23 points if correct
    score = score + 23.00
    correct = correct + 1#Adds a point to number of correct
    print("Correct!")
else:
    print("Incorrect! The answer is", compAnswer1)
    

print("What is the product of", randomInt1, "*", randomInt2, "?")#Question 2
userAnswer2 = int(input())
compAnswer2 = product(randomInt1, randomInt2)#Calls product fucntion test

if userAnswer2 == compAnswer2:#Will test user answer and award 14 points if correct
    score = score + 14.00
    correct = correct + 1#Adds a point to number of correct
    print("Correct!")
else:
    print("Incorrect! The answer is", compAnswer2)
    
    
print("Use integer division to answer the following:", randomInt3, "/", randomInt4, "?")#Question 3
userAnswer3 = int(input())
compAnswer3 = division(randomInt3, randomInt4)#Calls division fucntion test

if userAnswer3 == compAnswer3:#Will test user answer and award 31 points if correct
    score = score + 31.00
    correct = correct + 1#Adds a point to number of correct
    print("Correct!")
else:
    print("Incorrect! The answer is", compAnswer3)


print("What is the result of", randomInt3, "raised to the power of", randomInt2, "?")#Question 4
userAnswer4 = int(input())
compAnswer4 = power(randomInt3, randomInt2)#Calls power fucntion test

if userAnswer4 == compAnswer4:#Will test user answer and award 32 points if correct
    score = score + 32.00
    correct = correct + 1#Adds a point to number of correct
    print("Correct!")
else:
    print("Incorrect! The answer is", compAnswer4)
    

print("Alright", name, "let us see how you did...")
print("Correct answers:", correct, "of 4")
print("Score:", score," of 100 points (", score, "% of 100%)")
print("Grade:", computegrade(score))#Function called to calculate score to letter grade


