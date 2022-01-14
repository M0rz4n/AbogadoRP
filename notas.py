#No tengo claro como abrir los programas a traves de python, por lo que valoro hacer un notepad con tkinder

def main():
    print("Escriba y presione ENTER para guardar")
    with open("Notas.txt") as note:
        note.write(input())
    print("Nota guardada")
    print("Gracias y hasta más ver")


if __name__ == "__main__":
    main()