#Task1
#string manipulation

def first2last2(SampleString):
    if len(SampleString) < 2:
         return " " 
    
    else: return SampleString[0:2]+SampleString[-2:]
     
print(first2last2("helloworld"))
print(first2last2("my"))
print(first2last2("x"))

#Task 1 refactored without functions
# Input string from the user
samplestr = input("Please type a string: ")

# Check the length of the string
if len(samplestr) < 2:
    result = ""
else:
    # concatenation of first 2 letters & last 2 letters
    result = samplestr[:2] + samplestr[-2:]

# Print the result
print("Result:", result)

#Output check

#Please type a string: helloworld
#Result: held

#Please type a string: my
Result: mymy

#Please type a string: x
Result: 




#Task 2
#The valid phone number program.

randomstring = '2345675467'
if randomstring.isdigit() and len(randomstring) == 10:
    print('the string is in the right format for a phone number')
else: 
print('the string needs formatting')

#Task 3
#The math quiz program.

user_input = int(input("multiply 14 by 79, then substract 17: "))
if user_input == 1089:
    print("thank you. It's a valid answer")
else: print("unfortunately, the answer is incorrect")

#Task 4 
#The name check.

name = 'username'
username = input("Please, enter name Username here: ")
if username.lower() == name:
    print(True) 
