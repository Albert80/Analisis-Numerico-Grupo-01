#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Gauss.py 
   Created on 5 March 2014, 07:50
   A simple class wich implements an object of
   Gauss Method

   Universidad Nacional Autónoma de México
   Facultad de Ingeniería
   Análisis Numérico
   Semestre: 2014-2
   Profesor: Alejandro Figueroa Paez

   author: Trejo Juárez César Alberto'''

import math

class Gauss(object):
	"""Gauss method"""
	def __init__(self, nxn):
		"""Constructor"""
		self.A = [] #Matriz A
		self.B = [] #Matriz B
		self.cte = 0
		self.orden = nxn
		self.X = [] #Matriz X, soluciones

	def setB(self, matrixB):
		"""Método para establecer la matriz B"""
		for i in matrixB:
			self.B.append(i)

	def setA(self, matrixA):
		"""Método para establecer la matriz A"""
		for j in matrixA:
			self.A.append(j)

	def getX(self):
		"""Método que soluciona el sistema de ecuaciones"""
		temp = 0
		tm = 0
		# Muestra la matriz ingresada:
		print '-->Your Matrix: '
		for m in range(self.orden):
			for n in range(self.orden):
				print str(self.A[m][n]), 
			print ' |' + str(self.B[m])
		#-----------------------------------
		# Ordenamiento de renglones:
		for k in range(self.orden):
			for i in range(self.orden - 1):
				if self.A[i][0] < self.A[i+1][0]:
					for j in range(self.orden):
						temp = self.A[i][j]
						self.A[i][j] = self.A[i+1][j]
						self.A[i+1][j] = temp
					tm = self.B[i]
					self.B[i] = self.B[i+1]
					self.B[i+1] = tm
		#------------------------------------
		# Muestra la matriz ordenada:
		print '\n-->Matrix sorted: '
		for m in range(self.orden):
			for n in range(self.orden):
				print str(self.A[m][n]), 
			print ' |' + str(self.B[m])
		#-----------------------------------
		# Operaciones elementales
		for i in range(self.orden):
			if self.A[i][i] == 0:
				print 'Existe un cero en la diagonal'
				break
			# Normalizamos el primer renglón
			self.cte = self.A[i][i]
			for j in range(self.orden):
				self.A[i][j] = self.A[i][j] / self.cte
			self.B[i] = self.B[i] / self.cte
			#--------------------------------------
			# Eliminación Gaussiana
			for j in range(i+1, self.orden):
				self.cte = self.A[j-1][i] / self.A[i][i]
				for k in range(i, self.orden):
					self.A[j][k] = self.A[j][k] - self.cte * self.A[i][k]
				self.B[j] = self.B[j] - self.cte * self.B[i]
			#--------------------------------------
			
		# Muestra la ultima matriz:
		print '\n-->Last Matrix: <<<'
		for m in range(self.orden):
			for n in range(self.orden):
				print str(self.A[m][n]), 
			print ' |' + str(self.B[m])
		#-----------------------------------

		# Almacenar las soluciones en X
		for l in range(self.orden - 1, -1, -1):
			self.X.append(self.B[l])
			for k in range(self.orden - 1, l, -1): #Aquí el problema
				for j in range(self.orden, k):
					self.X[j] = self.X[j] - (self.A[l][k] * self.X[k])

		print
		return self.X

# Examples
if __name__ == '__main__':
	m = Gauss(2)
	matA = [ [1.0,4.0],
			 [3.0,5.0] ]
	matB = [1.0, 1.0]
	m.setB(matB)
	m.setA(matA)
	soluciones =  m.getX()
	for s in range(len(soluciones)):
		print 'Variable ' + str(s+1) + ' >>> ' + str(soluciones[s])
