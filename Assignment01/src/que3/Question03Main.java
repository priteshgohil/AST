package que3;

import java.util.ArrayList;
public class Question03Main 
{
	public static void main(String[] args) 
	{
		ArrayList<ArrayList> CalculatedList = new ArrayList<>();
		FunctionValueCalculator obj01 = new FunctionValueCalculator();	
		CalculatedList = obj01.FunctionCalc();
		System.out.println(CalculatedList);
		System.out.println(CalculatedList.get(0));
	}

}
