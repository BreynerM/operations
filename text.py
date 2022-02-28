def concat(t1,t2):
    return t1+" "+t2

def multiconcat(t1):
    return (t1 + " ") * 4

def textSR(opcion):
    t1 = str
    if opcion == 1:
        t1= "SUMA"
    elif opcion == 2:
        t1 = "RESTA"
    elif opcion == 3:
        t1 = "MULTIPLICACION"
    elif opcion == 4:
        t1 = "DIVISION"
    elif opcion == 5:
        t1 = "AREA DE UN TRIANGULO"
    elif opcion == 6:
        t1 = "MEDIA DE 4 NUMEROS"
    elif opcion == 7:
        t1 = "RADIO DE UN CIRCULO"
    else :
        print("ERROR")
    return t1

def textint():
    nums = "ingrese dos valores para la operacion"
    print(nums)
    return 0


print(textSR(3))