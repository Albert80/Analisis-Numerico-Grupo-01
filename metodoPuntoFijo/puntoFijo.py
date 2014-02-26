#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''     UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO
        FACULTAD DE INGENIERÍA
        Análisis Numérico
        Semestre: 2014-2
        Profesor: Ingeniero Alejandro Figueroa
        Grupo: 01
        Método Punto Fijo
        Viernes 26 de Febrero 2014
        Created by: César Alberto Trejo Juárez
        No Cuenta:      309266811'''

import math

def gFunction(x):
	return (pow(math.cos(x/3),3))


def calculate():
	it = 1
	x = 0
	root = None
	errorRel = None
	before = 0
	print 'antes del while'
	while errorRel == None or errorRel > 0.01:
		now = gFunction(x)
		print 'Iteración: ' + str(it) + '\tValue x: ' + str(x) + '\tg(x): ' + str(now)
		if it > 1:
			errorRel = ( math.fabs(now - before) / now ) * 100
			print '\t\tError Relativo: ' + str(errorRel)
		if now == before:
                        root = now
                        break
		before = x = now
		it += 1
	root = now
	print 'Root: ' + str(root)
		
		
if __name__ == '__main__':
        calculate()	
