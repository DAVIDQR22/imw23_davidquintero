import sys

def menu():
    phone_book = {}
    while True:

        print('''
        1. Mostrar lista de contactos.
        2. Añadir contacto (nombre y teléfono).
        3. Borrar contacto (nombre).
        4. Salir.
        ''')

        menu = input("Escoja la acción que desea realizar: ")

        if menu == '1':
            show_contacts(phone_book)


        elif menu == '2':
            name = input("Nombre del contacto que desea añadir: ")
            if name not in phone_book:
                phone = input("Número de teléfono del contacto: ")
                add_contact(phone_book, name, phone)
            else:
                print("Ese nombre de contacto ya está registrado. ")


        elif menu == '3':
            name = input("Nombre del contacto que desea eliminar: ")
            if name in phone_book:
                remove_contact(phone_book, name)
            else:
                print("El contacto que desea eliminar no se encuentra en su lista de contactos. ")

        elif menu == '4':
            break

        elif menu > '4':
            print("Por favor, escoja una opción válida: ")

def show_contacts(phone_book):
    if phone_book == {}:
        print("La agenda está vacía.")
    else:
        for name, phone in phone_book.items():
            print(name, ":", phone)

def add_contact(phone_book, name, phone):
    phone_book[name] = phone

def remove_contact(phone_book, name):
    del(phone_book[name])

if __name__ == '__main__':
    menu()
