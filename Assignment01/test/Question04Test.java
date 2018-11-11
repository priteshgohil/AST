import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import que4.ParameterCalculations;

class Question04Test {
	
	private double Perimeter,Area,diameter;
	private int selection;
	
	
	@Test
	void TestAreaandParimeterShouldReturnwithIntegerPrecision() 
	{
		
		diameter = 1;
		selection = 1;
        ParameterCalculations obj01 = new ParameterCalculations();	
		Perimeter = obj01.PerimeterOfCircle(selection,diameter);
		Area = obj01.AreaOfCircle(selection,diameter);
//		System.out.println();
		assertEquals(Perimeter, 3.0);
		assertEquals(Area, 0.75);
		
	}
	
	@Test
	void TestAreaandParimeterShouldReturnWithFloatPrecision()
	{
		diameter = 1;
		selection = 2;
        ParameterCalculations obj01 = new ParameterCalculations();	
		Perimeter = obj01.PerimeterOfCircle(selection,diameter);
		Area = obj01.AreaOfCircle(selection,diameter);
//		System.out.println();
		assertEquals(Perimeter, 3.1415927410125732);
		assertEquals(Area, 0.7853981852531433);
	}
	
	@Test
	void TestAreaandParimeterShouldReturnWithlongPrecision()
	{
		diameter = 1;
		selection = 3;
        ParameterCalculations obj01 = new ParameterCalculations();	
		Perimeter = obj01.PerimeterOfCircle(selection,diameter);
		Area = obj01.AreaOfCircle(selection,diameter);
//		System.out.println();
		assertEquals(Perimeter, 3.0);
		assertEquals(Area, 0.75);
	}
	
	@Test
	void TestAreaandParimeterShouldReturnWithDoublePrecision()
	{
		diameter = 1;
		selection = 4;
        ParameterCalculations obj01 = new ParameterCalculations();	
		Perimeter = obj01.PerimeterOfCircle(selection,diameter);
		Area = obj01.AreaOfCircle(selection,diameter);
//		System.out.println();
		assertEquals(Perimeter, 3.141592653589793);
		assertEquals(Area, 0.7853981633974483);
	}
}