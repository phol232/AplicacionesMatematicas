class Numeros:
    def raiz_cuadrada(self, a):
        x = 1.0
        for k in range(1, 20):
            x = (x + a / x) / 2
        return x

if __name__ == '__main__':
    while True:
        try:
            numero = float(input("Introduce un número: "))
            if numero < 0:
                print("El número debe ser no negativo. Inténtalo de nuevo.")
                continue
            operacion = Numeros()
            resultado = operacion.raiz_cuadrada(numero)
            print(f"La raíz cuadrada de {numero} es: {resultado}")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtalo de nuevo.")