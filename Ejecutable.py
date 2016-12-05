from Persona import Persona
class Ejecutable():
    def __init__(self):
        self.nombre = ''
        self.edad = 0
        self.sexo = ''
        self.peso = 0
        self.altura = 0
    def exe(self):
        print('Ingrese un nombre')
        self.nombre = input()
        print('Ingrese un edad')
        self.edad = input()
        print('Ingrese el sexo')
        self.sexo = input()
        print('Ingrese el peso')
        self.peso = input()
        print('Ingrese el altura')
        self.altura = input()
        self.obj1 = Persona(self.nombre, self.edad, self.sexo, self.peso, self.altura)
        self.obj2 = Persona(self.nombre, self.edad, self.sexo)
        self.obj3 = Persona()
        self.obj1.setNombre(self.nombre)
        self.obj1.setEdad(self.edad)
        self.obj1.setSexo(self.sexo)
        self.obj1.setPeso(self.peso)
        self.obj1.setAltura(self.altura)
        self.obj1.calcularMC()
        self.obj2.calcularMC()
        self.obj3.calcularMC()
        self.obj1.esMayorDeEdad()
        self.obj2.esMayorDeEdad()
        self.obj3.esMayorDeEdad()
        self.obj1.toString()
        self.obj2.toString()
        self.obj3.toString()
ejecutar = Ejecutable()
ejecutar.exe()