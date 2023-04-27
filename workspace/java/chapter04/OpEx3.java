package chapter04;

public class OpEx3 {

	public static void main(String[] args) {
		
		int a = 10;
		int b = 10;
		
		++a;	//전위 연산
		b++;	//후위 연산
		System.out.println(a);
		System.out.println(b);
		
		int x = 10;
		int y = ++x;	// 먼저 x를 1증가시킨 후 y에 대입
		System.out.println("전위 연산 결과 y = "+y);
		
		x = 10;
		y = x++;		// 먼저 y에 x를 대입한 후 x는 1증가
		System.out.println("후위 연산 결과 y = "+y);
		System.out.println("x = "+x);
	}
}
