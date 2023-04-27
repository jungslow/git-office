package chapter04;

public class OpEx4 {

	public static void main(String[] args) {
		int a = 10; 
		int b = 5;
		
		System.out.println( a > b ); 	// true
		System.out.println( a >= b ); 	// true
		System.out.println( a < b ); 	// false
		System.out.println( a <= b ); 	// false
		System.out.println( a == b ); 	// false
		System.out.println( a != b ); 	// true
		
		boolean c = a == b;
		System.out.println(" c = "+c); 	// 변수 c에 결과값(false) 대입
		boolean d = c == false;
		System.out.println(" d = " +d); // 변수 d에 결과값 대입
	}
}
