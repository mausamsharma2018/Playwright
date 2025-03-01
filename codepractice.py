
import random
class NumberGussing():





    def guessthenumber(self,):
        Guess = None
        secret_number = random.randint(1, 100)

        while Guess != secret_number:
            Guess = int(input("Enter your guess: "))
            if Guess < secret_number:
                print("Too low! Try again.")
            # Check if the guess is greater than the secret number
            elif Guess > secret_number:
                print("Too high! Try again.")
            # If the guess is correct, congratulate the player
            else:
                print("Correct! You guessed the number.")



obj= NumberGussing()
obj.guessthenumber()



