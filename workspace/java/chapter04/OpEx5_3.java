package chapter04;

public class OpEx5_3 {

	public static void main(String[] args) {
		int a= 10;
		int b = 0;
		
		//&연산: 양 쪽을 모두 확인 후 
		//System.out.println(b > 0 & (a/b >0));
		
		//&&연산: 앞이 false이므로 뒤는 실행 안함
		System.out.println(b > 0 && (a/b > 0));

	}
}
