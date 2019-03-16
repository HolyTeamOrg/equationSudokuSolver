# -*- coding: utf-8 -*-
"""
Vamos a solucionar el enigma propuesto en 
https://github.com/HolyTeamOrg/equationSudokuSolver

Created on Sat Mar  9 11:44:27 2019

@author: TebaPC
"""
from numpy import prod
from itertools import permutations


import cProfile, pstats, io


def profile(fnc):
    
    """A decorator that uses cProfile to profile a function"""
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        
        f = open('cProfiler_results.txt', 'w')
        f.write(s.getvalue())
        f.close
        
        return retval

    return inner


def factorial(n):
    
    return prod(range(1,n+1))


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
    

def check_coef(coef):
    
    """ Para coef comprobamos que el resultado de la ecuacion es 66 """
    
    if  riddle_equation(coef) == 66:
        return True
    else: 
        return False


@profile
def main():
    
    """ Programa principal """
    
    solutions = [] #iniciamos la lista de resultados
    for per in permutations(range(10)): 
        coef = list(per) #TODO: per es un iterador, no lo tengo claro si puedo pasarselo a riddle_equation    
        if check_coef(coef):
            solutions.append(coef) 
    return solutions
## MAIN
## ===================================================================
solutions = main()


