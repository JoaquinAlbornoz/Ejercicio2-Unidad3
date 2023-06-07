from sabor import Sabor
import csv

class Mansabor():
    def __init__(self):
        self.__lista = []

    def instanciarsabor(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 3\\ejercicio2\\sabores.csv', 'r') as f:
            reader = csv.reader(f, delimiter=';')
            for variable in reader:
                instancia = Sabor(int(variable[0]), variable[1], variable[2])
                self.__lista.append(instancia)

    def sabores(self): 
        x = ""
        for i in self.__lista:
            x += f'{i.getid()}. ingredientes: {i.getingre()} sabor: {i.getsabor()}\n'
        print(x)

    def getlista(self):
        return self.__lista
    
    def busq(self,s):
        id = None
        ingredientes = None
        k=0
        j=True
        while j and k < len(self.__lista()):
            if self.__lista[k].getsabor() == s:
                id = self.__lista()[k].getid()
                ingredientes = self.__lista()[k].getingre()
                j = False
            k += 1
        return id,ingredientes

    def getnombre(self, id):
        j = True
        i = 0
        while j and i < len(self.__lista):
            if self.__lista[i].getid() == id:
                j = False
                return self.__lista[i].getsabor()
            i += 1