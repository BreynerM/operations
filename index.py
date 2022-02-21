from inspect import _void
import aritmetica as a
import text as t


def operaciones:
    print("""
    -----------------------------------------------------
    -------------------    MENU    ----------------------
    - 1 SUMA 
    - 2 RESTA
    - 3 MULTIPLICACION 
    - 4 DIVISION 
    - 5 MEDIA DE CUATRO NUMEROS 
    - 6 RADIO DE UN CIRCULO 
    - 7 
    -----------------------------------------------------""")

    opc=int(input("Ingresa la opcion")) 


    if opc == 1:
        print(t.textSR(1))
        print(a.sumDosNum(3,4))
    elif opc == 2:
        print(t.textSR(2))
        print(a.restDosNum(8,3))
    elif opc == 3: 
        print(t.textSR(3))
        print(a.multiplicarDosNum(5,5))
    elif opc == 4: 
        print(t.textSR(4))
        print(a.dividirDosNum(60,3))
    elif opc == 5: 
        print(t.textSR(5))
        print(a.mediaCuatroNum(3,4))
    elif opc == 6: 
        print(t.textSR(5))
        print(a.areaDeUnTriangulo(3,4))
    elif opc == 7: 
        print(t.textSR(6))
        print(a.radioCirculo(3,4))
    else:
        print("Opcion no valida")

    print(t.multiconcat("Resultados Exitosos"))

    print(t.concat("REALIZANDO","OPERACION"))
    




def run():
    operaciones()


if __main__ == "__main__":
    run()