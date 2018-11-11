package que4;

public class ParameterCalculations 
{
	public double PerimeterOfCircle(int selection,double diameter)
	{	
		double pi;
		if (selection == 1)
		{
			 pi = (int) Math.PI;
		}
		else if (selection == 2)
		{
			 pi = (float) Math.PI;
		}
		else if (selection == 3)
		{
			 pi = (long) Math.PI;
		}
		else if (selection == 4)
		{
			 pi = (double) Math.PI;
		}
		else
		{
			 pi = (double) Math.PI;
		}
		
		double Perimeter = pi*diameter;
		return Perimeter;
	}
	public double AreaOfCircle(int selection,double diameter)
	{
		double pi;
		if (selection == 1)
		{
			 pi = (int) Math.PI;
		}
		else if (selection == 2)
		{
			 pi = (float) Math.PI;
		}
		else if (selection == 3)
		{
			 pi = (long) Math.PI;
		}
		else if (selection == 4)
		{
			 pi = (double) Math.PI;
		}
		else
		{
			 pi = (double) Math.PI;
		}
		
		double Area = (pi*diameter)/4.0;
		
		return Area;
		
	}
	

}
