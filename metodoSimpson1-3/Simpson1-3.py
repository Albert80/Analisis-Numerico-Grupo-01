#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Simpson1-3.py 
   Created on 28 April 2014, 08:13
   A simple class wich implements an object of
   Simpson's Integrate Method

   Universidad Nacional Autónoma de México
   Facultad de Ingeniería
   Análisis Numérico
   Semestre: 2014-2
   Profesor: Alejandro Figueroa Paez

   Author: Trejo Juárez César Alberto'''

import math

class Simpson13(object):
	def __init__(self, a, b):
		self.limitA = a
		self.limitB = b
		self.c = (self.limitA + self.limitB) / 2
		self.h = (self.limitB - self.limitA) / 2
		self.I = None

	def fx(self, x):
		return math.exp(math.cos(x))

	def getA(self):
		return self.limitA

	def getB(self):
		return self.limitB

	def getH(self):
		return self.h

	def getC(self):
		return self.c

	def integrate(self):
		self.I = (self.getH() / 3) * (self.fx(self.getA()) + 4 * self.fx(self.getC()) + self.fx(self.getB()))

	def getI(self):
		return round(self.I, 4)



# Examples
if __name__ == '__main__':
	ej = Simpson13(math.e, math.pi)
	ej.integrate()
	print 'La integral es: ' + str(ej.getI())


