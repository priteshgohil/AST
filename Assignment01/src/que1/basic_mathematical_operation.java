package que1;

import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.math.*;

public class basic_mathematical_operation {

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
		int totalSum = 0;
		int prevData = 1;
		int totalProduct = 0;
		int average = 0;
		int smallest = 0;
		int largerst = 0;
		
		int dataSize = number.size();
		for(int data : number)
		{
			totalSum = totalSum + data;
			totalProduct = data * prevData;
			prevData = totalProduct;
			if(smallest>data)
			{
				smallest = data;
			}
			if(largerst<data)
			{
				largerst = data;
			}
		}
		average = totalSum/dataSize;
		
//		for calculating variance
		int variance = 0;
		for(int data : number)
		{
			variance += Math.pow((data-average), 2);
		}
		variance = variance/(dataSize-1);
		variance = (int) Math.sqrt(variance);
		
		System.out.println("Sum is: " +totalSum);
		System.out.println("Product is: " +totalProduct);
		System.out.println("Average is: " +average);
		System.out.println("variance is: " +variance);
		System.out.println("Smallest number is: "+smallest);
		System.out.println("Smallest number is: "+largerst);
		}
}