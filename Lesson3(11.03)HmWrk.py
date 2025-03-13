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


#Task 3 ref simple prints and not input/function just practice of type casting

#values into variables
a = 8 
b = 6 

#Print the result for each operation
print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)           # Regular division
print("Exponent (Power): ", a ** b)  # a raised to the power of b
print("Modulus: ", a % b)            # Remainder of the division, modulo
print("Floor Division: ", a // b)    # Division that rounds down


#output

#Addition:  13
#Subtraction:  7
#Multiplication:  30
#Division:  3.3333333333333335
#Exponent (Power):  1000
#Modulus:  1
#Floor Division:  3
