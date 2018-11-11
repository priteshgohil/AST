package que4;

import java.util.Scanner;

import que3.FunctionValueCalculator;

public class CircleCalculations 
{
	public static void main(String[] args) 
	{
		Scanner io = new Scanner(System.in);
		Scanner precision = new Scanner(System.in);
		System.out.println("Input your selection for precision of pi 1.INT 2.Float 3.Long 4.Double: ");
		int Selection = io.nextInt();
		System.out.println("Input the diameter of the circle: ");
		double diameter = io.nextDouble();
		
		ParameterCalculations obj01 = new ParameterCalculations();	
		double perimeter = obj01.PerimeterOfCircle(Selection,diameter);
		double area = obj01.AreaOfCircle(Selection,diameter);

		System.out.println("Perimeter is = " + perimeter);
		System.out.println("Area is = " + area);

	}
}
