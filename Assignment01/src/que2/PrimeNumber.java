package que2;

import java.util.ArrayList;

public class PrimeNumber {
	public ArrayList getListInt(int number)
	{
		ArrayList primeList = new ArrayList<>();
		
		for (int count=2; count<=number; count++)
		{
			if ((count%2!=0 && count%3!=0 && count%5!=0 && count%7!=0) ||
					count == 2 || count == 3 || count == 5 || count == 7)
			{
				primeList.add(count);
			}
		}
//		System.out.println("operation is finished" + smallList);
		return primeList;
	}
}

