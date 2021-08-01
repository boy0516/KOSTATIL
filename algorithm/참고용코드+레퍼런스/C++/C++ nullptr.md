# C++ nullptr

포인터를 null로 초기화 할때 사용



### NULL, nullptr 차이점



C++에서 NULL의 정의

```c++
#ifndef NULL
	#ifdef __cplusplus
		#defin NULL 0
	#else
		#define NULL ((void *)0)
	#endif
#endif
```

위 코드의 뜻은 

C++에서는 NULL을 0으로 사용하고

C++이 아닌 C에서는 NULL을 ((void*)0)으로 치확해서 사용하겠다는 뜻



그래서 가짜 포인터를 쓰지말고 nullptr을 사용하자. 