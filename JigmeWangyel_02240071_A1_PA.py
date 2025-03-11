def main():
    while True:
        # Intro
        functions = ["(1).Prime Number Sum Calculator","(2).Length Unit Converter","(3).Consonent Counter","(4).Min-max Number Finder","(5).Palindrome Checker","(6).Word Conter"]
        for item in functions:
            print(item)
        try:
            x = int(input("Please enter a number from (1)-(6) as according to the function you want!: "))
            if x < 1 or x > 6:
                print("Invalid input! Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Prime Number Sum Calculator
        if x == 1:
            print("You chose Prime Number Sum Calculator!")
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

        # Length Unit Converter
        elif x == 2:
            print("You chose Length Unit Converter")
            L = input("'M' for Meter to Feet | and | F for Feet to Meter: ").upper()
            if L == "M":
                c = float(input("Put the length in meters to convert it into feet: "))
                l = c * 3.28
                print(f"{c} meters in feet is: {l} feet!")
            elif L == "F":
                d = float(input("Please enter the length in feet to convert it to meters: "))
                f_m = d * 0.3048
                print(f"The length {d} feet in meters is: {f_m} meters!")
            else:
                print("Invalid input! Type 'M' or 'F' to convert to respective units.")

        # Consonant Counter
        elif x == 3:
            print("You chose Consonant Counter")
            def count_consonants(text):
                vowels = "AaEeIiOoUu"
                count = 0
                for char in text:
                    if char.isalpha() and char not in vowels:
                        count += 1
                return count

            text = input("Enter a text: ")
            consonant_count = count_consonants(text)
            print(f"The number of consonants in the text is: {consonant_count}")

        # Min-Max Number Finder
        elif x == 4:
            print("You chose Min-Max Number Finder!")
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

        # Palindrome Checker
        elif x == 5:
            print("You chose Palindrome Checker!")
            def is_palindrome(s):
                cleaned = ''.join(c.lower() for c in s if c.isalnum())
                return cleaned == cleaned[::-1]

            user_input = input("Enter a text: ")
            if is_palindrome(user_input):
                print("True")
            else:
                print("False")

        # Word Counter
        elif x == 6:
            print("You chose Word Counter!")
            text = input("Enter a text: ")
            word_count = len(text.split())
            print(f"The number of words in the text is: {word_count}")

        # Ask if the user wants to continue
        leave = input("Do you want to continue? (Y/N): ").upper()
        if leave != "Y":
            print("Goodbye!")
            break

# Run the program
main()