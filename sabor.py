class Sabor():
    def __init__(self, id, ingre, sabor):
        self.__id = id
        self.__ingre = ingre
        self.__sabor = sabor

    def getid(self):
        return self.__id

    def getingre(self): 
        return self.__ingre

    def getsabor(self):
        return self.__sabor