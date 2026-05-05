# Estructura de un programa - Algoritmos y programas

Al escribir un programa en una computadora, ésta interpretará al pie de la letra lo que le indiquemos. En ese sentido hay que considerar como principal obstáculo la disociación entre "lo que decimos" y lo que quisimos decir.

Podemos escribir un programa en un programa pensado para esa tarea (al que llamamos editor de código, en nuestro caso Visual Studio Code -o VSCode-). 

Las instrucciones de los programas tienen una disposición similar a la del idioma español: se interpretan de arriba a abajo y de izquierda a derecha. Aunque a veces podemos indicarle que queremos que tal instrucción o conjunto de instrucciones se ejecute dos o más veces, o que en ocasiones no se ejecute, o que se vuelva a la primera instrucción, entre otras cosas similares. 

Este recorrido del código (entendemos código por conjuntos de instrucciones) que hace una 
máquina al interpretarlo se denomina flujo de un programa. Un conjunto de instrucciones con el objetivo de obtener un determinado comportamiento se conoce como algoritmo (según el diccionario de la RAE: conjunto ordenado y finito de operaciones que permite hallar la solución de un problema).
***
## Ejemplo de algoritmo - en nuestra vida cotidiana:
¿Cuál sería el algoritmo para que una maquina prepare mate?

### Algoritmo preparar_mate

    Agarrar pava
    Verter agua de la canilla en la pava hasta el 70% de su capacidad
    Encerder ornalla
    Apoyar pava en ornalla encendida
    Apagar ornalla cuando el agua alcance los 85%
    
    Agarrar mate
    Agarrar yerba
    Verter yerba en el mate hasta el 70% de su capacidad
    Mojar levemente yerba en mate con agua natural
    Agarrar bombilla
    Insertar bombilla en mate con yerba
    
    Verter agua de pava en mate sin desbordar el mismo
    Disfrutar el mate!

### Fin del algoritmo
***

## Ejemplo de algoritmo - matemáticas:

Para una función cuadrática, obtener raíces (x1 y x2):

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_________  
### - b ± √ b² - 4ac  
────────────────  
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2a

1. Elevar b al cuadrado.
2. Multiplicar 4 por a y por c .
3. Restar el resultado de (2) al resultado de (1).
4. Calcular la raíz cuadrada del resultado de (3).
5. Sumar el resultado de (4) a -b .
6. Dividir el resultado de (5) por 2a .
7. Restar el resultado de (4) a -b .
8. Dividir el resultado de (7) por 2a .

(Omito algunos pasos, la idea es ilustrar las operaciones que conforman el algoritmo).
***
## Tipos de programas/aplicaciones:

- Aplicaciones móviles (en un celular)
- Aplicaciones web (en el navegador)
- Aplicaciones de escritorio (interfaz gráfica)
- Aplicaciones de consola (las veremos en éste curso)