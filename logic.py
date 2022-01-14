from questions import questions as __questions

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






