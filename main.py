from stick import load_animation
from time import sleep
from logic import checkAnswer, init
from sys import exit
from os import system
from questionsRUS import questions as __questions
from random import randrange
from questionsRUS import questions as __questionsRUS
carma = 0
bonus = randrange(-100, 10, 2)
carma += bonus
print("")

if __name__ == "__main__":
    try:
        print("Select your localiation: \n 1) RUS // Русский \n 2) ENG // English \n")
        a = int(input())
        if (a == 1):
            __questions = __questionsRUS
        # else:
        #     print("This language does not supports. Wait some years please:)")
        init(a)

    except ModuleNotFoundError:
        print("Fatal Error: Localization not found")
        exit(1)
    except ValueError:
        print("Fatal Error: You entered not number")
        exit(1)
    load_animation(f"{__questions['Disclaimer']}", whileTime=92) #184
    print(__questions["Introduction"])
    sleep(2)

    curQuest = __questions["q1"]
    print(curQuest)
    answ = int(input("Ваш ответ"))
    carma += checkAnswer(answ, curQuest)

    curQuest = __questions["q2"]
    print(curQuest)
    answ = int(input("Ваш ответ"))
    carma += checkAnswer(answ, curQuest)

    curQuest = __questions["q3"]
    print(curQuest)
    answ = int(input("Ваш ответ"))
    carma += checkAnswer(answ, curQuest)

    load_animation(__questions["Podschet"], whileTime=88)
    print(f"Ваша карма: {carma}")
    if (carma >= 160):
        print(__questions["Success"])
    else:
        print(__questions["Fail"])

    load_animation(__questions["Exit"], 170) # тут было 200
    #exit(0)
    system("pause")
