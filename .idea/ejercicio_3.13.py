
class Calificacion:
    def __init__(self, nota_numerica):
        self.nota_numerica = nota_numerica

    def obtener_calificacion_literal(self):
        if self.nota_numerica >= 90:
            return 'A'
        elif self.nota_numerica >= 80:
            return 'B'
        elif self.nota_numerica >= 70:
            return 'C'
        elif self.nota_numerica >= 60:
            return 'D'
        else:
            return 'F'

if __name__ == '__main__':
    nota_numerica = float(input("Introduce la nota numérica: "))
    calificacion = Calificacion(nota_numerica)
    calificacion_literal = calificacion.obtener_calificacion_literal()
    print(f"La calificación literal de {nota_numerica} es: {calificacion_literal}")