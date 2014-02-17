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
	return (pow(x, 4) - 8 * pow(x, 3) - 35 * pow(x, 2) + 450 * x - 1001)
	# return (pow(x,10) - 1)

def derivateEcuation(x):
	return (4 * pow(x,3) - 24 * pow(x,2) - 70 * x + 450 )
	#return (10 * pow(x, 9))

def newtonRaphson(tol):
	x_0 = 0.65
	x_n_1 = 0
	tolerancia = tol
	x_n = x_0
	it = 1
	root = 0
	newValue = 0
	beforeValue = 0
	errorAbs = 0
	errorRel = 0
	before = 0
	after = 0
	while (math.fabs(x_n_1 - x_n) < tolerancia) or (ecuation(x_n_1) != 0):
		x_n_1 = x_n - (ecuation(x_n) / derivateEcuation(x_n))
		print 'Iteración: ' + str(it) + '	valor inicial: ' + str(x_n) + '	f(x): ' + str(ecuation(x_n)) + "	f'(x): " + str(derivateEcuation(x_n)) + '	posible raíz: ' + str(x_n_1)
		if it > 2:
			before = x_n
			after = x_n_1
			errorAbs = math.fabs(after - before)
			errorRel = (math.fabs((after - before)) / after) * 100
			print '\t\tError absoluto: ' + str(errorAbs) + '	Error relativo: ' + str(errorRel)
			if x_n_1 == root:
				print 'Raíz encontrada:	' + str(root)
				break
			root = math.fabs(x_n_1)		
		x_n = math.fabs(x_n_1)
		it += 1


# Examples
if __name__ == '__main__':
	newtonRaphson(0.01)
