#Task1 
#The greeting program.

name = "IamStemCell"
day = "Saturday"
#1 way using arguments of print function
print ("Good day",name,"!",day,"is a perfect day to learn some python.")
#2 way using formatting string 
print("Good day {}! {} is a perfect day to learn some python.".format(name,day))
#3 way using concatenation
print("Good day " + name + "! " + day + " is a perfect day to learn some python.")

#4 f-formatting string
print(f"Good day {name}! {day} is a perfect day to learn some python.")


#Task 2
#Manipulate strings.

first_name = "iamstemm"
last_name = "cell"

print("Hello, " + first_name.title() + " " + last_name.title())


#Task 3 
#Using python as a calculator.

a = 8
b = 6
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print (a**b)
print (a%b)
print (a//b)
