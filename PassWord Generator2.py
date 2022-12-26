#Importing the random module
import random

# Defining the function of the password generator
def pass_gen(n,first_char):
    password=""
    password=first_char
    for i in range(1,len0):
        b=random.randint(0,3)
        if b==0:
            ind=random.randint(0,len(lower)-1)
            password+=lower[ind]
        if b==1:
            ind=random.randint(0,len(upper)-1)
            password+=upper[ind]
        if b==2:
            ind=random.randint(0,len(digits)-1)
            password+=digits[ind]
        else:
            ind=random.randint(0,len(spchars)-1)
            password+=spchars[ind]
    for j in password:
        if j in lower:
            pass
        elif j in upper:
            pass
        elif j in digits:
            pass
        elif j in spchars:
            pass
        else:
            pass_gen(len0,first_char)
    print("Your Password is:",password[:len0])

''' Main program of the password generator '''

#Initiating a string of all lowercase alphabets.
lower="abcdefghijklmnopqrstuvwxyz"

#Initiating a string with uppercase alphabets.
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Initiating a string with all the digits i.e. 0-9
digits="0123456789"

#Initiating a string with all the special characters.
spchars="~!@#$%^&*()_-+=-/{}[]\|,.;:"

#Welcome message for the user
print("*=======================*")
print("|| Password Generator  ||")
print("||*********************||")
print("||   * Made by:        ||")
print("||      Pushpam Kumar* ||")
print("||                     ||")
print("||                     ||")
print("*=======================*")
print("")

#About the password generator
about0=input("Enter \"about\" to know about Password Generator! ")

if about0.lower()=="about":
    print("-> This passwrod generator has been made by Md Faizan, Rohit Kumar and Sainath Reddy for the end-term project of INT-108")
    print("-> It genearates a password consisting of special characters, upper and lower case alphabets and numbers.")
    print("-> It takes the length of the password as input from the user and generate a strong password.")
    print("")
else:
    print("Invalid input!")
    print("")
    pass

#Starting the password generator on user command
start=input("Enter \"start\" to start creating your password! ")

if start.lower()=="start":
    print("*NOTE* Minimum length of password should be 12!")
    #Taking length of password as input from the user
    len0=int(input("Enter length of password!"))
    if len0>11:
        #Calling thge password generator function
        first_char=input("Enter character to start your password with: ")
        pass_gen(len0,first_char)
        print("Thank You for using :)")
    else:
        print("Entered password length is less than the minimum length!")
        print("Please restart the program!")
else:
    print("Invalid input!")
    pass
c=input("Enter any character to exit!")

