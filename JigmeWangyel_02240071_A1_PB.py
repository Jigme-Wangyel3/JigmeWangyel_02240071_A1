while True:
    Options = ["1.Guess the Number Game!","2.Rock paper Scissor game","3.Exit The Game!"]
    for i in Options:
        print(i)
    X = int(input("Choose The game you want according the number or you can Exit the Game!: "))
    #Guess number Game
    if X==1:
        import random

        def guess_the_number():
            number_to_guess = random.randint(1, 100)
            attempts = 0

            print("Hello! You chose guess the Number Game")
            print("The Number Lies Between 1 and 100!")
            
            while True:
                try:
                    user_guess = int(input("Enter your guess here!: "))
                    attempts += 1

                    # Checking if the guess is correct
                    if user_guess < number_to_guess:
                        print("Your value is too Low! Put Your Value Again! ")
                    elif user_guess > number_to_guess:
                        print("Your value is too high! Put Your Value Again! ")
                    else:
                        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                        break
                except ValueError:
                    print("Please enter a valid number between 1-100!")

        # Start the game
        guess_the_number()
    elif X==2:
        print("You Chose Rock, Paper and Scissors Game! ")
        import random

        def get_computer_choice():
            return random.choice(['rock', 'paper', 'scissors'])

        def get_winner(player, computer):
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
                player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
                if player_choice == 'quit':
                    print("Thanks for playing!")
                    break
                if player_choice not in ['rock', 'paper', 'scissors']:
                    print("Invalid choice, try again.")
                    continue
                
                computer_choice = get_computer_choice()
                print(f"Computer chose: {computer_choice}")
                print(get_winner(player_choice, computer_choice))

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