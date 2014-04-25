/**
*	DDNewton.java
*
*	A simple class wich uses Diferencias Divididas de Newton
*
*	Universidad Nacional Autónoma de México
*   Facultad de Ingeniería
*   Análisis Numérico
*   Semestre: 2014-2
*   Profesor: Alejandro Figueroa Paez
*
*   @author: Trejo Juárez César Alberto
*/

public class DDNewton{
	// Propiedades
	int grado;
	double []Y;
	double []X;
	double [][]diferencias;
	double punto;


	// Constructor
	public DDNewton(double point){
		this.punto = point;
	}

	//Métodos

	/** 
	*	Metodo para establecer X
	*	@return: void
	*	@param: real
	*/
	public void setX(double x[]){
		grado = x.length;
		X = new double[grado];
		System.arraycopy(x, 0, this.X, 0, x.length);
	}

	/** 
	*	Metodo para establecer Y
	*	@return: void
	*	@param: real
	*/
	public void setY(double y[]){
		grado = y.length;
		Y = new double[grado];
		System.arraycopy(y, 0, this.Y, 0, y.length);
	}

	/** 
	*	Metodo para establecer Y
	*	@return: void
	*	@param: real
	*/
	public double[] getPolinomio(){
		int i,j,k;
		double fx[] = new double[grado];
		grado = X.length;
		diferencias = new double[grado-1][grado-1];

		for (i = 0; i < diferencias.length; i++) {
			diferencias[i][0] = Math.rint(((Y[i+1] - Y[i]) / (X[i+1] - X[i]))*100)/100;
		}
		
		k = 2;
		for (i = diferencias.length-2; i >= 0; i--) {
			for (j = 1; j < diferencias.length; j++) {
				if(j < k){
					diferencias[i][j] = Math.rint(((diferencias[i+1][j-1] - diferencias[i][j-1]) / (X[i+2] - X[i]))*100)/100;
				}
			}
			k++;
		}

		fx[0] = Y[0];
		for (i = 0;i < diferencias.length ; i++) {
			fx[i+1] = diferencias[0][i];
		}

		return fx;
	}
}
