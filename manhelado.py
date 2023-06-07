from helado import helado
from sabor import Sabor

class listahelado():
    def __init__(self):
        self.__lista = []

    def venta(self, b): 
        a = 0
        k = 0
        print('ingrese los datos de la venta:')
        cant = int(input('gramos: '))
        precio = float(input('precio: '))
        i = int(input('cantidad de sabores: '))
        instancia = helado(cant, precio)
        self.__lista.append(instancia)
        for a in range(i):
            s = input(f'Sabor {a + 1}: ')
            id,ingredientes=b.busq(s)
            if id is not None and ingredientes is not None:
                inst = Sabor(id, ingredientes, s)
                instancia.agregarsabor(inst)
        self.__lista.append(instancia)

    def saborV(self):
        num = int(input('ingresar numero de id: '))
        cantvendida = 0
        contador = 0
        for helado in self.__lista:
            sabores = helado.getsabores()
            for sabor in sabores:
                if sabor.getid() == num:
                    cantvendida += (helado.getgr() / len(sabores))
                    contador += 1
        print(cantvendida)

    def phelado(self):
        peso = int(input('ingresar peso a buscar: '))
        s = []
        for instancia in self.__lista:
            if instancia.getgr() == peso:
                s += [s.getsabor() for s in instancia.getsabores()]
        conj = set(s)
        print(conj)

    def total(self):
        tot100 = 0
        tot150 = 0
        tot250 = 0
        tot500 = 0
        tot1000 = 0
        for instancia in self.__lista:
            if instancia.getgr() == 100:
                tot100 += instancia.getprecio()
            elif instancia.getgr() == 150:
                tot150 += instancia.getprecio()
            elif instancia.getgr() == 250:
                tot250 += instancia.getprecio()
            elif instancia.getgr() == 500:
                tot500 += instancia.getprecio()
            elif instancia.getgr() == 1000:
                tot1000 += instancia.getprecio()
        print(f'100: {tot100 / 2} 150: {tot150 / 2} 250: {tot250 / 2} 500: {tot500 / 2} 1000: {tot1000 / 2}')







