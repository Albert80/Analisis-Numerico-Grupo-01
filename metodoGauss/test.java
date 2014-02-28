/**
*	test.java
*
*	Created on 28 February 2014, 08:18 hrs.
*	A simple class wich implements an object of
*	Gauss Method
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
		//+---------------Gauss-------------------+//
		double []solG;
		double []soluciones = {2.4, 6.4, 7.6};
		double [][]sistemaEc = { {1, 2, 3},
								 {-2, -4, 8},
								 {3, 1, 2} };
		Gauss matrix = new Gauss(soluciones.length);
		System.out.println("\t\t-+-+-+-+-GAUSS METHOD-+-+-+-+-");
		matrix.setB(soluciones);
		matrix.setA(sistemaEc);
		solG = matrix.getX();
		System.out.println("\n-->Gauss Solutions, X: ");
		for (int i = 0; i < solG.length; i++) {
			System.out.print("Variable " + (i+1) + " >>>\t" + Math.rint(solG[i]*10000)/10000); //redondear cifra a 3 decimales
			//System.out.print("Variable " + (i+1) + " >>>\t" + solG[i]); //--> sin redondear
			System.out.println();
		}
		//*/
}