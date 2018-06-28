import os


def getFavorIndexEffection(file):
    while True:
        createOrNot = input("好感度波动:无(0) 创建(1)")
        if createOrNot == "0":
            break
        elif createOrNot == "1":
            character = input("好感度波动主体:")
            change = input("上升(1),下降(2)")
            changeNum = input("波动幅度(一个整数)")
            if change == "1":
                file.write("favor {character} gain {changeNum}\n".format(
                    character=character.replace(" ", "/<space>"),
                    changeNum=changeNum.replace(" ", "/<space>")
                )
                )
            elif change == "2":
                file.write("favor {character} lose {changeNum}\n".format(
                    character=character.replace(" ", "/<space>"),
                    changeNum=changeNum.replace(" ", "/<space>")
                )
                )


def createEvent():
    fileName = input("输入该事件文件的名称")
    file = open("events/newEvents/" + fileName + ".event", "w+", -1, 'utf-8')

    while True:
        pattern = input("创建:对话(1) 场景(2) 动作(3) 新人物(4) 分支(5);保存并返回(0)")
        text = ""
        if pattern == "0":
            os.system("clear")
            break
        elif pattern == "1":
            characterName = input("输入人物名称:")
            sentence = input("输入对话内容:")
            text = '{pattern} {characterName} {sentence}'.format(
                pattern="say",
                characterName=characterName.replace(" ", "/<space"),
                sentence=sentence.replace(" ", "/<space>")
            )
        elif pattern == "2":
            sceneName = input("输入场景名称:")
            describe = input("输入场景描述:")
            text = '{pattern} {sceneName} {describe}'.format(
                pattern="scene",
                sceneName=sceneName.replace(" ", "/<space>"),
                describe=describe.replace(" ", "/<space>")
            )
        elif pattern == "3":
            action = input("输入动作描写:")
            text = '{pattern} {action}'.format(  # 考虑的人类的书写习惯，字符串外层使用单引号，上同
                pattern="action",
                action=action.replace(" ", "/<space>")
            )
        elif pattern == "4":
            characterID = input("输入人物id:")
            characterName = input("输入人物名称:")
            characterFavorIndex = input("输入人物初始好感度:")
            characterConquestIndex = input("输入可攻略好感度")
            characterInteractiveIndex = input("输入可互动好感度")
            text = "character {id} {name} {favorIndex} {conquestIndex} {interactiveIndex}".format(
                id=characterID,
                name=characterName,
                favorIndex=characterFavorIndex,
                conquestIndex=characterConquestIndex,
                interactiveIndex=characterInteractiveIndex
            )
        elif pattern == "5":
            file.write("/<choiceBegin>\n")
            choiceNum = int(input("输入分支的个数:"))
            i=1
            while i <=choiceNum:
                describe = input("分支{i}的描述(请描述好感度的变化)\n".format(
                    i=i
                )
                )
                file.write("choiceDescribe {i} {describe}\n".format(
                    i=i,
                    describe=describe.replace(" ", "/<space>")
                )
                )
                i += 1
            file.write("/<choiceDescribeEnd>\n")
            i = 1
            while i <= choiceNum:
                print("为第{i}个分支创建好感度波动".format(
                    i=i
                )
                )
                while True:
                    character = input("好感度波动主体:")
                    change = input("上升(1),下降(2)")
                    changeNum = input("波动幅度(一个整数)")
                    if change == "1":
                        file.write("choice {i} favor {character} gain {changeNum}\n".format(
                            i=i,
                            character=character.replace(" ", "/<space>"),
                            changeNum=changeNum.replace(" ", "/<space>")
                        )
                        )
                    elif change == "2":
                        file.write("choice {i} favor {character} lose {changeNum}\n".format(
                            i=i,
                            character=character.replace(" ", "/<space>"),
                            changeNum=changeNum.replace(" ", "/<space>")
                        )
                        )
                    stop = input("继续创建(1) 中止(0)")
                    if stop == "0":
                        break
                i += 1
            text = "/<choiceEnd>"

        file.write(text+"\n")
        getFavorIndexEffection(file)
    file.write("/<end>")
    file.close()


def eventEditor():
    while True:
        editPattern = input("退出(0) 新建(1) 编辑(2)")
        if editPattern == "0":
            break
        elif editPattern == "1":
            createEvent()
        elif editPattern == "2":
            print("暂时不支持编辑，请等待更新")
            return
        else:
            break

eventEditor()