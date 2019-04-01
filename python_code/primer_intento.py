# -*- coding: utf-8 -*-
""" 
Vamos a solucionar el enigma propuesto en 
https://github.com/HolyTeamOrg/equationSudokuSolver

Created on Sat Mar  9 11:44:27 2019

@author: Tebinski
"""
from numpy import prod
from itertools import permutations


import cProfile, pstats, io

def myfunction(arg1, arg2, kwarg='whatever.'):
    """
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    Args:
        arg1:   A positional argument.
        arg2:   Another positional argument.

    Kwargs:
        kwarg:  A keyword argument.

    Returns:
        A string holding the result.

    Raises:
        ZeroDivisionError, AssertionError, VVValueError.

    Examples:
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last):
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last):
            ...
        ValueError
    """
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
	
	
def profile(fnc):
    
    """
	A decorator that uses cProfile to profile a function
	
	parameter fnc
	
	@warning Esta es nua prueba de warning, queda genial, me encanta
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
    """
	Funcion que calcula n!
	"""
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
## MAIN
## ===================================================================
sol = main()


