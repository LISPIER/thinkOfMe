def saveData(directory,characters):
    dataList = open("saveData/{directory}/dataList.list".format(
        directory = directory
    ), "w+", -1, "utf-8")
    for characterID in characters:
        character = characters[characterID]
        dataList.write(character.id+"\n")
        dataFile = open("saveData/{directory}/{id}.data".format(
            directory=directory,
            id=character.id
        ), "w+", -1, "utf-8")
        dataFile.write("id {id}\n".format(
            id=character.id
        )
        )
        dataFile.write("name {name}\n".format(
            name=character.name
        )
        )
        dataFile.write("favorIndex {favorIndex}\n".format(
            favorIndex=character.favorIndex
        )
        )
        dataFile.write("conquestIndex {conquestIndex}\n".format(
            conquestIndex=character.conquestIndex
        )
        )
        dataFile.write("interactiveIndex {interactiveIndex}\n".format(
            interactiveIndex=character.interactiveIndex
        )
        )
        dataFile.write("")
        dataFile.write("/<end>")
        dataFile.close()
    dataList.write("/<end>")
    dataList.close()