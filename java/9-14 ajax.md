dom이 뭐에요? 

다큐먼트오브젝트 모델

문서를 오브젝트화 해서 구조화한것

모델화해야 제어하기 용이하다.



DOM구현해야 속성

엘리먼트 프로퍼티 조작



## 부모/자식, 형제관계인지 파악해라



## 장남으로 할건지 막내로 할건지



## 부모가 앞인지 자식이 앞인지 위치파악



이걸 파악하고나면

append() // 막내아들 ( 뒤쪽으로들어감)

appendTo()

prepend()   // 첫째 아들 (앞쪽으로 들어감)

prependTo()

를 골라서 쓸 수 있다.



형제관계인지,

형인지 동생인지

- 나.before(형) 나를 기준으로 형을 전에 
- 형.insertBefore(나) 나를 기준으로 형을 삽입
-  insertAfter()
- After()

```
//$('b').appendTo($('div'))
		//$('div').append($('b'));
		//$('span').appendTo($('b'));
		//$('span').prependTo($('b'));
		//$('div').before($('b'));
		//$('b').insertBefore($('span'));
		$('b').insertAfter($('div'));
		alert($('body').html());
```



# each

# find

# wrap('태그') 태그로 감싸고싶을때사용

