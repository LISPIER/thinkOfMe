import characters.characterClass


def readData(fileName):  # 在main中循环调用以读取所有的数据文件
    dataFile=open("saveData/using/{fileName}.data".format(
        fileName=fileName
    ), "r", -1, "utf-8")
    character = characters.characterClass.character()
    while True:
        line = dataFile.readline().split(" ")

        if line == "/<end>":
            break

        elif line[0] == "id":
            character.id = line[1].rstrip("\n")

        elif line[0] == "name":
            character.name = line[1].rstrip("\n")

        elif line[0] == "name":
            character.name = line[1].rstrip("\n")

        elif line[0] == "favorIndex":
            character.favorIndex = int(line[1].rstrip("\n"))

        elif line[0] == "conquestIndex":
            character.conquestIndex = int(line[1].rstrip("\n"))

        elif line[0] == "interactiveIndex":
            character.interactiveIndex = int(line[1].rstrip("\n"))

        else:
            break
    dataFile.close()
    return character
