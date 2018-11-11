package que1;

import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.math.*;

public class basic_mathematical_operation{

	public static void main(String[] args) {
	
		// TODO Auto-generated method stub
		System.out.println("Enter any integer between 0 to 100:");
		Scanner scan = new Scanner(System.in);
		int number1 = scan.nextInt();
		
		System.out.println("You made a great choice!");
		System.out.println("Now add "+ number1+ " extra number");
		ArrayList<Integer> number = new ArrayList<Integer>();
		for (int count=0; count<number1; count++)
		{
			System.out.println("number remained to enter: "+(number1-count));
			number.add(scan.nextInt());
		}	
		scan.close();
	
		ArithmaticOp obj1 = new ArithmaticOp();
		int sumIs = obj1.additionofNumber(number);
		int productIs = obj1.productofNumber(number);
		int larger = obj1.largerNumber(number);
		int smaller = obj1.smallerNumber(number);
		int average = obj1.averageofNumber(number);
		int variance = obj1.variance(number);
		System.out.println("sum: "+sumIs);
		System.out.println("Product: "+productIs);
		System.out.println("average: "+average);
		System.out.println("smaller: "+smaller);
		System.out.println("larger: "+larger);
		System.out.println("variance: "+variance);
	}
}
