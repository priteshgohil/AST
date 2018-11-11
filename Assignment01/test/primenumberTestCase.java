import static org.junit.Assert.assertThat;
import static org.junit.jupiter.api.Assertions.*;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.Before;
import org.junit.jupiter.api.Test;

import que2.PrimeNumber;

class primenumberTestCase {

	private ArrayList prime = new ArrayList<>();
	private ArrayList actual = new ArrayList<>();
	
	@Test
	public void testArrayInit(){
		assertTrue(prime.isEmpty());
		assertTrue(prime.size() == 0);
	}

	@Test
	public void enteredRangeShoulReturnListofPrimeNumber() {

		PrimeNumber tester = new PrimeNumber();
		
		prime.add(2);
		prime.add(3);
		prime.add(5);
		
		actual = tester.getListInt(3);
		assertEquals(prime.get(0),actual.get(0));
	}
	
	@Test
	public void zeroShouldReturnNullEntry() {
		PrimeNumber tester = new PrimeNumber();
		actual = tester.getListInt(0);
		assertTrue(actual.isEmpty());
	}
	
	
	@Test
	public void rangePassedShouldNotExceedPrimeCalculation() {
		int range = 150;
		PrimeNumber tester = new PrimeNumber();
		actual = tester.getListInt(range);
		int lastIndex = actual.size()-1;
		if((Integer)actual.get(lastIndex)<range) 
		{
			assertTrue(true);
		}
		else
		{
			assertTrue(false);
		}
	}
	
	
}