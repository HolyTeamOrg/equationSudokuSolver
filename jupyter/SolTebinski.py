# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Si si prueba Probamos a explicar el codigo en un jupyter notebook

# ## Constructor de permutaciones
# Resolveremos cuantas permutaciones sin repeticion posibles hay con los numeros 1,2 y 3:

from itertools import permutations

permutations(range(1,4))

# `permutations` nos genera un iterador. Hay varias alternativas para extraer las soluciones.

# Usamos el generador de listas `list`

list(permutations(range(1,4)))

# O para mayor claridad contruimos un bucle `for`. 

for per in permutations(range(1,4)):
    print(per)

# Por algun motivo si probamos a crear un list_comprenhension nos da error **SI NO** añadimos los corchetes:

print(per) for per in permutations(range(1,4))

# Y si los añadimos nos da un output que no queremos

[print(per) for per in permutations(range(1,4))]

# Para calcular el número de permutaciones posibles, vamos a contruir una sencilla funcion factorial.

# ## Funcion factorial

import numpy as np
def factorial(n):
     return np.prod(range(1,n+1))


# Para las permutaciones sin repeticion de 1,2 y 3, habrá 3! permutaciones.

factorial(3)

# Como en la ecuacion tendremos los numeros del 1 al 9 sin repetirse, será 9! = 

factorial(9)


# ## Evaluador de la ecuacion

# Tendremos que comprobar 362880 permutaciones. Para ello vamos a definir una funcion que evalue la ecuacion dada una combinacion.

def riddle_equation(coef):
       
    """ Calculamos el resultado de esos coeficientes en la ecuacion """

    try:
        eq = (coef[0] + 
    			  13 
    			  * coef[1]
    			  / coef[2]
    			  + coef[3]
    			  + 12 
    			  * coef[4] 
    			  - coef[5] 
    			  -11 
    			  + coef[6]
    			  * coef[7]
    			  / coef[8]
    			  - 10) # = 66
        return eq
    except ZeroDivisionError:
        return float('NaN')


# Utilizamos la funcion con la primera permutacion. 

coef = range(1,10)
print(tuple(coef))
riddle_equation(coef)


# Ahora vamos a crear una sencilla funcion para comprobar si el resultado para unso coef dados es 66

def check_coef(coef):
    
    """ Para coef comprobamos que el resultado de la ecuacion es 66 """
    
    if  riddle_equation(coef) == 66:
        return True
    else: 
        return False


# ## Programa principal

# Ya tenemos todos los preparativos. Ahora solo tenemos que 
# - generar todas las permutaciones posibles
# - Calcular si el resultado es 66
# - Almacenar cada solucion. 

def main(): 
    solutions = []
    for per in permutations(range(1,10)):
        coef = tuple(per)
        if check_coef(coef):
            solutions.append(coef)
    return solutions


solution = main()

# Ahora os toca a vosotros @HolyTeam!

len(solution)

for sol in solution:
    print(sol)


