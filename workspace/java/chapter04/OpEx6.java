package chapter04;

public class OpEx6 {

	public static void main(String[] args) {

		System.out.println("2: "+ Integer.toBinaryString(2));
		System.out.println("3: "+ Integer.toBinaryString(3));
		
		// 비트 논리연산
		System.out.println("2&3: "+ (2&3));
		System.out.println("2|3: "+ (2|3));
		System.out.println("2^3: "+ (2^3));
		System.out.println("~3: "+ ~3);
		
		System.out.println("~3을 이진수로 : "+ Integer.toBinaryString(~3));
		System.out.println(Integer.toBinaryString(~3).length());
		System.out.println(Integer.MAX_VALUE);
		System.out.println(Integer.parseInt("1111111111111111111111111111100", 2)-Integer.MAX_VALUE-1);
	
		
	}

}
