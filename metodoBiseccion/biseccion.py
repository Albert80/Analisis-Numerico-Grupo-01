#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''	UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
	FACULTAD DE INGENIERÍA
	Análisis Numérico
	Semestre: 2014-2
	Profesor: Ingeniero Alejandro Figueroa 
	Grupo: 01
	Método Bisección
	Viernes 7 de Febrero 2014
	Created by: César Alberto Trejo Juárez'''

import math

def ecuation(x):
	return (pow(x, 3.5) - 80)

def biseccion(tol):
	a = 0
	b = 4
	c = 0
	before = 0
	after = 0
	errorAbs = 0
	errorRel = 0
	it = 1
	while(math.fabs(ecuation(b-a)) >= tol and ecuation(c) != 0):
		c = (a + b) / 2
		after = c
		print 'Limite a: ' + str(a) + '	Límite b: ' + str(b) + ' Valor medio: ' + str(c) + ' f(a): ' + str(ecuation(a)) + ' f(b): ' + str(ecuation(b)) + ' f(c): ' + str(ecuation(c))
		if it > 1:

			print '\t\tError absoluto: ' + str(errorAbs) + ' Error Relativo: ' + str(errorRel)
		if ecuation(a) * ecuation(c) < 0:
			b = c
			before = b
		else:
			a = c
			before = a

	print 'Raíz encontrada: ' + str(c)

# Examples
if __name__ == '__main__':
	biseccion(0.01)