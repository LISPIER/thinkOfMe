

class character():

    def __init__(self, id=None, name=None, favorIndex=0, conquestIndex=0, interactiveIndex=0):
        self.id = id
        self.name = name
        self.favorIndex = favorIndex
        self.conquestIndex = conquestIndex
        self.interactiveIndex = interactiveIndex

    def gainFavorIndex(self,index):
        self.favorIndex += index

    def loseFavorIndex(self,index):
        if self.favorIndex > 0:
            if index > self.favorIndex:
                self.favorIndex = 0  # 当好感度大于0但是减数大于好感度时，将好感度清零
            else:
                self.favorIndex -= index
        elif self.favorIndex <= 0 :
            if self.favorIndex-index <= -20:
                self.favorIndex = -20  # 当好感度减少指-20以下时，将好感度调整为-20，即敌对/厌恶max
            else:
                self.favorIndex -= index  # 这是最朴素的减法

    def conquest(self):
        if self.favorIndex >= self.conquestIndex:
            print("{characterName}攻略完成".format(
                characterName=self.name
            )
            )