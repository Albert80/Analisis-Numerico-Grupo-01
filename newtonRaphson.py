#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''	UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
	FACULTAD DE INGENIERÍA
	Análisis Numérico
	Semestre: 2014-2
	Profesor: Ingeniero Alejandro Figueroa 
	Grupo: 01
	Método Newton Raphson
	Viernes 7 de Febrero 2014
	Created by: César Alberto Trejo Juárez'''

import math

def ecuation(x):
	return (math.sin(x) - pow(x, 2))

def derivateEcuation(x):
	return (math.cos(x) - 2 * x)

def newtonRaphson(tol):
	x_0 = 0.5
	x_n_1 = 0
	tolerancia = tol
	x_n = x_0
	it = 1
	while (math.fabs(x_n_1 - x_n) < tolerancia) or (ecuation(x_n_1) == 0):
		x_n_1 = x_n - (ecuation(x_n) / derivateEcuation(x_n))
		print 'Iteración: ' + str(it) + '	valor: ' + str(x_n_1)
		x_n = x_n_1
		it += 1

# Examples
if __name__ == '__main__':
	newtonRaphson(0.01)
