from manhelado import listahelado
from mansabor import Mansabor

def test(): 
    a = listahelado()
    b = Mansabor()
    b.instanciarsabor()
    b.sabores()
    print('----MENU----')
    x = int(input('ingrese el numero de la accion(terminae con -1): '))
    while x==1 or x==2 or x==3 or x==4:
        match x:
            case 1:
                a.venta(b)
            case 2:
                a.saborV()
            case 3:
                a.phelado()
            case 4:
                a.total()
        x = int(input('ingrese el numero de la accion(terminae con -1): '))


if __name__ == '__main__':
    test()