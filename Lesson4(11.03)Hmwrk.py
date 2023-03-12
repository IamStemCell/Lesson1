#Task1
#string manipulation

def first2last2(SampleString):
    if len(SampleString) < 2:
         return " " 
    
    return SampleString[0:2]+SampleString[-2:]
     
print(first2last2("helloworld"))
print(first2last2("my"))
print(first2last2("x"))


Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical 
characters and is only 10 characters long
. Print a suitable message depending on the outcome of the string evaluation.


Task 3

The math quiz program.

Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.

 

Task 4

name = 'svitlana'
username = input("Please, enter your name: ") 
if username.lower() == name:
    print(True) 

