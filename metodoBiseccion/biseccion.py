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
	pow(x, 3.5) - 80

def biseccion(tol):
	a = 3
	b = 4
	c = 0
	while(math.fabs(ecuation(a-b)) >= tol and ecuation(c) != 0):
		c = (a + b) / 2
		print 'Limite a: ' + str(a) + '	Límite b: ' + str(b) + 'valor medio: ' + str(c) + ''
		if ecuation(a) * ecuation(c) < 0:
			b = c

		else:
			a = c

	print 'Raíz encontrada: ' + str(c)

