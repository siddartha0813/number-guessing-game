import random
import winsound
import os
RED="\033[91m"
GREEN="\033[92m"
YELLOW="\033[93m"
BLUE="\033[94m"
RESET="\033[0m"


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
        self.high_score=self.load_highscore()
    def Take_guess(self):
        try:
            guess = int(input("Guess the number: "))
            return guess
        except ValueError:
            print("Please enter a number")
            return None

    def Check_guess(self, guess):
        if guess > self.secret_num:
            winsound.Beep(300,500)
            print(RED+"Guess was too high")
            self.attempts_left -= 1
        elif guess < self.secret_num:
            winsound.Beep(300,500)
            print(RED+"Guess was too low")
            self.attempts_left -= 1
        else:
            winsound.Beep(900,1000)
            print(GREEN+"Guess was correct")
            self.attempts_left -= 1
            print(GREEN+"guess was currect")
            return True
        return False
    def load_highscore(self):
        if not os.path.exists("highscore.txt"):
            with open("highscore.txt","w") as file:
                file.write("0")
            return 0
        with open("highscore.txt","r") as file:
            data=file.read().strip()
            if data.isdigit():
                return int(data)
            else:
                return 0

    def save_highscore(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.high_score))
    def start_game(self):
        score=0
        print(f"\nGuess the number between {self.settings.min_num} and {self.settings.max_num}")
        print(f"you have {self.attempts_left} attempts\n")
        while self.attempts_left > 0:
            guess = self.Take_guess()
            if guess is None:
                continue
            if self.Check_guess(guess):
                score=self.attempts_left*10
                print(GREEN+f"you scored:{score}  points !"+RESET)
                if score>self.high_score:
                    print(GREEN+f" NEW HIGH SCORE:{score}  points !"+RESET)
                    self.high_score=score
                    self.save_highscore()
                else:
                    print(YELLOW + f"High score remains:{self.high_score} points "+RESET)
                break
            print(YELLOW+f"attempts left: {self.attempts_left}"+RESET)

        if self.attempts_left == 0:
            winsound.Beep(200,500)
            print(RED+f"\n Game over! The number was {self.secret_num}"+RESET)

def choose_difficulty():
    print(BLUE+"\nchoose difficulty level:"+RESET)
    print("1.Easy (1-50,10 attempts)")
    print("2.Medium (1-100,5 attempts)")
    print("3.Hard (1-150,5 attempts)")
    while True:
        choose = input("Enter chooce(1-3): ")
        if choose == "1":
            return 1,50,10
        elif choose == "2":
            return 1,100,5
        elif choose == "3":
            return 1,150,5
        else:
            print(RED+"Please enter a valid choose"+RESET)

if __name__ == "__main__":
    while(True):
        min_num,max_num,max_attempts = choose_difficulty()
        settings = GameSettings(min_num,max_num,max_attempts)
        game = NumberGuessGame(settings)
        game.start_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thank you for playing...")
            break



