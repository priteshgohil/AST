package que1;

import java.util.ArrayList;
import java.math.*;

public class ArithmaticOp {
	public int result;
	public int additionofNumber(ArrayList<Integer> data) {
//		int dataSize = data.size();
//		int totalSum = 0;
		result =0;
		for (int num: data)
		{
			result = result + num;
		}
		return result;
	}
	
	public int productofNumber(ArrayList<Integer> data) {
		result = 0;
		int prevData = 1;
		for (int num: data)
		{
			result = num * prevData;
			prevData = result;
		}
		return result;
	}
	
	public int largerNumber(ArrayList<Integer> data) {
		result =data.get(0);
		for (int num: data)
		{
			if(result<num)
			{
				result = num;
			}
		}
		return result;
	}
	public int smallerNumber(ArrayList<Integer> data) {
		result =data.get(0);
		for (int num: data)
		{
			if(result>num)
			{
				result = num;
			}
		}
		return result;
	}
	
	public int averageofNumber(ArrayList<Integer> data) {
		int dataSize = data.size();
		result = additionofNumber(data)/dataSize;
		return result;
	}
	
	public int variance(ArrayList<Integer> data) {
		result =0;
		int dataSize = data.size();
		int averageIs = averageofNumber(data);	
		for (int num: data)
		{
			result += Math.pow((num-averageIs), 2);
		}
		result = result/dataSize;
		result = (int) Math.sqrt(result);
		return result;
	}
}

