
from atexit import register
from typing_extensions import Self


class RegisterUser(object):
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

class User(RegisterUser): 
    def __init__(self, nombre, id):
        super().__init__(nombre, id)
        print("Usuario {self.nombre} con identificacion {self.id}")
        
class MovieTickets(object):
    def Horas(self):
        self.horas = ["9:00 am", "12:00 pm", "3:00 pm", "6:00 pm"]
        print("Las horas disponibles para la funcion son a las: {self.horas[0]}, {self.horas[1]}, {self.horas[2]} y {self.horas[3]}")
    def AsientosTcikets(self, asientos, ticekts):
        self.asientos = [50]
        self.tickets = 50
        try:
            ticekts = int(input("Digite el numero de tickets que desea comprar: "))
            if self.tickets >= ticekts: 
                self.tickets -= ticekts
            for x in range (ticekts):
                asientos = int(input("Digite los asientos a elegir, recuerde que son 10 filas de 5 asientos: "))
                self.asientos[asientos] = 1
        except ValueError:
            print("Solo puede digitar numeros enteros")

              

