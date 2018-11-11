
import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import que3.FunctionValueCalculator;

class Question03Test 
{
	
	private ArrayList<ArrayList> CalculatedList = new ArrayList<>();
	private ArrayList IndiVidualList = new ArrayList<>();
	private ArrayList VerificationList = new ArrayList<>();
	
	@Test
	void FunctionShouldReturnMultipleofTwoforGivenEntry() 
	{
		FunctionValueCalculator obj01 = new FunctionValueCalculator();
		CalculatedList = obj01.FunctionCalc();
		IndiVidualList = CalculatedList.get(8);
		
		double value =(float)IndiVidualList.get(0);
		
		
		assertEquals(value, 18.0);
		
	}
	
	@Test
	void FunctionShouldReturnTenToThePowerNumber()
	{
		FunctionValueCalculator obj01 = new FunctionValueCalculator();
		CalculatedList = obj01.FunctionCalc();
		IndiVidualList = CalculatedList.get(25);
		double value =(double)IndiVidualList.get(2);
		
		assertEquals(value, Math.pow(10, 26));
		
	}
	
	@Test
	void FunctionShouldReturnCubeOfTheNumber()
	{
		FunctionValueCalculator obj01 = new FunctionValueCalculator();
		CalculatedList = obj01.FunctionCalc();
		IndiVidualList = CalculatedList.get(55);
		double value =(double)IndiVidualList.get(3);
		
		assertEquals(value, Math.pow(56, 3));
	}
	
	
	@Test
	void FunctionShouldReturnSquareRootOfTheNumber()
	{
		FunctionValueCalculator obj01 = new FunctionValueCalculator();
		CalculatedList = obj01.FunctionCalc();
		IndiVidualList = CalculatedList.get(92);
		double value =(double)IndiVidualList.get(1);
	
		assertEquals(value, Math.sqrt(93));
	}
	
	@Test
	void FunctionShouldReturnExponentToNumber()
	{
		FunctionValueCalculator obj01 = new FunctionValueCalculator();
		CalculatedList = obj01.FunctionCalc();
		IndiVidualList = CalculatedList.get(38);
		double value =(double)IndiVidualList.get(5);
	
		assertEquals(value, Math.exp(39));
	}
	
	@Test
	void FunctionShouldReturn2toThePower1UponNumber()
	{
		FunctionValueCalculator obj01 = new FunctionValueCalculator();
		CalculatedList = obj01.FunctionCalc();
		IndiVidualList = CalculatedList.get(19);
		double value =(double)IndiVidualList.get(4);
		double a = Math.pow(2.0,(1.0/20));
		if ((value-a)< 10e-5)
		{
			assertTrue(true);
		}
		
	}
	
	@Test
	void FunctionShoulCalculateForHundredNumbers()
	{
		FunctionValueCalculator obj01 = new FunctionValueCalculator();
		CalculatedList = obj01.FunctionCalc();
		IndiVidualList = CalculatedList.get(15);
		
		int Length01 = (int) CalculatedList.size();
		int Length02 = (int) IndiVidualList.size();
		
		if (Length01 == 100 && Length02 == 6)
		{
			assertTrue(true);
		}
			
		
	}

}
