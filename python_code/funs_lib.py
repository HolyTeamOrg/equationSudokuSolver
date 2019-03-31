# -*- coding: utf-8 -*-
"""
Este es el archivo de funciones que hemos creado

Created on Sat Mar  9 11:44:27 2019

@author: Tebinski
"""
from numpy import prod
from itertools import permutations


import cProfile, pstats, io


def profile(fnc):
    
    """A decorator that uses cProfile to profile a function
	
	::args: fnc
	::outputs: txt file
	"""
    
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
    """ Funcion que calcula n! 
	
	::warning: Negative integer o float will raise a ValueError
	
	::args: 	n (int)
	::outputs: 	integer
	"""
    if n == 0: 
        return 1
    elif n < 0 or isinstance(n, float): 
        raise ValueError(('n must be a positive integer' % (n)))
    else:
        return prod(range(1,n+1))


def riddle_equation(coef):
       
    """ Calculamos el resultado de esos coeficientes en la ecuacion
    
    ::args: lst or tuple of 9 components
    ::outs: float 
    """

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
    
""" Definimos el programa main para poder darselo a cProfiler mediante el 
decorador. """
@profile
def main():
    
    """ Programa principal """
    
    solutions = [] #iniciamos la lista de resultados
    for per in permutations(range(1,10)): 
        if riddle_equation(per)==66:
            solutions.append(per) 
            
    return solutions



