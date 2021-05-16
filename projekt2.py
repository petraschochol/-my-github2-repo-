import random
import time

odd = "-" * 90
number = str()
choice = str()
wheel = 0
starttime = float()

# Predstaveni hry
def start():
  print("Hi there!")
  print(odd)
  print("I've generated a random 4 digit number for you.")
  print("Let's play a bulls and cows game.")
  print(odd)

# Generovani 4-mistneho cisla a kontrola duplicity a kontrola, že všechny znaky jsou čísla
def generate_num():
    global number
    while True:
        number = str(random.randint(1000, 10000))
        #print("Number: ", number)  ### Ukáže vygenerované číslo !
        #print(odd)
        if number.isdigit() == False:
            continue
        elif number[0] == number[1] or number[0] == number[2]:
            continue
        elif number[1] == number[2] or number[1] == number[3]:
            continue
        elif number[2] == number[3] or number[0] == number[3]:
            continue
        else:
            return number

# Zadání a kontrola vstupu uživatele.

def typing_input():
    global starttime
    starttime = time.time()
    global choice
    global wheel
    while True:
        wheel += 1
        print("Round:", wheel)
        choice = input("Enter a number(4-digit) : ")
        print(odd)
        if choice.isdigit() == False:
            print("Your number is bad, enter another number !")
            print("The number must have 4 digits only, no letters!")
            print(odd)
            continue
        elif len(choice) != 4 or choice[0] == "0":
            print("Your number is bad, enter another number !")
            print("The number must have 4 digits and the first number cannot be 0 !")
            print(odd)
            continue
        elif choice[0] == choice[1] or choice[0] == choice[2]:
            print("Your number is bad, enter another number !")
            print("The number entered must not contain duplicates !")
            print(odd)
            continue
        elif choice[1] == choice[2] or choice[1] == choice[3]:
            print("Your number is bad, enter another number !")
            print("The number entered must not contain duplicates !")
            print(odd)
            continue
        elif choice[2] == choice[3] or choice[0] == choice[3]:
            print("Your number is bad, enter another number !")
            print("The number entered must not contain duplicates !")
            print(odd)
            continue
        else:
            return choice

# Procházení jednotlivých znaků a počítání bulls a cows
def suma_bull(choice, number):
    bu = str()
    co = str()
    bull = 0
    cow = 0
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
    print(f"{bu}: {bull}  {co}: {cow} ")
    print(odd)
    return bull, cow

# Porovnavani a vyhodnocení výsledků.
def evaluation(choice, number, wheel):
    print("ve funkci: ", choice, number)
    stoptime = time.time()
    cas = stoptime - starttime
    print(odd)
    print(f"Correct, you've guessed the right number in {wheel} guesses after {cas:0.3f} s.!")
    if wheel in range(1,11):
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

# Ukonceni hry
def game_over():
    print("G A M E  O V E R !")
    time.sleep(5)
    quit()

def main():
    start()
    generate_num()
    for o in range(50):
        typing_input()
        if number == choice:
            evaluation(choice, number, wheel)
            game_over()
        else:
            suma_bull(choice, number)
    print(f"{wheel} round and nothing...I thought of a number {number}. You can try it again!")
    game_over()

if __name__ == '__main__':
    main()