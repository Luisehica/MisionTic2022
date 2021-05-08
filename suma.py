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
S = 0
for _ in range(N):
    X = input_number("Ingrese un número:\n")
    S = S + X
print(S)
