package chapter04;

public class OpEx5_2 {

	public static void main(String[] args) {
		
		int a= 10;
		int b = 5;
		
		//&연산: 양 쪽을 모두 확인 후 false, test()메서드 실행
		System.out.println(a==b & test());
		
		//&&연산: 앞이 false이므로 뒤의 test()메서드는 실행 안함
		System.out.println(a==b && test());
	}
	
	public static boolean test() {
		System.out.println("test()메서드 실행됨");
		return true;
	}
}
