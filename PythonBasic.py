# This is a sample Basic Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Execute String On terminal or Compiler

#we will Execute Our String Through print Function print() Its a Builten Function of python
print("Hello World") # This statement Execute ' Hello World ' on Terminal
print("My name is Adeel") # This statement Execute ' My name is Adeel ' on Terminal
print("I am a software developer") # This statement Execute ' I am a software developer ' on Terminal
# if any result whose data type Exept String then How to print That
a=5
print(f"{a} is a prime number")  # This statement Execute ' 5 is a prime number ' on Terminal


# Declaration of Variables

# In python we dont need For datatype its Auto generated
a="Sum of given value is" #string
b=9                       #int
c=4.5                     #float
print(f"{a} : {b+c}")  # This statement Execute ' Sum of given value is : 13.5 ' on Terminal

#How To take user input

# variable = datatype(Input function) => input() if You Want to Display input String Then u give String in input Function
input = int(input("Enter Number")) # for intiger value like 1,2,3,4,5,6,7
input = str(input("Enter String")) # for String like any sentence
input = float(input("Enter String")) # for float value like 1.8,2.6,3.3,4.2,5.5,6.0,7.3
input = chr(input("Enter String")) # for single  Charachter like a,b,c,d,e

#Condition if  else
a=5
b=6
if a>b: # check Whether a is greater then b then enter the if Body other wise Enter else Body
    #if Body
    # identation is mendotory to execution
    print(f"{a} is greater then {b}") # a is greter then b ' a_value is greter then b_value  ' on terminal
else:
    #else body
    # identation is mendotory to execution
    print(f"{b} is greater then {a}") # a is greter then b ' b_Value is greter then a_value  ' on terminal

# Other Example: For Elif
# a is ia user input Whose Data type is integer
if a == 0:  # check Whether a is Equal to 0 then enter the if Body other wise Enter elif Body
    # if Body
    # Some code
elif a == 1:  # if Condition is not Match in if Body then it come to elif and then check Whether a is Equal to 1 then enter the elif Body other wise Enter Else Body
    # elif body
    # Some code
else:
    # Else body
    # Some Code

# Other Example: For nested if
User = 'Adeel' # This Username Store in privately
pass = 123  # This pass Store in privately
# here input is Enter String through user
if inputUser ==  User:
    if inputpass == pass:
        print("login Sucessfully")
    else:
        print("Password is not match")
else:
    print("Username is not match")

# Other Example: For Multiple Conditions
User = 'Adeel' # This Username Store in privately
pass = 123  # This pass Store in privately
# here input is Enter String through user
# key Words
# and : and for use Both Condition Are true Then true Other Wise false
# or : or for use any one Condition Are true Then true Other Wise false
if inputUser ==  User and inputpass == pass:
    print("login Sucessfully")
else:
    print("login not Sucessfully")

# Thank You in next Repository i will teach you How to print Multi Statemnt thorugh loop



