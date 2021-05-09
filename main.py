import numpy as np


def validate_input_yes_no(message):
    """ Validate that user entry must be an string with "si" or "no"

    :param message:
    :return boolean:
    """
    while True:
        user_input = (input(message))
        accept_more_option = user_input == "Si" or user_input == "si" or user_input == "s" or user_input == "S"
        decline_more_options = user_input == "No" or user_input == "no" or user_input == "n" or user_input == "N"
        if accept_more_option:
            return True
            break
        elif decline_more_options:
            return False
            break
        else:
            print("Ingrese si o no")
            continue


def validate_input_number(message):
    """ Validate that user entry must be an integer

    :param message:
    :return:
    """
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Entrada incorrecta; recuerda poner un NUMERO entero (1, 2, 5000,..)")
            continue
        else:
            return user_input
            break


def amount_to_be_pay(price, quantity):
    """ Calculate the amount to be pay for two list, price and quantity, this list must have the same length
suppose all product have 19% IVA

    :param price:
    :param quantity:
    :return: sum_amount
    """
    # set variables
    quantity = np.array(quantity)
    price = np.array(price)
    total = np.dot(quantity, price)
    sub_total = round(total / 1.19, 2)

    return sub_total, total


def header():

    print("*" * 50)
    print("Factura_soft-> Tu software para ayudar en tu negocio")
    print("Calcula el valor a pagar de tus clientes")
    print("*" * 50)

def main_program():
    """ Initialize the bill system

    :return:
    """

    # initialize list and while-
    price = []
    quantity = []
    i = 0
    # print header
    while True:
        i += 1
        # request price and quantity of some item
        print("Introduce el precio y la cantidad de productos")
        actual_price = validate_input_number("Introduce el precio del producto " + str(i) + " (sí con el IVA)\n")
        actual_quantity = validate_input_number(
            "Introduce la cantidad de items del producto " + str(i) + "\n")  # This copy could be confused

        # append price and quantity in list
        price.append(int(actual_price))
        quantity.append(int(actual_quantity))

        # ask if add more items

        ask_for_other_item = validate_input_yes_no("¿Hay más objetos por registar? Si/No\n")
        print("-" * 20)
        if ask_for_other_item:
            continue
        else:
            # verifica la canasta
            m = 0  # counter
            print("Verifica la canasta de tu cliente")
            if len(price) == 1:
                print("Producto 1: el precio es ", price[0], " y tiene ", quantity[0], "items")
                return price, quantity
            else:
                for i in range(len(price)):
                    m += 1
                    print("Producto ", m, ": el precio es ", price[i], " y tiene ", quantity[i], "items")
                return price, quantity


if __name__ == '__main__':
    # test homework cases
    test = False
    if test:
        # Case 1
        customer_price_1 = [1, 1, 1]
        customer_quantity_1 = [45000, 35000, 27000]
        sub_total_1, total_pay_1 = amount_to_be_pay(customer_price_1, customer_quantity_1)
        print("Customer 1 sub-total:", sub_total_1)
        print("Customer 1 total:", total_pay_1)

        # Case 2
        customer_price_2 = [3, 2]
        customer_quantity_2 = [120000, 3000]
        sub_total_2, total_pay_2 = amount_to_be_pay(customer_price_2, customer_quantity_2)
        print("Customer 2 sub-total:", sub_total_2)
        print("Customer 2 total:", total_pay_2)

    # start program
    header()
    while True:
        customer_price_3, customer_quantity_3 = main_program()
        sub_total_3, total_pay_3 = amount_to_be_pay(customer_price_3, customer_quantity_3)
        print("+" * 20)
        print("Sub-total:", sub_total_3)
        print("Total:", total_pay_3)
        print("=" * 20)

        continue_in_program = validate_input_yes_no("Quieres calcular el total a otro cliente? Si/No\n")
        if continue_in_program:
            continue
        else:
            print("Hasta luego!")
            break
