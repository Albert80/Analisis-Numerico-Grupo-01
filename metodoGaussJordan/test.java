/**
*	test.java
*
*	Created on 28 February 2014, 08:27 hrs.
*	A simple class wich implements a single object of
*	GaussJordan class
*	@see Gauss.java
*	@see GaussJordan.java
*
*	Universidad Nacional Autónoma de México
*	Análisis Numérico
*	Facultad de Ingeniería
*	Semestre: 2014-2
*	Profesor: Alejandro Figueroa Paez
*/

/**
*	@author -> Trejo Juárez César Alberto				contact:   cesaralberto@yandex.com / cesaratj27@gmail.com
*
*/

public class test{
	public static void main(String args[]){
		///*
		//+----------------GaussJordan----------------+//
		double []solGJ;
		double []solucionesGJ = {2.4, 6.4, 7.6};
		double [][]sistemaEcGJ = { {1, 2, 3},
								 {-2, -4, 8},
								 {3, 1, 2} };
		GaussJordan matrix_2 = new GaussJordan(3);
		System.out.println("\n\n\t\t-+-+-+-+-GAUSS-JORDAN METHOD-+-+-+-+-");
		matrix_2.setB(solucionesGJ);
		matrix_2.setA(sistemaEcGJ);
		solGJ = matrix_2.getX();
		System.out.println("\n-->Gauss-Jordan Solutions, X:");
		for (int i = 0; i < solGJ.length; i++) {
			System.out.print("Variable " + (i+1) + " >>>\t" + Math.rint(solGJ[i]*10000)/10000);
			System.out.println();
		}
		//*/

}