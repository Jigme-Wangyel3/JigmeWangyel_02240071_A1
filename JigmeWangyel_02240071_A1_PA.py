#Intro
print("From the given Funtions, choose the function you want to pick with the number (1-6) matching the function")
functions = ["(1).Prime Number Sum Calculator","(2).Length Unit Converter","(3).Consonent Counter","(4).Min-max Number Finder","(5).Palindrome Checker","(6).Word Conter"]
for item in functions:
    print(item)
x = int(input("Please enter a number from (1)-(6) as according to the function you want!: "))
print(x)
#Prime number sum Calculator
if x == 1:
    p1 = int(input("Please enter what range you want to start from!(Doesn't have to be a Prime Number!): "))
    p2 = int(input("Please enter till where you want to end the prime number at! (It doesn't have to be a prime number!): "))
    if p1 and p2 < 2:
        print ("The Prime Number has to be Greater than 2!")
        print("The sum of the prime numbers you took in range is : " )
    print("The sum of the Prime numbers within your given range is!: ")
#Length unit converter
if x == 2:
    print("Please select a unit to convert as follows")
    L = input("'M' for Meter to Feet | and | F for Feets to Meter: ")
    print(L)
    if L.upper() == "M":
        c = float(input("Put the length in meter unit to convert it into Feet!: "))
        l = c*3.28

        print(str(c) +" meters " " In feet is!: " + str(l) + " Feet!" )
    elif L.upper()== "F":
        d = float(input("Please enter the length in feet to convert it to meters!: "))
        f_m = d*0.3048
        print("The length "+ str(d) + " Feet" + " in meter is!: " + str(f_m) + " Meters!")
    else:
        print("Type 'M' or 'F'! to convert to respective units! ")
    #4231