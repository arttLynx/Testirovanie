from questionsRUS import questions as __questionsRUS
from sys import exit
def init(number=1):
    global __questions
    if number == 1:
        __questions = __questionsRUS
    else:
        print("This language does not supports. Wait some years please:)")
        exit(1)

# def locals(num):
#     try:
#         print("Select your localiation: \n 1) RUS // Русский \n 2) ENG // English \n")
#         #a = int(input())
#         if (num == 1):
#             from questionsRUS import questions as __questions
#     except ModuleNotFoundError:
#         print("Fatal Error: Localization not found")
#     except ValueError:
#         print("Fatal Error: You entered not number")

def checkAnswer(index, curQ):
    #q1
    if (index == 3 and curQ == __questions["q1"]):
        return 4
    elif (index != 3 and curQ == __questions["q1"]):
        return -4

    #q2
    if (index == 1 and curQ == __questions["q2"]):
        return 1000
    elif (index == 3 and curQ == __questions["q2"]):
        return -10000
    elif (index == 2 and curQ == __questions["q2"]):
        return -100

    #q3

    if (index == 1 and curQ == __questions["q3"]):
        return 100
    elif (index != 1 and curQ == __questions["q3"]):
        return -10






