import java.util.Scanner;

public class Main{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		double n = scan.nextDouble();
		n = n / 30.48;
		double foot = Math.floor(n);
		n = (n - foot) * 12;
		double inch = Math.floor(n);
		System.out.format("%1.0f %1.0f", foot, inch);
	}
}
