서버개발 언어

1. servlet/JSP => java계열
2. asp/c# => .net계열
3. php
4. nodejs => javascript
5. 장고/플라스크 => python: 카카오



Servlet/JSP => Spring



웹 어플리케이션이란?

요즘은 웹솔루션이라고 더 많이 한다.

웹 솔루션: 서버 프로그램





면접에서 나올 수 있는 질문 was 뭐 쓰셨나요?

웹서버를 어떻게 구성하셨나요? 

톰켓을 사용했습니다.

톰켓을 이용해서 was를 구성했습니다. 이렇게 대답할 수 있어야한다.



J2EE라는것이 있다. 

컨테이너에서 동작: Servlet, JSP, EJB

Servlet: java코드 안에 HTML코드가 포함 => 비지니스 처리 용이

JSP: HTML코드 안에 java코드가 포함 => 화면 처리 용이



JSP가 서블릿으로 변환되서 돌아간다. 



서버사이드 프로그램은 무엇인가?

웹어플리케이션서버(WAS)는 무엇인가?

Servlet/JSP 차이점과 공통점은 무엇인가?

- 서버사이드 프로그램을 개발하기 위해 사용
- 차이점: 비지니스 처리 용이, 화면처리 용이

멀티스레드를 이용해서 



jsp -> servlet변환 ->컴파일 -> 인스턴스화-> 초기화-> 실행



servlet-> 컴파일-> 인스턴스화 -> 초기화 -> 실행



서블렛 구현방법

- HttpServlet상속
- doGet, doPost 메서드 오버라이딩
- request, response사용 구현

