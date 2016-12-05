class Persona():
    def __init__(self, nombre='none', edad=0, sexo='H', peso=0, altura=0):
        self.__comprobarSexo(sexo)
        self.__nombre = nombre
        self.__edad = int(edad)
        self.__DNI = ''
        self.__sexo = sexo
        self.__peso = int(peso)
        self.__altura = int(altura)
        self.generarDNI()

    def calcularMC(self):
            if(self.__sexo=='H'):
                K=4
            else:
                K=2
            PI=self.__altura-100-((self.__altura-150)/K)
            if(PI==self.__peso):
                print('Peso Ideal')
                return 0
            else:
                if(PI<self.__peso):
                    print('Sobre Peso')
                    return -1
                else:
                    print('Infra Peso')
                    return 1

    def esMayorDeEdad(self):
        if (self.__edad > 17):
            return True
        else:
            return False

    def __comprobarSexo(self, sexo):
        if (sexo != 'M' and sexo != 'H'):
            sexo = 'H'

    def toString(self):
        print(self.__nombre)
        print(self.__edad)
        print(self.__DNI)
        print(self.__sexo)
        print(self.__peso)
        print(self.__altura)

    def generarDNI(self):
        import random
        diccionario = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X",
                       11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L",
                       20: "C", 21: "K", 22: "E"}
        x = []
        i = 0
        while (i < 8):
            x.append(random.randint(0, 9))
            i += 1

        x2 = str(x[0])+str(x[1])+str(x[2])+str(x[3])+str(x[4])+str(x[5])+str(x[6])+str(x[7])
        resto = int(x2) % 23
        letra = diccionario[resto]

        self.__DNI = x2 + letra
        print(self.__DNI)

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = int(edad)

    def setSexo(self, sexo):
        self.__sexo = sexo

    def setPeso(self, peso):
        self.__peso = int(peso)

    def setAltura(self, altura):
        self.__altura = int(altura)





