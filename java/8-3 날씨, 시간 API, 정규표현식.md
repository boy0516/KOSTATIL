## 날씨, 시스템시간 API

- calendar클래스

Calendar gc = Calendar.getInstance();



- gc.get(Calendar.YEAR)+"년"
- (gc.get(Calendar.MONTH)+1)+"월"
  - MONTH는 +1을 해줘야 현재와 맞음
- gc.get(Calendar.DATE)+"일"
- gc.get(Calendar.MINUTE)+"분"



- gc.add(Calendar.DATE,100);
  - 일에 100을 추가해줌
- gc2.set(2020, 11, 25);
  - 날짜를 세팅해줌
  - 달은 11에 1을 더해서 12로 세팅됨



- SimpleDataFormat

  - SimpleDateFormat dataFormat = 
    				new SimpleDateFormat("yyyy-MM-dd hh:mm");
    - 포멧에 이용하는 기호는 자바책2권 379페이지를 참고
    - 참고링크: https://the-illusionist.me/41
  - 이런식으로 선언해줌
  - String str = dataFormat.format(//Date객체 ); 시간 포멧으로 문자열 만들어줌
  - dataFormat.parse(입력)에서 입력 형식이 맞지 않으면 예외가 발생하게 해준다.

  



- gc.getTime();
  - Calendar 객체를 Date객체로 바꿔줌



- gc.get(Calendar.DAY_OF_WEEK)
  - 1~7까지 일월화수목금토 에 맞게 출력됨



- gc.getActuralMaximum(Calendar.DATE);
  - 그 달이 31일인지 30일인지 28일인지 아무튼 알 수 있다.



이렇게 SimpleDataFormat으로 선언해준 객체에 키보드 입력을 받을때 

```
SimpleDateFormat sd = new SimpleDateFormat(pattern);
Scanner sc  = new Scanner(System.in);
Date inDate = null;

while(sc.hasNextLine()) {
			
	try {
		inDate = sd.parse(sc.nextLine());
		break;
	} catch (Exception e) {
		System.out.println("날짜를"+ pattern+"의 형태로 다시 입력해주세요");
	}
}
```

sd.parse()를 이용해서 입력받은 문자열을 Date형식으로 변환을 해준다. 이때 우리가 쓰기 편하게 하기 위해 

Calendar형태로 바꿔준다. 

```
Calendar cal = Calendar.getInstance();
cal.setTime(inDate);
Calendar today = Calendar.getInstance();
```

이렇게 해주고 아래 코드로 값을 계산해준다.

```
long day = (today.getTimeInMillis() - cal.getTimeInMillis())/(24*60*60*1000);
System.out.println(today.getTimeInMillis());
int m = (int)(day/30);
int year = m/12;
int month = m%12;
		
System.out.println("결과"+year+"년"+month+"개월");
```



Calendar클래스의 

- getTimeInMillis()
  - 천분의 일초단위로 반환

자바책2권 382p 참고

관련 참고링크: https://jamesdreaming.tistory.com/103

****



# 정규표현식

특정한 규칙(패턴)을 가진 문자열의 집합을 표현하는데 사용하는 표현식 언어

### 정규표현식 문법

- `.` :  `.`이 위치한 곳에는 반드시 임의의 한글자가 위치해야한다는 의미

  ex) a.b 이렇게 되면 acb, azb등과 같다.

- `*` :  `*`바로앞의 문자가 없거나 하나 이상 반복한다는 의미 

  ex) Hello* 는 Hell, Hello, Helloooo 등과 같다. 

- `+` :  `+`바로 앞의 문자가 하나이상 반복한다는 의미

  ex) Hello+ 는 Hello, Hellooo 등과 같다. 

- `?` : `?` 바로앞의 문자가 없거나 하나임을 의미

  ex) A?c 는 c, AC 중에서 하나이다.

  ex) Hello? 는 Hell, Hello 중에 하나이다.

- `^` : 문장의 처음을 나타내며, `^`가 있는 단어로 문장이 시작됨을 의미

  ex) ^Hello는 Hello World, Hello Java 등과 같다.

