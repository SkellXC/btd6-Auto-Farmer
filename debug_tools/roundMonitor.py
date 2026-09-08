from time import sleep
import keyboard
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tools as t
import templateMatcher

def checkRounds(interval: int):
    rounds = []
    print("Round monitor has started.")
    print("Check the console for the readings")
    print("Hold 'C' to end the program")
    while not keyboard.is_pressed("c"):
        sleep(1)
        try:
            sleep(interval)
            result = templateMatcher.getRoundNumber()
            rounds.append(t)
            print(result)
        except:
            print(rounds)
            print("Error. Program did not complete")

    print("Program has successfully ended")
    print(f"Unique Numbers:\n{set(rounds)}")

if __name__ == "__main__":
    checkRounds(2)