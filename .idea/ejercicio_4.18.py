import turtle

class DibujoCubo:
    def __init__(self, lado):
        self.lado = lado
        self.tortuga = turtle.Turtle()

    def dibujar_cuadrado(self, x, y):
        self.tortuga.penup()
        self.tortuga.goto(x, y)
        self.tortuga.pendown()
        for _ in range(4):
            self.tortuga.forward(self.lado)
            self.tortuga.right(90)

    def dibujar_cubo(self):
        # Draw front square
        self.dibujar_cuadrado(0, 0)

        # Draw back square
        self.dibujar_cuadrado(self.lado / 2, self.lado / 2)

        # Draw connecting lines
        self.tortuga.penup()
        self.tortuga.goto(0, 0)
        self.tortuga.pendown()
        self.tortuga.goto(self.lado / 2, self.lado / 2)

        self.tortuga.penup()
        self.tortuga.goto(self.lado, 0)
        self.tortuga.pendown()
        self.tortuga.goto(self.lado + self.lado / 2, self.lado / 2)

        self.tortuga.penup()
        self.tortuga.goto(self.lado, -self.lado)
        self.tortuga.pendown()
        self.tortuga.goto(self.lado + self.lado / 2, -self.lado + self.lado / 2)

        self.tortuga.penup()
        self.tortuga.goto(0, -self.lado)
        self.tortuga.pendown()
        self.tortuga.goto(self.lado / 2, -self.lado + self.lado / 2)

        self.tortuga.hideturtle()

if __name__ == '__main__':
    lado = float(input("Introduce la longitud del lado del cubo: "))
    dibujo = DibujoCubo(lado)
    dibujo.dibujar_cubo()
    turtle.done()