
import csv
import random
import time

odd = "-" * 90

def start():
  print("Hi there!")
  print(odd)
  print("I've generated a random 4 digit number for you.")
  print("Let's play a bulls and cows game.")
  print(odd)


def body():
    bu = ""
    co = ""
    bull = int()
    cow = int()
    wheel = 0

    number = str(random.randint(1000, 10000))
    #print("Number: ", number)  ### Ukáže vygenerované číslo !
    #print(odd)
    starttime = time.time()
    for o in range(50):
        wheel += 1
        print(wheel)
        choice = input("Enter a number(4-digit) : ")

        if len(choice) != 4 or choice[0] == "0":
            print("Your number is bad, enter another number !")
            print("The number must have 4 digits and the first number cannot be 0 !")
            print(odd)
            continue
        else:
            for i, a in enumerate(choice):
                if choice[i] == number[i]:
                    bull += 1
                else:
                    if a in number:
                        cow += 1

                if bull == 1:
                    bu = "bull"
                else:
                    bu = "bulls"
                if cow == 1:
                    co = "cow"
                else:
                    co = "cows"

            if choice == number:
                stoptime = time.time()
                cas = stoptime - starttime
                print(odd)
                print(f"Correct, you've guessed the right number in {wheel} guesses after {cas:0.3f} s.! You are winner !")
                if wheel in range(1,10):
                    print(f"Incredibly! In the {wheel} round ? Are you a wizard ?")
                elif wheel in range(11,20):
                    print(f"Amazing! {wheel} round is good !")
                elif wheel in range(21,30):
                    print(f"Good! {wheel} round is average !")
                elif wheel in range(31,40):
                    print(f"Uff! {wheel} round not so good!")
                else:
                    print(f"Ok! {wheel} round is not much, but you guessed it!")
                    print(odd)
                bull = 0
                cow = 0
                break
            else:
                print(f"{bu}: {bull}  {co}: {cow} ")
                print(odd)
            bull = 0
            cow = 0
    else:
        print(f"Uff! {wheel} round and nothing... You had no luck! Try it again! The number was {number}")

start()
body()

