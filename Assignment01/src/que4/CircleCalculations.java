package que4;

import java.util.Scanner;

public class CircleCalculations 
{
	public static void main(String[] args) 
	{
		Scanner io = new Scanner(System.in);
		Scanner precision = new Scanner(System.in);
		System.out.println("Input your selection for precision of pi 1.INT 2.Float 3.Long 4.Double: ");
		int Selection = io.nextInt();
		double pi;
		if (Selection == 1)
		{
			 pi = (int) Math.PI;
		}
		else if (Selection == 2)
		{
			 pi = (float) Math.PI;
		}
		else if (Selection == 3)
		{
			 pi = (long) Math.PI;
		}
		else if (Selection == 4)
		{
			 pi = (double) Math.PI;
		}
		else
		{
			 pi = (double) Math.PI;
		}
		
		System.out.println("Input the diameter of the circle: ");
		double diameter = io.nextDouble();
		double perimeter = pi * diameter;
		double area = (pi * diameter * diameter) / 4.0;

		System.out.println("Perimeter is = " + perimeter);
		System.out.println("Area is = " + area);

	}
}
