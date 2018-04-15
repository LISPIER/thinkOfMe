import game.readData
import game.saveData
import game.characters
import characters.characterClass
import os


S0253 = characters.characterClass.character("S0253","S0253", 0, 100, 50)
zergQueen = characters.characterClass.character("zergQueen", "zergQueen", 0, 100, 50)
Rota = characters.characterClass.character("Rota", "Rota", 0, 100, 50)


characterList = {
    S0253.id: S0253,
    zergQueen.id: zergQueen,
    Rota.id: Rota}


game.saveData.saveData("original", characterList)

#  一个数据恢复工具，将当前的saveData/original件夹重置为一个初始存档
