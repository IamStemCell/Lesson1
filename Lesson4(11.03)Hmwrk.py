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

name = svitlana
username = input("Please, give your name: ") #my attempt 
if username.lower() == name 
    return True 
print(return) 

The name check.

Write a program that has a variable with
 your name stored (in lowercase) 
and then asks for your name as input. 
The program should check if your input is equal to the stored 
name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, 
it should return True.