- `$` : 문장의 끝을 나타내며, `$`가 있는 단어로 문장이 끝남을 의미

  ex) World$ 는 HelloWorld 등과 같다.

- `[]` : 괄호 안의 문자 중 잋리하는 것을 검색할 경우 사용

```
[a,b,c]에 일치하는 문자열예시
a, b, c, ab, abc등

^[a-zA-Z0-9] : 영문대소문자 숫자로 시작하는 문자열검색
```

- `[]`안에서의 `^` : `[]`안에 있는 문자를 포함하고 있지 않는 모든 문자열을 찾고자 할 경우

```
[^abc]de에 일치하는 문자열예시
dde, fde, zde등
```

- `{}`: 특수분자 앞의 문자가 반복되는 횟수를 의미

  ex) hel{2}o 는 hello와 같다.

- `()`: `()`안의 문자열을 하나의 문자로 취급

  (hello){3}은 hellohellohello와 같다.



- or연산

  ex) Hi|Hello 는 Hi 또는 Hello가 포함된 문자열이다.





### 문자 클래스

- \p{Alpha}
  - 모든 영문자
- \p{Digit}
  - 숫자[0-9]
- \p{Alnum}
  - 영문과 숫자
- \p{Space}
  - 공백





### 특수 문자 사용

- 해당 특수문자 앞에 역슬레스\를 사용해줘야한다. 
  - 두번 써줘야함. 
  - ex) 점을 찍고싶으면 \\\\\. 이렇게 



### 기타 표현

- \w :  알파벳이나 숫자

- \W : 알파벳이나 숫자를 제외한 문자

- \d : 숫자와 동일

- \D : 숫자를 제외한 모든 문자

- ^[0-9]*$ : 숫자만 
  - = \p{Digit}

- ^[a-zA-Z]*$ : 영문자
  - \p{Alpha}
- ^[가-힣]*$ : 한글만
- ^[a-zA-Z0-9]*$ : 영어/숫자만
  - \p{Alnum}
- [[:space:]] : 공백
  - \p{Space}



### 예제

- //abc 문자 포함 여부

		//abc 문자 포함 여부
		if(str.matches(".*abc.*")) {
			System.out.println("매칭");
		}else {
			System.out.println("비매칭");
		}

- //숫자만 3자리 유무 판단

		//숫자만 3자리 유무 판단
		if(str.matches("^[1-9][0-9]{2}$")) {
			System.out.println("매칭");
		}else {
			System.out.println("비매칭");
		}
		
		//숫자만 3자리 유무 판단
		if(str.matches("[\\d]{3}")) {
			System.out.println("매칭");
		}else {
			System.out.println("비매칭");
		}



- 알파벳, 숫자만 5자리 이상

		// 알파벳, 숫자만 5자리 이상
		if(str.matches("[\\w]{5,}")) {
			System.out.println("매칭");
		}else {
			System.out.println("비매칭");
		}



- 한글 3~5자리 입력

		// 한글만 3~5자리 입력
		if(str.matches("[가-힣]{3,5}")) {
			System.out.println("매칭");
		}else {
			System.out.println("비매칭");
		}



### 예시 미션

- 이메일 관련 검증
  //dolsam77@nate.com => 매칭
  //432dolsam@nate.com => 비매칭(숫자시작
  //dolsam77nate.com => @ 없음 비매칭
  //dolsam77@nate.comcomㅡ => 비매칭

		//내풀이
		if(str.matches("^[\\d].*")) {
			System.out.println("비매칭");
		}else if(!str.matches(".*@.*")){
			System.out.println("비매칭");
		}else if(!str.matches(".*\\.com")){
			System.out.println("비매칭");
		}else System.out.println("매칭");

```
	//강사풀이
	if(str.matches("^[\\D]\\w+@\\w+\\.\\w{2,3}$")) {
		System.out.println("매칭");
	}else { 
		System.out.println("비매칭");
	}
```



