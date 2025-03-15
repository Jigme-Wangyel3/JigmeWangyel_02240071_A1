while True:
    Options = ["1.Guess the Number Game!","2.Rock paper Scissor game","3.Exit The Game!"]
    for items in Options:
        print(items)
    X = int(input("Choose The game you want according the number or you can Exit the Game!: "))
    #Guess number Game
    if X==1:
        import random

        def number_guesser():
            number_for_guessing = random.randint(1, 100)
            attempts = 0

            print("Hello! You chose guess the Number Game")
            print("The Number Lies Between 1 and 100!")
            
            while True:
                try:
                    user_guess = int(input("Enter your guess here!: "))
                    attempts += 1

                    # Checking if the guess is correct
                    if user_guess < number_for_guessing:
                        print("The value You have input is too Low! Try putting in your value Again! ")
                    elif user_guess > number_for_guessing:
                        print("The value You have input is too High! Try putting in your value Again! ")
                    else:
                        print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
                        break
                except ValueError:
                    print("Please enter a valid number between 1-100!")

        # Start the game
        number_guesser()
    elif X==2:
        print("You Chose Rock, Paper and Scissors Game! ")
        import random

        def random_choice():
            return random.choice(['rock', 'paper', 'scissors'])

        def winning_moment(player, computer):
            if player == computer:
                return "It's a tie!"
            elif (player == 'rock' and computer == 'scissors') or \
                (player == 'scissors' and computer == 'paper') or \
                (player == 'paper' and computer == 'rock'):
                return "You win!"
            else:
                return "Computer wins!"

        def main():
            while True:
                choice_of_player = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
                if choice_of_player == 'quit':
                    print("Thanks for playing!")
                    break
                if choice_of_player not in ['rock', 'paper', 'scissors']:
                    print("Invalid choice, try again.")
                    continue
                
                choice_of_computer = random_choice()
                print(f"Computer chose: {choice_of_computer}")
                print(winning_moment(choice_of_player, choice_of_computer))

        if __name__ == "__main__":
            main()
    elif X == 3:
        print("Thanks for playing! Goodbye!")

    else:
        print("Please enter 1, 2, or 3 for the Game Or To Exit!")
    leave = input("Do you want to continue? (press 'Y' to play agin or press 'N' To leave the Game!): ").strip().upper()
    if leave != "Y":
        print("Goodbye!")
        break 