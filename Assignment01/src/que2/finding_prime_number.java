package que2;
//import java.util.*;
//import java.util.ArrayList;
import java.util.Scanner;
import java.math.*;
import java.util.ArrayList;

public class finding_prime_number {
	public static int highestInt = 0;
	public static long highestLong = 0;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		highestInt = Integer.MAX_VALUE ;
//		highestLong = Long.MAX_VALUE;
//		System.out.println(highestInt+" "+highestLong);
//		creating list array to store our prime number
		ArrayList smallList = new ArrayList<>();
		
//		get user input to calculate the prime number
		System.out.println("Enter the last number of range to calculate the prime number: ");
		Scanner scan = new Scanner(System.in);
		int range = scan.nextInt();
		for (int count=2; count<=range; count++)
		{
			if ((count%2!=0 && count%3!=0 && count%5!=0 && count%7!=0) ||
					count == 2 || count == 3 || count == 5 || count == 7)
			{
				smallList.add(count);
			}
		}
		System.out.println("operation is finished");
		System.out.println("prime numbers are " +smallList);
	}
}