import math

class ConversorAngulos:
    def __init__(self, angulo, tipo):
        self.angulo = angulo
        self.tipo = tipo

    def a_radianes(self):
        if self.tipo == 'grados':
            return math.radians(self.angulo)
        else:
            return self.angulo

    def a_grados(self):
        if self.tipo == 'radianes':
            return math.degrees(self.angulo)
        else:
            return self.angulo

if __name__ == '__main__':
    angulo = float(input("Introduce el ángulo: "))
    tipo = input("Introduce el tipo (grados/radianes): ").strip().lower()

    conversor = ConversorAngulos(angulo, tipo)

    if tipo == 'grados':
        print(f"{angulo} grados son {conversor.a_radianes()} radianes.")
    elif tipo == 'radianes':
        print(f"{angulo} radianes son {conversor.a_grados()} grados.")
    else:
        print("Tipo no válido. Introduce 'grados' o 'radianes'.")