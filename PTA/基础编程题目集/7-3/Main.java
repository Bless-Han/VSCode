import java.util.Scanner;

public class Main{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int m = in.nextInt();
		int n = change(m);
		System.out.println(n);
	}

	public static int change(int m){
		return m % 10 * 100 + m % 100 / 10 * 10 + m / 100;
	}
}
