class Pila:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.esta_vacia():
            raise ValueError("La pila está vacía")
        return self.items.pop()

    def peek(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)


def mostrar_torres(torres, n):
    """Dibuja las tres torres. Cada disco se dibuja con '#'."""
    ancho = 2 * n + 1
    print()
    for nivel in range(n - 1, -1, -1):
        linea = ""
        for nombre in "ABC":
            items = torres[nombre].items
            if nivel < len(items):
                d = items[nivel]
                disco = "#" * (2 * d - 1)
            else:
                disco = "|"
            linea += disco.center(ancho) + "  "
        print(linea)
    print(("=" * ancho + "  ") * 3)
    print("".join(nombre.center(ancho) + "  " for nombre in "ABC"))


def mover_disco(torres, origen, destino, estado, mostrar):
    """Mueve el disco de arriba de 'origen' a 'destino' con push/pop."""
    disco = torres[origen].peek()
    tope_destino = torres[destino].peek()

    # Regla del juego: no se puede poner un disco grande sobre uno pequeño
    if tope_destino is not None and disco > tope_destino:
        raise ValueError("Movimiento inválido")

    torres[destino].push(torres[origen].pop())
    estado["movimientos"] += 1
    print(f"Movimiento {estado['movimientos']}: disco {disco} de {origen} a {destino}")
    if mostrar:
        mostrar_torres(torres, estado["n"])
        print()


def hanoi(k, origen, destino, auxiliar, torres, estado, mostrar):
    """Resuelve Hanoi con recursión para k discos."""
    if k == 0:
        return
    hanoi(k - 1, origen, auxiliar, destino, torres, estado, mostrar)
    mover_disco(torres, origen, destino, estado, mostrar)
    hanoi(k - 1, auxiliar, destino, origen, torres, estado, mostrar)


def resolver(n, mostrar):
    torres = {"A": Pila(), "B": Pila(), "C": Pila()}
    for disco in range(n, 0, -1):  # el disco más grande queda abajo
        torres["A"].push(disco)

    estado = {"movimientos": 0, "n": n}

    print("\nEstado inicial:")
    mostrar_torres(torres, n)
    print()

    hanoi(n, "A", "C", "B", torres, estado, mostrar)

    print("\nEstado final:")
    mostrar_torres(torres, n)
    print(f"\nDiscos: {n}")
    print(f"Movimientos realizados: {estado['movimientos']}")
    print(f"Mínimo teórico (2^n - 1): {2 ** n - 1}")


def pedir_discos():
    while True:
        try:
            n = int(input("¿Cuántos discos? (3 a 10): "))
            if 3 <= n <= 10:
                return n
            print("Escribe un número entre 3 y 10.")
        except ValueError:
            print("Escribe un número entero.")


def menu():
    print("\n==============================")
    print("      TORRES DE HANOI")
    print("==============================")
    print("1. Resolver Torres de Hanoi")
    print("2. Salir")
    return input("Elige una opción: ").strip()


def main():
    while True:
        opcion = menu()

        if opcion == "1":
            n = pedir_discos()
            r = input("¿Dibujar las torres en cada paso? (s/n): ").strip().lower()
            resolver(n, r == "s")

        elif opcion == "2":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()