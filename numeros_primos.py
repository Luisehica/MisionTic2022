

def input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Entrada incorrecta; recuerda poner un NUMERO entero (1, 2, 5000,..)")
            print("-"*20)
            continue
        else:
            return user_input
            break


N = input_number("Ingrese N:\n")
divisores = 0
C = 2
while C < N:
    if N % C == 0:
        divisores += 1
        print("divisores: ", divisores)
    C += 1
    print("C: ", C)

if divisores == 0:
    print("El número es Primo")
else:
    print("El número NO es Primo")