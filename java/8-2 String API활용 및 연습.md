# API

### API 종류 예시

- Integer.parseInt(), Math.random(), Scanner sc  = new Scanner(System.in); sc.nextInt()

기초클래스

- Object, Wrapper, String, StringBuffer, Calendar, SimpleDataFormat, 정규표현식



자료구조 클래스

- List(ArrayList),  Map(HashMap), Set(TreeSet)



입출력 클래스

- Input/Output stream



멀티스레드 클래스

- 동시성 프로그램(Thread, Runnable)



네트워크 클래스

- Socket => 채팅



테스트, Json 클래스

- JUnit, Data전달



- - - 편리한 추가 내용

object클래스에는 toString이라는 메서드가 정의되어있는데 이는 system.out.println(참조변수)

하면 참조변수에 저장된 주소값이 출력되는데 

toString을 오버라이딩 해서 내부 값을 출력되게 해주면 

system.out.println(참조변수)하면 내부 값이 출력되게 해줄 수 있다.

@@ 이 부분은 제너레이트 toString이 따로 편의 기능이 있다. 이용해주자.



equals도 원래는 주소값을 비교해주는건데 오버라이딩을 통해 원하는기능으로 이용해줄 수 있다.



### wrapper클래스

프리미티브 타입을 객체로 표현하는데 사용되는 다음 클래스들의 통칭

왜 필요하느냐? 

기본형데이터형과 레퍼런스형 두가지가 있는데

기본형은 기본형끼리 데이터

기본형 <=> 레퍼런스 형 기본형 값을 레퍼런스형으로 변환해줄때 wrapper클래스가 필요

Object obj = 10; //wrapper클래스가 없다면 안된다. 

Object obj2 = new Integer(10);// 이렇게 해주면 된다. 

int n = obj2.intValue(); 다시 int값을 가져올때는 이렇게 변환해주면 된다.



### Boxing과 Unboxing

자동 Unboxing이 일어나는 경우

```
Integer obj = new Integer("10");
int sum = obj +20; // Integer객체와 int타입의 값을 더하는 명령문
```

자동으로 Unboxing이 일어나서 계산이 된다.



자동으로 Boxing이 일어나는 경우

```
static void printDouble(Double obj){
}

pringDouble(123.45);// 이렇게 쓰면 자동으로 Boxing이 일어남
```



### 문자열 관련 클래스

- 문자열 불변성

  문자열을 함수를 통해 변경해도 원본은 변하지 않는다.

  다른 변수를 통해 받아주거나 스스로 다시 받거나 해야한다

  아무튼 concat이나 + 연산등을 통해 문자열을 추가해줄 수 있다.

```
		String str = "ABC";
		String str2 = new String("def");
		
		//String 불변성
		str.concat(str2);
		System.out.println(str);
		
		//str은 변하지 않음
		
		String sql = "select * from board ";
		int num = 10;
		
		if(num == 10) {
			sql += "where num = 10";
		}
		
		System.out.println(sql);
```



- StringBuffer
  - 문자열을 보완하기 위해 나온 StringBuffer
  - append()를 이용해서 원본에 문자열 추가 가능

```
StringBuffer sb = new StringBuffer("가나다");
sb.append("라마바");
System.out.println(sb);
```



- indexOf("문자열")
  - 해당 문자열의 위치를 파악

```
String sql = "select * from board ";
sql += "where num = 10";

System.out.println(sql.indexOf("board"));

//출력 = 14
```



- length()
  - 해당 문자열의 길이를 파악



- charAt()
  - 인텍스에 해당하는 문자 출력 => charAt(인덱스)



- subString()
  - 문자열 부분추출

```
//문자열 부분추출: subString(5),subString(5,10)
//select * from board where num = 10
System.out.println(sql.substring(3,5));
```



### 중요 예시)파일명과 확장자를 분리

```
String fileName = "kosta.jpg";
String head = fileName.substring(0,fileName.indexOf("."));
String pattern = fileName.substring(fileName.indexOf("."),fileName.length());

System.out.println(head);
System.out.println(pattern);
```

이렇게 분리할 수 있다.



- endsWith("문자열")
  - 해당 문자열로 끝나는지 true false로 반환
- startsWith("문자열")
  - 해당 문자열로 시작하는지 true false로 반환



- equalsIgnoreCase()
  - 대소문자  구분없이 비교



- toLowerCase()
  - 문자열 소문자로 변경
- toUpperCase()
  - 문자열 대문자로 변경



- - - 참고) 문자 하나 대문자 변환 Character.toUpperCase(문자);



### 중요) 공백문자 처리

- trim()
  - 문자열의 앞뒤로 공백문자를 제거



- split(" ")
  - " "를 기준으로 나눔
- 문자열 => 배열로 변환

```
String fruits = "사과 포도 수박 배";
String arr[] = fruits.split(" ");
System.out.println(Arrays.toString(arr));
```

```
[사과, 포도, 수박, 배]
```



- join(" ")
  - " "를 기준으로 결합



- toCharArray()
  - 문자열을 각 문자별로 배열로 변환

```
System.out.println(Arrays.toString(fruits.toCharArray()));
```

```
[사, 과,  , 포, 도,  , 수, 박,  , 배]
```



