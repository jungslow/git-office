package chapter04;

public class OpEx5 {

	public static void main(String[] args) {
		int a = 10;
		int b = 5;
		
		// and 연산
		System.out.println(a > b && a ==10);	// true
		System.out.println(a > b && a ==b);		// false
		
		// or 연산
		System.out.println(a > b || a ==b);		// true
		System.out.println(a < b || a ==b);		// false
		
		// xor 연산 : 두 항목 중에서 하나만 참이면 참 
		System.out.println(a > b ^ a ==10);		// false
		System.out.println(a > b ^ a ==b);		// true
				
		// not 연산
		System.out.println(!(a > b ));			// false
		System.out.println(!(a < b ));			// true
	}
}
