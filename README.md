# simulador-planificacion-de-procesos
Consiste en un programa que permite elegir:
 	- algoritmo de planificación.
 	- la memoria (particiones variables o fijas).
 	- el tamaño de esta (y de las particiones fijas)
 	- el método de ordenamiento. 

 Luego se necesitan cargar los procesos con:
 	- su tamaño.
	- tiempos de arribo y ráfagas.
 	- recurso que utiliza (CPU,E/S). 
 Una vez determinado todo esto, el programa simula la planeación de estos procesos por orden según la configuración antes ingresada. Como resultados podemos ver en cada tiempo el estado de los procesos, los recursos y la memoria (y cada partición de esta), así como también vemos los tiempos promedio de retorno y espera y también podemos visualizar un gráfico de Gantt que resume lo anterior.

 Esta aplicación precisa de las siguientes librerias para ejecutarse:

	- PyQt5. (pip install pyQt5)
	- matplotlib (pip install matplotlib).
