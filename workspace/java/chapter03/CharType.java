package chapter03;

public class CharType {
	public static void main(String[] args) {
		char a = 'A';
		System.out.println("a: "+a);
		
		int b = a;
		System.out.println("b: "+b);
		
		int c = 66;
		System.out.println("c: "+c);
		
		int d = a + b;
		System.out.println("d: "+d);
		
		//char c = 'hello' : error!!! char에는 한 문자만 대입 가능
		String str = "Hello";
		System.out.println("String: "+str);
		}
}
