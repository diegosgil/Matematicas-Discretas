class Calculadora:
    def __init__(self ,num1 = 0 ,num2 = 0 ,Zn = 0):
        self.num1 = num1
        self.num2 = num2
        self.Zn = Zn

    # SUMA
    def imprimirSumaMod(self):
        if self.Zn > 0:
            if self.num1 < 0:
                resultadoDiv = self.num1 / self.Zn
                cociente = resultadoDiv + (abs(resultadoDiv.__round__()))
                multiplicacionDiv = cociente * self.Zn
                print(f"El resultado de ({multiplicacionDiv.__round__()} + {self.num2 % self.Zn}) mod {self.Zn} es: {(multiplicacionDiv.__round__() + (self.num2 % self.Zn)) % self.Zn}")
            elif self.num2 < 0:
                resultadoDiv = self.num2 / self.Zn
                cociente = resultadoDiv + (abs(resultadoDiv.__round__()))
                multiplicacionDiv = cociente * self.Zn
                print(f"El resultado de ({multiplicacionDiv.__round__()} + {self.num1 % self.Zn}) mod {self.Zn} es: {(multiplicacionDiv.__round__() + (self.num1 % self.Zn)) % self.Zn}")
            else:
                print(f"El resultado de ({self.num1 % self.Zn} + {self.num2 % self.Zn}) mod {self.Zn}, es: {(self.num1 + self.num2) % self.Zn}")
        else:
            print("Base Modular incorrecta")

    # MULTIPLICACION
    def imprimirMultiplicacionMod(self):
        if self.Zn > 0:
            if self.num1 < 0:
                resultadoDiv = self.num1 / self.Zn
                cociente = resultadoDiv + (abs(resultadoDiv.__round__()))
                multiplicacionDiv = cociente * self.Zn
                print(f"El resultado de ({multiplicacionDiv.__round__()} * {self.num2 % self.Zn}) mod {self.Zn} es: {(multiplicacionDiv.__round__() * (self.num2 % self.Zn)) % self.Zn}")
            elif self.num2 < 0:
                resultadoDiv = self.num2 / self.Zn
                cociente = resultadoDiv + (abs(resultadoDiv.__round__()))
                multiplicacionDiv = cociente * self.Zn
                print(f"El resultado de ({multiplicacionDiv.__round__()} * {self.num1 % self.Zn}) mod {self.Zn} es: {(multiplicacionDiv.__round__() * (self.num1 % self.Zn)) % self.Zn}")
            else:
                print(f"El resultado de ({self.num1 % self.Zn} * {self.num2 % self.Zn}) mod {self.Zn}, es: {(self.num1 * self.num2) % self.Zn}")
        else:
            print("Base modular incorrecta")

    # INVERSO MODULAR
    def AlgEuclides(self, num1 ,ZnInv):
        if num1 == 0:
            return (ZnInv ,0 ,1)
        else:
            sumando ,multiplicador ,residuo = self.AlgEuclides(ZnInv % num1 ,num1)
        return (sumando ,residuo - (ZnInv // num1) * multiplicador ,multiplicador)
    def inversoMod(self, num1 ,ZnInv):
        sumando ,residuo ,multiplicador = self.AlgEuclides(num1 ,ZnInv)
        if sumando != 1:
            raise Exception("Inverso modular no existe")
        else:
            return residuo % ZnInv

    # DIVISION
    def divisionMod(self, num1Div, num2Div, ZnInv):
        if ZnInv > 0:
            resultado_num1Div = num1Div % ZnInv
            resultado_num2Div = num2Div % ZnInv
            # print(f"{num1Div} mod {ZnInv} es: {resultado_num1Div}")
            # print(f"{num2Div} mod {ZnInv} es: {resultado_num2Div}")
            print(f"{resultado_num2Div}^-1 en Zn n:{ZnInv} es: {resultadoInversoMod}")
            print(f"{num1Div} Ø {num2Div} en n, n:{ZnInv}")
            resultadoDivMod = resultado_num1Div * resultadoInversoMod
            print(f"El resultado de {resultadoDivMod} mod Zn, n:{ZnInv} es: {resultadoDivMod % ZnInv}")
        else:
            print("Base modular incorrecta")

    # POTENCIA
    def imprimirPotenciaMod(self, numBase, numPotencia, ZnPot):
        self.numBase = numBase
        self.numPotencia = numPotencia
        self.ZnPot = ZnPot
        if self.ZnPot > 0:
            if self.numBase < self.ZnPot and self.numPotencia < self.ZnPot:
                print(f"{self.numBase}^{self.numPotencia} ϵ a Zn:{self.ZnPot}")
                resultadoBasePotencia = self.numBase ** self.numPotencia
                resultadoTotalBase = resultadoBasePotencia % self.ZnPot
                print(f"El resultado de {self.numBase}^{self.numPotencia} en Zn, n:{self.ZnPot} es igual a: ----> {resultadoTotalBase}")
            else:
                print(f"{self.numBase}^{self.numPotencia} ∉ a Zn:{self.ZnPot}")
                # Cuando ∉ aplicamos la division
                resultadoDivMod = self.numBase % self.ZnPot
                # print(f"El resultado de {numBase} mod Zn, n:{Zn} es: {numBase % Zn}")
                print(f"{self.numBase}^{self.numPotencia} ∉ a Zn, n:{self.ZnPot}  {resultadoDivMod}^{self.numPotencia} en Zn, n:{self.ZnPot}")
                resultadoMod = (resultadoDivMod ** self.numPotencia) % self.ZnPot
                print(f"El resultado de {self.numBase}^{self.numPotencia} en Zn, n:{self.ZnPot} es igual a: ---> {resultadoMod}")
        else:
            print("Base modular incorrecta")

    #RAIZ
    def RaizMod(self, numRaiz, ZnRaiz):
        if ZnRaiz > 0:
            cont = 0
            resultadosRaiz = ""
            while (cont < ZnRaiz):
                resultRaiz = (cont * cont) % ZnRaiz
                if resultRaiz == numRaiz:
                    resultadosRaiz += str(cont) + " "
                cont = cont + 1
            print(f"Los resultados de la raiz son: {resultadosRaiz}")
        else:
            print("Base modular incorrecta")

    #CUADRADO PERFECTO
    def cuadradoPerfecto(self, ZnCp):
        if ZnCp > 0:
            contador = 0
            resultadosCp = ""
            while (contador < ZnCp):
                resultRaiz = (contador * contador) % ZnCp
                resultadosCp += str(resultRaiz) + " "  # Convertir un 'entero' a un 'string'
                contador = contador + 1
            resultadosCp = list(set(resultadosCp))
            Cp = len(list(set(resultadosCp)))-1
            print(f"Los resultados de la raiz son: {resultadosCp}")
            print(f"El numero de valors que contiene el cuadrado perfectos son: {Cp}")
        else:
            print("Base modular incorrecta")



#MENU
def menu():
    print("\n=====MENU=====\n")
    print("1. Suma Modular")
    print("2. Multiplicacion Modular")
    print("3. Inverso Modular")
    print("4. Division Modular")
    print("5. Potencia Modular")
    print("6. Raiz Cuadrado Modular")
    print("7. Cuadrados Perfectos Modular")
    print("8. Salir")
    opcion = int(input("Seleccione una opcion: "))
    return opcion

opcion = 0
while opcion != 8:
    opcion = menu()

    if opcion == 1: #SUMA
        try:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            Zn = int(input("Ingresa el modulo 'Zn':"))
            iniciarSuma = Calculadora(num1, num2, Zn)
            iniciarSuma.imprimirSumaMod()
        except:
            print("Error, ingresa solo numeros enteros")

    elif opcion == 2:   #MULTUPLICACION
        try:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            Zn = int(input("Ingresa el modulo 'Zn':"))
            iniciarMultiplicacion = Calculadora(num1, num2, Zn)
            iniciarMultiplicacion.imprimirMultiplicacionMod()
        except:
            print("Error, ingresa solo numeros enteros")

    elif opcion == 3:   #INVERSO
        try:
            num1 = int(input("Ingresa el numero que desea invertir: "))
            ZnInv = int(input("Ingresa el modulo Zn, n:"))
            iniciarInverso = Calculadora(num1, ZnInv)
            resultado = iniciarInverso.inversoMod(num1, ZnInv)
            print(f"El inverso de {num1 % ZnInv}^-1 es: {resultado} en base {ZnInv}")
        except:
            print(
                "Error, ingresa solo numeros enteros")

    elif opcion == 4:   #DIVISION
        try:
            num1Div = int(input("Ingresa el primer numero: "))
            num2Div = int(input("Ingresa el segundo numero: "))
            ZnInv = int(input("Ingresa el Zn, n: "))
            iniciarDiv = Calculadora(num1Div, num2Div ,ZnInv)
            resultadoInversoMod = iniciarDiv.inversoMod(num2Div ,ZnInv)
            print(f"El inverso de {num2Div % ZnInv}^-1 en Zn, n:{ZnInv} es: {resultadoInversoMod}")
            print("entonces: ")
            resultadoDivMod = iniciarDiv.divisionMod(num1Div, resultadoInversoMod, ZnInv)
        except:
            print("Error, ingresa solo numeros enteros")

    elif opcion == 5:   #POTENCIA MODULAR
        try:
            numBase = int(input("Ingrese el numero de la base: "))
            numPotencia = int(input("Ingrese el numero de la potencia: "))
            ZnPot = int(input("Ingresa el modulo 'Zn':"))
            iniciarPotencia = Calculadora(numBase, numPotencia, ZnPot)
            iniciarPotencia.imprimirPotenciaMod(numBase, numPotencia, ZnPot)
        except:
              print("Error, ingresa solo numeros enteros")

    elif opcion == 6:   #RAIZ CUADRADA MODULAR
        try:
            numRaiz = int(input("Ingrese el numero de la raiz: "))
            ZnRaiz = int(input("Ingresa el modulo 'Zn': "))
            raizModular = Calculadora()
            raizModular.RaizMod(numRaiz ,ZnRaiz)
        except:
            print("Error, ingresa solo numeros enteros")

    elif opcion == 7:   #CUADRADO PERFECTO
        try:
            #numRaiz = int(input("Ingrese el numero de la raiz: "))
            ZnCp = int(input("Ingresa el modulo 'Zn': "))
            raizModular = Calculadora()
            raizModular.cuadradoPerfecto(ZnCp)
        except:
            print("Error, ingresa solo numeros enteros")

    else:   #SALIR
        print("Hasta pronto")


