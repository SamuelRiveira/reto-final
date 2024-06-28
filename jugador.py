import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vidaMax = random.choice(range(40, 65))
        self.vidaActual = self.vidaMax
        self.ataque = random.choice(range(9, 20))
        self.defensa = random.choice(range(5, 15))
        self.nivel = 1

    def __str__(self):
        return f"{self.nombre}:\n Vida Máxima: {self.vidaMax}, Vida Actual: {self.vidaActual}, Ataque: {self.ataque}, Defensa: {self.defensa}, Nivel: {self.nivel}\n"

    def atacar(self, objetivo):

        CalcularDefensaCritica = random.choice(range(0, 100))
        CalcularAtaqueCritico = random.choice(range(0, 100))
        defensaCritica = False
        ataqueCritico = False 

        daño = self.ataque - (objetivo.defensa / 2)

        if CalcularDefensaCritica <= 8:
            defensaCritica = True

        elif CalcularAtaqueCritico <= 5:
            ataqueCritico = True

        elif ataqueCritico == True:
            daño = self.ataque * 2 - (objetivo.defensa / 2)

        elif defensaCritica == True:
            daño = self.ataque - objetivo.defensa

        if daño < 0:
            daño = 0

        objetivo.vidaActual -= daño

        if objetivo.vidaActual < 0:
            objetivo.vidaActual = 0


    def subirDeNivel(self):
        
        self.vidaMax += random.choice(range(4, 10))
        self.ataque += random.choice(range(2, 5))
        self.defensa += random.choice(range(1, 3))
        self.nivel += 1

    def curarse(self):
        self.vidaActual += (self.vidaMax - self.vidaActual) * 0.5