- 이미지파일 구별
  // abc.jpg, abc.gif, abc.PNG, abc.txt
  // (?i) => 소대문자 구분없이	

	// 내 풀이
		if(str.matches("^[\\D]\\w+\\.+(?i)(jpg|gif|PNG|txt)")) {
			System.out.println("매칭");
		}else { 
			System.out.println("비매칭");
		}

	// 강사풀이
	if(str.matches("^\\S+\\.+(?i)(jpg|gif|PNG|txt)")) {
			System.out.println("매칭");
		}else { 
			System.out.println("비매칭");
		}





### 문자열에 특정문자 바꿔주는법

- 문자열.replaceAll("특정문자", "바꾸고싶은 문자")



위에서 문자열을 matches하는것도 있지만 



#### java.util.regex패키지의 Pattern클래스

Pattern을 이용해도 된다.

이용 예시

		String data[] = {
				"bat", "bba", "bbg", "bonus",
				"CA", "ca", "c232", "car",
				"date", "dic", "diraaa"
		};
		
		Pattern p = Pattern.compile("c[a-z]*");
		
		for(int i = 0; i < data.length; i++) {
			Matcher m = p.matcher(data[i]);
			if(m.matches()) {
				System.out.println(data[i]);
			}
		}

이런식으로 Pattern객체에 정규표현식 패턴을 생성하고 Matcher 객체를 이용해서 비교해줄수도 있다. 



### 오늘의 총 정리 문제 

```java
package kosta.api;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Test {

	public static void main(String[] args) {
//		서울특별시 마포구에 사는 사람은 1명
//		부산광역시 동구에 사는 사람은 2명
//		서울특별시 중랑구에 사는 사람은 2명
//		서울특별시 노원구에 사는 사람은 1명
//		인천광역시 남동구에 사는 사람은 1명
//		경기도 구리시에 사는 사람은 1명
//		서울 중랑구에 사는 사람은 1명
//		서울특별시 구로구에 사는 사람은 1명
//		충청남도 예산군에 사는 사람은 1명
//		충청남도 천안시에 사는 사람은 1명
//		충청남도 당진시에 사는 사람은 1명
		
		String reg = "(([가-힣]+(시|도))|서울|부산|대구|광주|울산|인천)\\s[가-힣]+(시|구|군)";
		//~시에 살거나 서울, 인천, 대구, 광주, 부산, 울산 의 주소를 가지고 뒤쪽에 시, 군,구 로 끝나는 부분을
		Map<String, Integer> map = new HashMap<String, Integer>();
		//키워드와 갯수를 가지는 리스트에
		String[] addresses = { "서울특별시 중랑구 공릉로 13길 27", "서울특별시 중랑구 겸재로 68 (면목동)",
				"서울특별시 노원구 공릉로 95 (공릉동)",
				"서울특별시 구로구 가마산로 77 (구로동)", "서울특별시 마포구 가양대로 1 (상암동)",
				"충청남도 천안시 동남구 성남면 5산단1로 22",
				"부산광역시 동구 고관로 5 (초량동)", "인천광역시 남동구 간석로 2 (간석동)",
				"충청남도 예산군 신암면 오신로 852-2", "충청남도 당진시 우강면 박원로 138",
				"부산광역시 동구 중앙대로 243-13 (초량동)", "경기도 구리시 동구릉로136번길 47 (인창동)",
				"서울 중랑구 공릉로 13길 27" };		
		
		Pattern p = Pattern.compile(reg);
		for (String address : addresses) {
			Matcher m = p.matcher(address);
			if (m.find())
				map.put(m.group(), map.getOrDefault(m.group(), 0) + 1);
		}

		for (Entry<String, Integer> s : map.entrySet())
			System.out.println(s.getKey() + "에 사는 사람은 " + s.getValue() + "명");

	}

}

```



여기서 핵심은 

#### String reg = 

#### "(([가-힣]+(시|도))|서울|부산|대구|광주|울산|인천)\\\s[가-힣]+(시|구|군)";

이 부분을 작성하는것.

내가 틀린부분은 __\\\s__를 이용해서 공백을 처리해주지 않아서 답이 나오지 않음.



\\\\s 를이용해서 공백을 잘 처리해주도록하자
