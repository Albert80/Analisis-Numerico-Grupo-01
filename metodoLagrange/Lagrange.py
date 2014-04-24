#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Lagrange.py 
   Created on 26 March 2014, 08:03
   A simple class wich implements an object of
   Lagrange's Interpolation Method

   Universidad Nacional Autónoma de México
   Facultad de Ingeniería
   Análisis Numérico
   Semestre: 2014-2
   Profesor: Alejandro Figueroa Paez

   Author: Trejo Juárez César Alberto'''

import math

class Lagrange(object):
	"""A simple class wich implements Lagrange's Method"""
	def __init__(self, X):
		self.X = X # X which we need to approximate, example x = 0.415
		self.xs = []
		self.ys = []
		self.order = None

	def getXapro(self):
		return self.X

	def setXs(self, xValues):
		self.xs = xValues

	def getXs(self):
		return self.xs

	def setYs(self, yValues):
		self.ys = yValues

	def getYs(self):
		return self.ys

	def setOrder(self, Order):
		self.order = Order

	def getOrder(self):
		return self.order

	def poly(self):
		fX = 0
		for i in range(self.getOrder() + 1):
			fXp = 1
			for j in range(self.getOrder() + 1):
				if i <> j:
					fXp = fXp * ( (self.getXapro() - self.xs[j]) / (self.xs[i] - self.xs[j]) )
			fX = fX + (fXp * self.ys[i])

		print '\n\t\tLa mejor aproximación para x = ' + str(self.getXapro()) + ' es: ' + str(fX) + '\n'


# Examples
if __name__ == '__main__':
	x = [0.1, 0.4, 0.7, 1]
	y = [2.31, 3.36, 4.59, 6]
	polinomio = Lagrange(0.2)
	polinomio.setOrder(2)
	polinomio.setXs(x)
	polinomio.setYs(y)
	polinomio.poly()