usuarios = {
"mmacia": {
    "nombre": "Martí",
    "apellido": "Macià",
    "password": "123123"
  },
"fmuguruza": {
    "nombre": "Fermín",
    "apellido": "Muguruza",
    "password": "654321"
 },
"cbiriukov": {
    "nombre": "Chechu",
    "apellido": "Biriukov",
    "password": "123456"
 }
}

#En este caso he dado a suponer que debe tiene um máximo de tres intentos para poner la contraseña antes de
#el programa le eche.
usuario = str(input("Escribe el usuario: "))
max_intentos = 3
for intento in range(1, max_intentos +1):
    passwd = str(input("Escribe la contraseña: "))
    intentos_restantes = max_intentos - intento
    if usuario in usuarios:
        if passwd == usuarios[usuario]["password"]:
            print("Hola,", usuarios[usuario]["nombre"], usuarios[usuario]["apellido"],)
            break
        else:
            if intentos_restantes >= 0:
                print("ERROR! Te quedan", intentos_restantes ,"intentos.")
                exit
                if intentos_restantes == 0:
                    print("Has agotados todos tus intentos")
    else:
        print("El usuario introducido no existe!")