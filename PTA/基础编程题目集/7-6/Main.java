import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		f();
	}

	private static void f(){
		Scanner in = new Scanner(System.in);
		double d1 = in.nextDouble();
		int n = in.nextInt();
		char c = in.next().charAt(0);
		double d2 = in.nextDouble();
		System.out.printf("%c %d %1.2f %1.2f", c, n, d1, d2);
	}
}
