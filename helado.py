class helado():
    def __init__(self, gr, precio):
        self.__gr = gr 
        self.__precio = precio
        self.__sabores = []

    def agregarsabor(self, sabor):
        self.__sabores.append(sabor)

    def getsabores(self):
        return self.__sabores

    def getprecio(self):
        return self.__precio

    def getgr(self):
        return self.__gr

    def __str__(self):
        return f"Sabor: {self.nombre}"