import java.lang.System;
public class PEproblem30{
	public static boolean digit_power(int num){
		int tot = 0;
		int temp = num;
		boolean res = false;
		while (temp >= 1){
			tot += Math.pow(temp % 10,5);
			temp = (temp - (temp % 10)) / 10;
		}
		if (tot == num){
			res = true;
		}
		return(res);
	}
	public static int sum_digit_power(int limit){
		int tot = 0;
		for (int i = 2; i < limit; i++){
			if (digit_power(i)){
				tot += i;
			}
		}
		return(tot);
	}
	public static void main(String[] args){
		long start = System.nanoTime();
		int res = sum_digit_power(355000);
		float elapsed  = (float)(Math.pow(10,-9))*(float)(System.nanoTime() - start);
		System.out.format("The result is %d, and it took %.5f seconds %n",res,elapsed);
	}
}
