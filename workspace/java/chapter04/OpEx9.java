package chapter04;

public class OpEx9 {

	public static void main(String[] args) {
		int a = 5;
		int b = 4;
		int c = 3;
		
		// * 연산이 먼저 실杏
		System.out.println(a+b*c);
		
		// 괄호로 묶어 우선순위를 높임
		System.out.println((a+b)*c);

	}

}
