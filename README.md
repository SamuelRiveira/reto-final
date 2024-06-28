Pueden realizarlo en cualquier lenguaje de programación, mi recomendación es que lo hagan en los lenguajes de programación que ya conozcan como: Python, Javascript y Java.

Crear una clase Jugador con los siguientes datos:

    El constructor por defecto de Jugador debe inicializar los atributos de la siguiente manera:
        nombre, el valor que viene por parámetro
        vidaMáxima, aleatorio entre 40-65
        vidaActual, la misma que vidaMáxima
        ataque, aleatorio entre 9-20
        defensa, aleatorio entre 5-15
        nivel, 1

    Método atacar:
        Recibe un jugador por parámetro que será el que vamos a atacar, primero ataca Jugador this, luego ataca jugador por parámetro.

        Calcular ataqueCritico, un valor que simbolice un 5%, si es así, lo ponemos a true.

        Calcular defensaCritica, un valor que simbolice un 8%, si es asi, lo ponemos a true.

        Para las formulas this (yo) j1 (enemigo)
        
        Si el ataque es critico usamos la siguiente formula de ataque:
            damage = this.ataque * 2 - (j1.defensa / 2);

        Si la defensa es critica usamos la siguiente formula de ataque:
            damage = this.ataque - j1.defensa;

        Si ambos es crítico, es como si no fuera critico, por lo tanto usamos la formula normal:
            damage = this.ataque - (j1.defensa / 2);

        Si en algunos de los casos damage es menor que 0, haremos que damage valga 0, es decir no haga ningún tipo de daño.

        Una vez ataque this, comprobar si ha muerto j1, si no, j1 ataca ahora. (los this se intercambian por j1 y los j1 por this en las fórmulas)

        Siempre que no se muera al final de una pelea, debe llamar a subir nivel.

    Método subir nivel:
        Deberá incrementar el valor de todos los atributos.
            vidaMáxima, entre 4 y 10.
            ataque, entre 2 y 5.
            defensa, entre 1 y 3.
            nivel, +1

        Método toString mostrará la ficha del jugador.

        En el método Main, crear un método de prueba que cree unos jugadores de prueba y mostrar el toString, hacerlos pelear y volver a mostrar el toString para ver las subidas de niveles como prueba.

        Después otro método Battle Royale que deberá crear una especie de torneo y mostrar el ganador.

        Crear una Lista de jugadores (tamaño aleatorio entre 3 y 8), crear esa cantidad de jugadores (se le puede poner los nombres por teclado).

        Escoger dos Jugadores aleatorios (o en orden de lista) y hacerlos pelear hasta que muera uno, y el que muera se elimina de la lista. Mostrar "X jugador elimina a Y."

        El ganador se deberá curar un 50% de vida que le falte. vidaActual += (vidaMax - vidaActual) * 0.5.

        Se deberá priorizar Jugadores que no han peleado antes.

        Hacer una especie de while (lista.size() != 1) y cuando termina el bucle significa que sólo queda 1, el ganador.

        Mostrar el nombre del último jugador vivo que será el ganador. "X jugador ha ganado el Battle Royale de Haría."

        Se deberá crear métodos que puedan ayudar, por ejemplo, generar un número aleatorio entre 0 y el length/size - 1.

        Otro que haga lo mismo que el anterior pero con un parámetro extra, que no devuelva el mismo número que el tercer parámetro.