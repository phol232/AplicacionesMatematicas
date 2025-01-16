import turtle

class DibujoCuadrado:
    def __init__(self, lado):
        self.lado = lado
        self.tortuga = turtle.Turtle()

    def dibujar(self):
        for _ in range(4):
            self.tortuga.forward(self.lado)
            self.tortuga.right(90)
        self.tortuga.hideturtle()

if __name__ == '__main__':
    lado = float(input("Introduce la longitud del lado del cuadrado: "))
    dibujo = DibujoCuadrado(lado)
    dibujo.dibujar()
    turtle.done()