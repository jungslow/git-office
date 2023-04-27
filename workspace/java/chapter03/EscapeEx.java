package chapter03;

public class EscapeEx {

	public static void main(String[] args) {
		String greet = "안녕하세요, \n저는 \"홍길동\"입니다.";
		String greet2 = "\t반갑습니다.";
		
		System.out.println(greet);
		System.out.println(greet2);
	}
}
