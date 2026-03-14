pin_correcto = 1234
acceso = False
intentos = 0

while intentos < 3:
    pin_ingresado = int(input("Ingresá tu PIN: "))
    
    if pin_ingresado == pin_correcto:
        print("Acceso permitido")
        acceso = True
        intentos = 3
    else:
        intentos = intentos + 1
        print("PIN incorrecto. Intentos: " + str(intentos))

if acceso == False:
    print("Tarjeta bloqueada")

