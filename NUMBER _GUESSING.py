import random


class GameSettings:
    def __init__(self,min_num,max_num,max_attempts):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts=max_attempts
class NumberGuessGame:
    def __init__(self,settings):
        self.settings = settings
        self.secret_num=random.randint(self.settings.min_num,self.settings.max_num)
        self.attempts_left=settings.max_attempts

    def Take_guess(self):
        try:
            guess = int(input("Guess the number: "))
            return guess
        except ValueError:
            print("Please enter a number")
            return None

    def Check_guess(self, guess):
        if guess > self.secret_num:
            print("Guess was too high")
            self.attempts_left -= 1
        elif guess < self.secret_num:
            print("Guess was too low")
            self.attempts_left -= 1
        else:
            print("guess was currect")
            return True
        return False

    def start_game(self):
        print(f"\nGuess the number between {self.settings.min_num} and {self.settings.max_num}")
        print(f"you have {self.attempts_left} attempts\n")
        while self.attempts_left > 0:
            guess = self.Take_guess()
            if guess is None:
                continue
            if self.Check_guess(guess):
                break
            print(f"attempts left: {self.attempts_left}")
        if self.attempts_left == 0:
            print(f"\n Game over! The number was {self.secret_num}")

if __name__ == "__main__":
    settings = GameSettings(1,100,10)
    game = NumberGuessGame(settings)
    game.start_game()
