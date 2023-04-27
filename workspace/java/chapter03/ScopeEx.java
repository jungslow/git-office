package chapter03;

public class ScopeEx {
	int no;		// class 블럭 내에서 사용 가능한 전역변수/멤버변수

	public static void main(String[] args) {
		// main 메서드 블럭내에서 사용 가능한 지역변수
		String name;
		
		if (true) {
			// 메서드 블럭 안에서 선언한 변수 사용 가능
			name = "홍길동";
			
			//if 블럭 안에서 변수 선언
			String email = "hong@test.com";
		}
		//if 블럭 밖에서 email변수를 상용하면 error발생
		//email = "hong@test.com";   

	}
}
