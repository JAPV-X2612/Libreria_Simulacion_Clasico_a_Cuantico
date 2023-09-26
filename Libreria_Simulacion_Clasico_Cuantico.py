# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/09/21

# Programa de Simulación de lo Clásico a lo Cuántico

from numpy import *
from copy import *
from math import *


def Mult_Clics(m,c):
    """Calcula y devuelve la matriz de relaciones correspondiente a dar c clics
    (2D array, int) -> tipo(s) de dato(s) de salida"""
    m = array(m)
    mc = copy(m)
    for k in range(c-1):
        mc = dot(mc,m)
    return mc


def Sim_Exp_Can_Det(m,xi,c):
    """Calcula y devuelve el estado final de una simulación del experimento determinístico de canicas dada la matriz de relaciones, el estado inicial y el número de clics
    (2D array, 1D array, int) -> 1D array"""
    m,xi = array(m),array(xi)
    xf = copy(xi)
    for x in xi:
        if x != int(x):
            return "El número de canicas en cada vértice debe ser un entero positivo"
    rel = 0
    for k in m:
        rel += sum(k)
    if rel != len(m):
        return "La matriz de relaciones no cumple las condiciones"
    elif c != int(c):
        return "El número de clics debe ser un entero positivo"
    else:
        for k in range(c):
            xf = dot(m,xf)
        return xf


def Sim_Exp_Part_Prob(n,m):
    """Calcula y devuelve el estado final y la matriz de probabilidades después de 2 clics, simulando el experimento probabilístico de una partícula disparada por n rendijas
    (int, 2D array) -> 2D array, 1D array"""
    m = array(m)
    m2 = Mult_Clics(m,2)
    xi = zeros((3*n+2,1))
    xi[0,0] = 1
    if n != int(n):
        return "El número de rendijas debe ser un entero positivo"
    else:
        xf = dot(m2,xi)
        return m2,xf


def Sim_Exp_Part_Cuan(n,m):
    """Calcula y devuelve el estado final y la matriz de probabilidades después de 2 clics, simulando el experimento cuántico de una partícula disparada por n rendijas
    (int, 2D array) -> 2D array, 1D array"""
    m = array(m)
    m2 = Mult_Clics(m,2)
    xi = zeros((3*n+2,1))
    xi[0,0] = 1
    if n != int(n):
        return "El número de rendijas debe ser un entero positivo"
    else:
        xf = dot(m2,xi)
        return m2,xf