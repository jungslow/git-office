package chapter04;

public class OpEx2 {

	public static void main(String[] args) {
		
		int a = 5 + 5;
		System.out.println("5 + 5 = "+a);
		
		int b = a - 5;
		System.out.println("10 - 5 = "+b);
		
		int c = b * 2;
		System.out.println("5 * 2 = "+c);
				
		int d = c / 5;
		System.out.println("10 / 5 = "+d);
		
		int e = 10 % 3;
		System.out.println("10 % 3 = "+e);
		
		a = 5;
		System.out.println("+a = "+ +a);
		System.out.println("-a = "+ -a);
		
		a = -5;
		System.out.println("+a = "+ +a);
		System.out.println("-a = "+ -a);
	}
}
