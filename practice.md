### Ordenación de Caracteres en una Cadena Usando el Algoritmo de Selección

En este ejercicio, se implementará un programa que ordena los caracteres de una cadena en orden alfabético (según el diccionario) utilizando el algoritmo de ordenación por selección. El objetivo es comprender cómo manipular cadenas de caracteres en Python y aplicar un algoritmo de ordenación básico.

#### Descripción del Programa

El programa se compone de las siguientes funciones:

* `find_minimum(word, start_pos)`: Encuentra la posición del carácter mínimo en la subcadena que comienza desde `start_pos` hasta el final de la cadena `word`. Esta función ayuda a localizar el carácter más pequeño para realizar intercambios durante la ordenación.

* `selection_sort(word)`: Implementa el algoritmo de ordenación por selección. Recorre la cadena `word` y, en cada posición, encuentra el carácter mínimo desde la posición actual hasta el final y lo intercambia con el carácter en la posición actual si es necesario.

* `main()`: Función principal que toma una cadena de ejemplo, la ordena utilizando `selection_sort()` y muestra el resultado.

#### Ejemplo de Uso

```commandline
python3 ordenacion_cadena.py
```

Si la entrada es "hola", el programa imprimirá la cadena ordenada "ahlo".
