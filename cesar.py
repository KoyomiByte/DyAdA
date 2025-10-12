
mi = list("abcdefghijklmnñopqrstuvwxyz ,.")
mys = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ,.")  

opcion = input("Elija una opción:\n e) Encriptar texto\n d) Desencriptar texto\n b) Fuerza bruta (probar todos los desplazamientos)\n>>: ").strip().lower()

if opcion == 'e':
    texto = input("\nPega el texto a encriptar:\n>> ")
    try:
        des = int(input("\nDesplazamiento (entero, por defecto 1): ") or "1")
    except ValueError:
        des = 1
    cifrado = ""
    for caracter in texto:
        if caracter in mi:
            cifrado += mi[(mi.index(caracter) + des) % len(mi)]
        elif caracter in mys:
            cifrado += mys[(mys.index(caracter) + des) % len(mys)]
        else:
            cifrado += caracter
    print("\n Texto encriptado:\n")
    print(cifrado)

elif opcion == 'd':
    texto = input("\nPega el texto a desencriptar:\n>> ")
    try:
        des = int(input("\nDesplazamiento usado (entero, por defecto 1): ") or "1")
    except ValueError:
        des = 1
    descifrado = ""
    for caracter in texto:
        if caracter in mi:
            descifrado += mi[(mi.index(caracter) - des) % len(mi)]
        elif caracter in mys:
            descifrado += mys[(mys.index(caracter) - des) % len(mys)]
        else:
            descifrado += caracter
    print("\n Texto desencriptado:\n")
    print(descifrado)

elif opcion == 'b':
    texto = input("\nPega el texto cifrado (se intentarán todos los desplazamientos):\n>> ")
    max_des = len(mi)  # número total de posiciones 
    print(f"\n Probando todos los desplazamientos (1 a {max_des}):\n")
    for des in range(1, max_des + 1):
        candidato = ""
        for caracter in texto:
            if caracter in mi:
                candidato += mi[(mi.index(caracter) - des) % len(mi)]
            elif caracter in mys:
                candidato += mys[(mys.index(caracter) - des) % len(mys)]
            else:
                candidato += caracter
        print(f"Desplazamiento {des:2d}: {candidato}")
    print("\nRevisa las salidas y busca la que tenga sentido en español.")

else:
    print("Opción no válida.")


