from inspect import _void
import aritmetica as a
import text as t


def operaciones():
    print("""
    -----------------------------------------------------
    -------------------    MENU    ----------------------
    - 1 SUMA 
    - 2 RESTA
    - 3 MULTIPLICACION 
    - 4 DIVISION 
    - 5 MEDIA DE CUATRO NUMEROS 
    - 6 RADIO DE UN CIRCULO 
    - 7 AREA DE UN CIRCULO 
    -----------------------------------------------------""")

    opc=int(input("Ingresa la opcion")) 


    if opc == 1:
        print(t.textSR(1))  
        print(t.textin(nums))
        a=int(input) 
        b=int(input)
        print(a.sumDosNum(a,b))
    elif opc == 2:
        print(t.textSR(2)) 
        print(t.textin(nums))
        a=int(input) 
        b=int(input)
        print(a.restDosNum(a,b))
    elif opc == 3: 
        print(t.textSR(3))
        print(t.textin(nums))
        a=int(input) 
        b=int(input)
        print(a.MultiplicarDosNum(a,b))
    elif opc == 4: 
        print(t.textSR(4))
        print(t.textin(nums))
        a=int(input) 
        b=int(input)
        print(a.DividirDosNum(a,b))
    elif opc == 5: 
        print(t.textSR(5))
        print(t.textin(nums))
        a=int(input) 
        b=int(input)
        print(a.MediaCuatroNum(a,b))
    elif opc == 6: 
        print(t.textSR(5))
        print(t.textin(nums))
        a=int(input) 
        b=int(input)
        print(a.AreaTriangulo(a,b))
    elif opc == 7: 
        print(t.textSR(6))
        print(t.textin(nums))
        a=int(input) 
        b=int(input)
        print(a.AreaCirculo(a,b))
    else:
        print("Opcion no valida")

    print(t.multiconcat("Resultados Exitosos"))

    print(t.concat("REALIZANDO","OPERACION"))


def run():
    operaciones()


if __name__ == "__main__":
    run()

