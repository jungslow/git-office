package chapter04;

public class OpEx6_1 {

	public static void main(String[] args) {
		
		// << 연산
		System.out.println(3<<2);
		System.out.println("3의 2진수 : "+ Integer.toBinaryString(3));
		System.out.println("12의 2진수 : "+ Integer.toBinaryString(12));
		
		// >> 연산
		System.out.println(8<<2);
		System.out.println("8의 2진수 : "+ Integer.toBinaryString(8));
		System.out.println("2의 2진수 : "+ Integer.toBinaryString(2));
				
		// >>> 연산
		System.out.println(-8>>>3);
		System.out.println("-8의 2진수 : "+ Integer.toBinaryString(-8));
		System.out.println("-8 >>> 3 : "+ Integer.toBinaryString(-8 >>> 3));
		
	}

}
