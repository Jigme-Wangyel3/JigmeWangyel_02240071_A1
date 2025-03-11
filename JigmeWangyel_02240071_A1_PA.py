#Intro
print("From the given Funtions, choose the function you want to pick with the number (1-6) matching the function")
functions = ["(1).Prime Number Sum Calculator","(2).Length Unit Converter","(3).Consonent Counter","(4).Min-max Number Finder","(5).Palindrome Checker","(6).Word Conter"]
for item in functions:
    print(item)
x = int(input("Please enter a number from (1)-(6) as according to the function you want!: "))
print(x)
#Prime number sum Calculator
if x == 1:
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_primes_in_range(start, end):
        if start < 2:
            raise ValueError("Starting number must be at least 2.")
        
        prime_sum = sum(n for n in range(start, end + 1) if is_prime(n))
        return prime_sum

    try:
        start = int(input("Enter the starting number of the range: "))
        end = int(input("Enter the ending number of the range: "))
        result = sum_primes_in_range(start, end)
        print(f"The sum of prime numbers between {start} and {end} is {result}.")
    except ValueError as e:
        print(f"Error: {e}")
  
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
#Consonent counter
if x== 3:
    def Consonents(Text):
        Vow=("AaEeIiOoUu")
        count = 0
        
#Min-Max Number Finder
if x == 4:
    try:
        count = int(input("Enter how many numbers you want to input: "))
        if count <= 0:
            raise ValueError("The count must be a positive integer.")
        
        numbers = []
        for i in range(count):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        
        min_num = min(numbers)
        max_num = max(numbers)
        
        print(f"Minimum number: {min_num}")
        print(f"Maximum number: {max_num}")
    except ValueError as e:
        print(f"Error: {e}")


   
    
