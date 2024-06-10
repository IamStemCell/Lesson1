#Task1
#string manipulation

def first2last2(SampleString):
    if len(SampleString) < 2:
         return " " 
    
    else: return SampleString[0:2]+SampleString[-2:]
     
print(first2last2("helloworld"))
print(first2last2("my"))
print(first2last2("x"))


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
