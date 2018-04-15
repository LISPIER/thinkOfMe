import ui
import game.characters
import characters.characterClass


def turnSpace(string):
    return string.replace("/<space>", " ")


def lineParser(line, choice=None):  # choice在扫描选择分支的阶段会被赋值。。。其他时候默认None
    pattern = line[0]
    if pattern == "say":  # 这个地方传入的character其实是id，要注意！！！
        character = line[1]
        sentence = line[2]
        sentence = sentence.rstrip("\n")
        ui.view.view(pattern=pattern,character=character,sentence=sentence)
    elif pattern == "scene":
        scene = line[1]
        describe = line[2]
        describe = describe.rstrip("\n")
        ui.view.view(pattern=pattern,scene=scene,describe=describe)
    elif pattern == "action":
        action = line[1]
        action = action.rstrip("\n")
        ui.view.view(pattern=pattern,action=action)
    elif pattern == "favor":
        character = line[1]
        change = line[2]
        num = line[3]
        if change == "gain":
            game.characters.characters[character].gainFavorIndex(num)
        elif change == "lose":
            game.characters.characters[character].loseFavorIndex(num)
    elif pattern == "character":
        id = line[1]
        name = line[2]
        favorIndex = int(line[3])
        conquestIndex = int(line[4])
        interactiveIndex = int(line[5])
        newCharacter = characters.characterClass.character(id, name, favorIndex, conquestIndex, interactiveIndex)
        game.characters.characters[id] = newCharacter
    elif pattern == "/<choiceBegin>":
        return True
    elif pattern == "choiceDescribe":
        if choice == True:
            choiceNum = line[1]
            choiceDescribe = line[2]
            print("选择{choiceNum}:{choiceDescribe}".format(
                choiceNum=choiceNum,
                choiceDescribe=choiceDescribe
            )
            )
        return True
    elif pattern == "/<choiceDescribeEnd>":
        choiceNum = input("选择:")
        choice = choiceNum
        return choice
    elif pattern == "choice":
        choiceNum = line[1]
        choicePattern = line[2]
        choiceCharacter = line[3]
        choiceOperate = line[4]
        choiceOperateNum = int(line[5])
        if choiceNum == choice:
            if choicePattern == "favor":
                if choiceOperate == "gain":
                    print(game.characters.characters[choiceCharacter])
                    game.characters.characters[choiceCharacter].gainFavorIndex(choiceOperateNum)
                elif choiceOperate == "lose":
                    game.characters.characters[choiceCharacter].loseFavorIndex(choiceOperateNum)


def eventParser(eventName,eventDirectory):
    eventFile = open("events/"+eventDirectory+"/"+eventName+".event", "r", -1, "utf-8")
    listedFile = []
    gettingChoice = False
    while 1:
        line = eventFile.readline().rstrip("\n")
        if line == "/<end>":
            break
        else:
            listedLine = line.split(" ")
            newListedLine = []
            for element in listedLine:  # 去掉每项的空格
                element = turnSpace(element)
                newListedLine.append(element)
            listedLine = newListedLine

            gettingChoice = lineParser(listedLine,gettingChoice)
            # gettingChoice的值有很多可能性。。。最开始它是False，之后被赋值为True以保证正确读取所有的选择描述标签
            # 到最后会被赋值为一个数字字符串。。。用于标示用户做出了哪一项选择

            listedFile.append(listedLine)


