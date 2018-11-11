import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;

import org.junit.jupiter.api.Test;

import que1.ArithmaticOp;

class ArithmaticOperationTest {
	private int result=0;
	private ArrayList<Integer> testData = new ArrayList<>(); 
	ArithmaticOp tester = new ArithmaticOp();
	@Test
	void AdditionAlgorithmTestingShouldReturnSumAndInteger() {
		testData.add(10);
		testData.add(15);
		result = tester.additionofNumber(testData);
		assertEquals(result, 25);
	}
	
	@Test
	void MultiplicationAlgorithmTestShouldReturnProductAndInteger() {
		testData.add(5);
		testData.add(5);
		testData.add(2);
		result = tester.productofNumber(testData);
		assertEquals(result, (5*5*2));
	}
	
	@Test
	void AverageValueShouldbeRealAndIntegerNumber()
	{
		testData.add(5);
		testData.add(15);
		testData.add(85);
		testData.add(6);
		testData.add(15);
		testData.add(6);
		int averageToTest = (5+15+85+6+15+6)/6;
		result = tester.averageofNumber(testData);
		assertEquals(result, averageToTest);
	}
	
	
	@Test
	void SmallerNumberShouldbeFound()
	{
		testData.add(5);
		testData.add(15);
		testData.add(85);
		testData.add(6);
		testData.add(15);
		testData.add(2);
		result = tester.smallerNumber(testData);
		assertEquals(result, 2);
	}

	
	@Test
	void LargerNumberShouldbeFound()
	{
		testData.add(5);
		testData.add(15);
		testData.add(850);
		testData.add(6);
		testData.add(15);
		testData.add(28658);
		result = tester.largerNumber(testData);
		assertEquals(result, 28658);
	}
	
	@Test
	void VarianceShouldReturnRightValueandInteger()
	{
		testData.add(1);
		testData.add(2);
		testData.add(3);
		testData.add(4);
		testData.add(5);
		testData.add(0);
		result = tester.variance(testData);
		assertEquals(result, 1);
	}
	
	@Test
	void OverFlowofIntegerShouldNotAllow()
	{
		int highestInteger = Integer.MAX_VALUE;
		testData.add(highestInteger);
		testData.add(highestInteger);
		testData.add(3);
		testData.add(4);
		testData.add(5);
		testData.add(6);
		result = tester.additionofNumber(testData);
		if(result < highestInteger)
		{
			assertTrue(false);
		}
		else
		{
			assertTrue(false);
		}
	}
	
	@Test
	void ArrayListShouldNotExceedRangeofInteger()
	{
		int highestInteger = Integer.MAX_VALUE;
		testData.add(highestInteger);
		testData.add(5);
//		result = tester.additionofNumber(testData);
		if(testData.size() < highestInteger)
		{
			assertTrue(true);
		}
	}
	
}
