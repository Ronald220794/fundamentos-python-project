import sys
from typing import Optional
from module_catalog import get_catalog
from module_cart import Cart



def console_clean():
    sdad


def show_menu():
    print("\nWelcome to the Online Store")
    print("1. Show Catalog")
    print("2. Add product to cart")
    print("3. Remove product from cart")
    print("4. Empty cart")
    print("5. Show cart")
    print("6. Complete purchase")
    print("7. Go out")
    print("\n")


def get_option() -> Optional[int]:
    try:
        option = int(input("> "))
        if 1 <= option <= 7:
            return option
        print("Error: Enter a number between 1 y 7")
    except ValueError:
        print("Error: You must enter a valid number")
    return None

def show_catalog():
    #print("\nProducts Catalog:")
    for product in get_catalog():
        print(f"Code: {product['code']} | Product: {product['name']} | Price: S/{product['price']:.2f}")
    print("...\n")      

def added_to_cart(cart: Cart):
    code = input("Enter product code: ").strip().upper()
    try:
        quantity = int(input("Quantity: "))
        exito, message = cart.add_cart(code, quantity)
        print(message)
    except ValueError:
        print("Error: La cantidad debe ser un número entero")
    print("\n")


def show_cart(cart: Cart):
    if cart.it_is_empty():
        print("You Cart is empty")
        print("\n")
        return
    else:
        print("\nYou Cart")
        for item in cart.get_cart():
            print(f"- {item ['name']} (x{item['quantity']}) -> S/{item['subtotal']:.2f}")
        print(f"Total: S/{cart.calculate_total():.2f}")
    print("\n")


def main():

    cart = Cart()
    show_menu()

    while True:
        #console_clean()
        
        option = get_option()
        
        if option is None:
            input("\nPress Enter to continue...")
            continue
        
        if option == 1:
            show_catalog()
        elif option == 2:
            added_to_cart(cart)
        elif option == 3:
            #eliminar_del_carrito(carrito)
            print("eliminar del carrito")
        elif option == 4:
            exito, message = cart.empty_cart()
            print(message)
        elif option == 5:
            show_cart(cart)
        elif option == 6:
            #finalizar_compra(carrito)
            print("Finalizar compra")
        elif option == 7:
            print("\nHasta pronto")
            break

if __name__ == "__main__":
    main()
