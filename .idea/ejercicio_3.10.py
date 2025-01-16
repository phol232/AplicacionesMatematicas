class CuentaBancaria:
    def __init__(self, saldo, tasa_interes_anual):
        self.saldo = saldo
        self.tasa_interes_anual = tasa_interes_anual

    def calcular_interes_mensual(self):
        tasa_interes_mensual = self.tasa_interes_anual / 12
        interes_mensual = self.saldo * (tasa_interes_mensual / 100)
        return interes_mensual

    def aplicar_interes_mensual(self):
        interes_mensual = self.calcular_interes_mensual()
        self.saldo += interes_mensual
        return self.saldo

if __name__ == '__main__':
    saldo_inicial = float(input("Introduce el saldo inicial: "))
    tasa_interes_anual = float(input("Introduce la tasa de interés anual (en %): "))
    cantidad_anos = int(input("Introduce la cantidad de años: "))

    cuenta = CuentaBancaria(saldo_inicial, tasa_interes_anual)
    print(f"Saldo inicial: {cuenta.saldo}")

    for mes in range(1, cantidad_anos * 12 + 1):
        cuenta.aplicar_interes_mensual()
        print(f"Saldo después del mes {mes}: {cuenta.saldo:.2f}")