while(True):
    try:
        numero = int(input("Ingrese un número : "))
        if numero in [1,2,3]:
            resultado = "ES NÚMERO PRIMO"
        else:
            c = 0
            for i in range(1, numero + 1):
                if numero % i == 0:
                    c += 1
            if c == 2:
                print("ES NÚMERO PRIMO")
            else:
                print("NO ES NÚMERO PRIMO")
            break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")