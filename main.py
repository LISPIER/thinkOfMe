import events.eventParser
import game.readData
import game.saveData
import game.characters
import tools.getRandomEvent


def main():
    # 读档

    dataList = open("saveData/using/dataList.list", "r", -1, "utf-8")
    while True:
        line = dataList.readline()
        if line == "/<end>":
            break
        else:
            line = line.rstrip("\n")
            data = game.readData.readData(line)
            game.characters.characters[line] = data

    while True:
        chooseToDo = input("行动:日常(1) 交互(2);退出并存档(0)")
        # 根据反映，应该将交互和联系分开，并用两个指数确认可用性
        # 最后吐槽一句噼里啪啦一时爽，维护/重构火葬场
        if chooseToDo == "0":
            game.saveData.saveData("using",game.characters.characters)
            break
        elif chooseToDo == "1":
            randomEvent = tools.getRandomEvent.getRandomEvent()
            print(randomEvent)
            events.eventParser.eventParser(randomEvent,"randomEvents")
        elif chooseToDo == "2":
            print("交互界面还未完成，请等待")

            interactivableCharacter = []
            for characterID in game.characters.characters:
                character = game.characters.characters[characterID]
                if character.favorIndex >= character.interactiveIndex:
                    interactivableCharacter.append(character)
                    print(character.name)
            # 到此处已经筛选出了所有可以交互的对象了，下一步懒得写了

main()