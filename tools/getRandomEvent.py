import random


def getRandomEvent():
    file = open("events/randomEvents/list.txt","r",-1,"utf-8")
    list = []
    while 1:
        line = file.readline()
        if line == "/<end>":
            break
        else:
            list.append(line.rstrip("\n"))  # 防换行符
    randomEvent = random.sample(list,1)[0]
    file.close()
    return randomEvent