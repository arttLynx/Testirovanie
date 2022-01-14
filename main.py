from questions import questions as __questions
from stick import load_animation
from time import sleep
from logic import checkAnswer
from sys import exit
from os import system
carma = 0
if __name__ == "__main__":
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

    load_animation("Подсчёт результатов ", whileTime=88)
    print(f"Ваша карма: {carma}")
    if (carma >= 160):
        print("Вы прошли тест! ПОЗДРАВЛЯЮ!!!")
    else:
        print("[ПРИКАЗ] Отвезти этого белого в Бразилию, к обезьянам!")

    load_animation("Выход из программы", 200)
    #exit(0)
    system("pause")
