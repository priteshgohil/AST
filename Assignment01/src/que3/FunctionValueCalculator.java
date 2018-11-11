package que3;

import java.util.ArrayList;

public class FunctionValueCalculator 
{
	public static void main(String[] args) 
	{
		ArrayList FunctionCalculator = new ArrayList<>();
		ArrayList shallowCopy = new ArrayList<>();
		ArrayList<ArrayList> mainList = new ArrayList<>();
		float i;
		for (i = 1; i < 101; ++i) 
		{
			FunctionCalculator.removeAll(FunctionCalculator);
			FunctionCalculator.add(2.0f * i);
			FunctionCalculator.add(Math.sqrt(i));
			FunctionCalculator.add(Math.pow(10.0f, i));
			FunctionCalculator.add(Math.pow(i, 3));
			FunctionCalculator.add(Math.pow(2, (1 / i)));
			FunctionCalculator.add(Math.exp(i));
			shallowCopy = new ArrayList<>(FunctionCalculator);
			mainList.add(shallowCopy);
		}
		System.out.println(mainList);
	}
}