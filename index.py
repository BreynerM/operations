from inspect import _void
import aritmetica as ar
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

    opc = (input("Ingresa la opcion "))
    opc = int(opc)

    if opc == 1:
        print(t.textSR(1))  
        print(t.textint())
        a =int(input("Ingrese el primer valor "))
        b =int(input("Ingrese el segundo valor "))
        print(ar.sumDosNum(a,b))
    elif opc == 2:
        print(t.textSR(2)) 
        print(t.textint())
        a=int(input("Ingrese el primer valor ")) 
        b=int(input("Ingrese el segundo valor "))
        print(ar.restDosNum(a,b))
    elif opc == 3: 
        print(t.textSR(3))
        print(t.textint())
        a=int(input("Ingrese el primer valor ")) 
        b=int(input("Ingrese el segundo valor "))
        print(ar.multiplicarDosNum(a,b))
    elif opc == 4: 
        print(t.textSR(4))
        print(t.textint())
        a=int(input("Ingrese el primer valor ")) 
        b=int(input("Ingrese el segundo valor "))
        print(ar.dividirDosNum(a,b))
    elif opc == 5: 
        print(t.textSR(5))
        print(t.textint())
        a=int(input("Ingrese el primer valor ")) 
        b=int(input("Ingrese el segundo valor "))
        c=int(input("Ingrese el tercer valor "))
        d= int(input("Ingrese el cuarto valor "))
        print(ar.mediaCuatroNum(a,b,c,d))
    elif opc == 6: 
        print(t.textSR(5))
        print(t.textint())
        a=int(input("Ingrese la base  ")) 
        b=int(input("Ingrese la altura "))
        print(ar.areaDeUnTrinagulo(a,b))
    elif opc == 7: 
        print(t.textSR(6))
        print(t.textint())
        a=int(input("Ingrese el radio ")) 
        print(ar.radioCirculo(a))
    else:
        print("Opcion no valida ")
    print(t.concat("REALIZANDO","OPERACION"))
    print(t.multiconcat("Resultados Exitosos"))

operaciones()