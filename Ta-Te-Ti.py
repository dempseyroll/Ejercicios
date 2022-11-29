def inicio(choice):
    opcion = 1
    while (opcion >= 1):
        if (choice == "X"):
            elecX = print("Seras " + choice)
            opcion = 0
            return elecX
        else:
            if (choice == "O"):
                elecO = print("Seras " + choice)
                opcion = 0
                return elecO
            else:
                print("Has hecho una elección inválida. Vuelve a intentarlo.")
                opcion += 1
                choice = input("Ingresa 1 si quieres ser X, o 2 si quieres ser O: ")

def tablero():
    A1 = "|_|"
    A2 = "|_|"
    A3 = "|_|"
    B1 = "|_|"
    B2 = "|_|"
    B3 = "|_|"
    C1 = "|_|"
    C2 = "|_|"
    C3 = "|_|"
    return 


eleccion = input("Ingresa X si quieres ser X, o O si quieres ser O: ")
start = inicio(eleccion)

if (start == "Seras X" or "Seras O"):
    tablero()
    jugada = input("\nRealice su primer movimiento: ")
