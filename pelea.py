from jugador import Jugador
import random

class BattleRoyale(Jugador):

    def __init__(self, nombre=None):
        super().__init__(nombre)
        self.jugadores = []
        self.siguienteRonda = []

    def pelea(self, jugador1, jugador2):
        print(jugador1)
        print(jugador2)

        jugador1.atacar(jugador2)
        print(f"\n{jugador1.nombre} ataca a {jugador2.nombre}\n\n")
        jugador1.subirDeNivel()
        while True:
            if jugador2.vidaActual > 0:
                print(jugador1)
                print(jugador2)
                jugador2.atacar(jugador1)
                print(f"\n{jugador2.nombre} ataca a {jugador1.nombre}\n\n")
                jugador2.subirDeNivel()
                if jugador1.vidaActual > 0:
                    print(jugador1)
                    print(jugador2)
                    jugador1.atacar(jugador2)
                    print(f"\n{jugador1.nombre} ataca a {jugador2.nombre}\n\n")
                    jugador1.subirDeNivel()
                else:
                    print(f"--------------------\n{jugador2.nombre} gana\n--------------------\n\n")
                    print(jugador1)
                    print(jugador2)
                    jugador2.curarse()
                    self.eliminar_jugador(jugador1)
                    self.siguienteRonda.append(jugador2)
                    self.eliminar_jugador(jugador2)
                    break
            else:
                print(f"--------------------\n{jugador1.nombre} gana\n--------------------\n\n")
                print(jugador1)
                print(jugador2)
                jugador1.curarse()
                self.eliminar_jugador(jugador2)
                self.siguienteRonda.append(jugador1)
                self.eliminar_jugador(jugador1)
                break

    def eliminar_jugador(self, jugador):
        # Eliminar al jugador mediante el índice
        for i, j in enumerate(self.jugadores):
            if j is jugador:
                del self.jugadores[i]
                break

    def torneo(self):
        contadorRondas = 0
        candidatos = []
        num_jugadores = random.randint(3, 8)

        for i in range(num_jugadores):
            jugador = Jugador(f"Jugador{i+1}")
            self.jugadores.append(jugador)

        while True:

            if len(self.jugadores) == 0:
                for jugador in self.siguienteRonda:
                    self.jugadores.append(jugador)
            self.siguienteRonda = []

            if len(self.jugadores) == 1:
                print(f"El ganador del Battle Royale de Haría es {self.jugadores[0]}")
                break

            elif contadorRondas > 0:
                print(f"\n¡Ronda número {contadorRondas+1}!\n")

            print(f"Jugadores restantes: {len(self.jugadores)}\n")

            while len(self.jugadores) >= 2:
                candidatos = []
                for _ in range(2):
                    while True:
                        candidato = random.choice(self.jugadores)
                        if candidato not in candidatos:
                            candidatos.append(candidato)
                            break

                self.pelea(candidatos[0], candidatos[1])

            if len(self.jugadores) == 1:
                self.siguienteRonda.append(self.jugadores[0])
                self.eliminar_jugador(self.jugadores[0])

            contadorRondas += 1