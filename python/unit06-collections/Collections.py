
'''
1) Realiza un programa que siga las siguientes instrucciones:

Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
Crea un conjunto llamado administradores con los administradores Juan y Marta.
Borra al administrador Juan del conjunto de administradores.
Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario
es administrador o no.
Notas: Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma
similar a una lista. También cuentan con un método llamado .discard(elemento) que sirve
para borrar un elemento.



usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}

administradores = {'Juan', 'Marta'}

administradores.discard('Juan')

administradores.add('Marcos')

for usuario in usuarios:
    aux = ''
    if usuario in administradores:
        aux = "es administrador"
    print(usuario, aux)

'''
from builtins import print

'''
2) Durante el desarrollo de un pequeño videojuego se te encarga configurar y 
balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, 
debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.
El guerrero tiene el doble de ataque y alcance que un caballero.
El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa 
y el doble de su alcance.
Muestra como quedan las propiedades de los tres personajes.


caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }


caballero['vida'] = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2

guerrero['ataque'] = caballero['ataque'] * 2
guerrero['alcance'] = caballero['alcance'] * 2

arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] * 2

print(caballero)
print(guerrero)
print(arquero)

'''



'''

3) Durante la planificación de un proyecto se han acordado una lista de tareas. 
Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor 
es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas 
pero sin los números de orden?

Pista: Para ordenar automáticamente una lista es posible utilizar el método .sort().
'''

'''
tareas = [
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])

'''


'''
Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
El script contendrá un bucle for que itere el número de veces del primer argumento.
Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (end='' evita el salto de línea).
Ejecuta el código y observa el resultado.
'''

import sys

if len(sys.argv) == 3:

    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    ran = range(1, 10)

    if filas in ran and columnas in ran:
        print(ran)

        for n in range(filas):
            print()
            for n2 in range(columnas):
                print(" * ", end='')

    else:
        print("error")

else:
    print("Error - Introduce los argumentos correctamente")
    print('Ejemplo: main.py 1 5')






