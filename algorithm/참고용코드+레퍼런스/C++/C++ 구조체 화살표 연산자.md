# C++ 구조체, 사용법

구조체는 사용자 정의 데이터 형식

구조체는 다른 유형의 항목들을 단일 유형으로 그룹화하는데 사용



- 선언방법

```
struct student {
    char name[20];
    char address[100];
    int age;
};
```



구조체 변수 선언 방법

방법1

```
struct Point {
    int x;
    int y;
} p1;
```

방법2

```
struct Point {
    int x;
    int y;
};
 
int main(void) {
    struct Point p1;
}
```



# C++ -> 연산자

구조체 포인터 안의 구조체 변수에 쉽게 접근하기 위해 사용



예시)

```
typedef struct
{
	int data;	
} A;
```

위의 구조체를 이용하기 위해

초기화 또는 동적할당을 해줘야한다. 

```
A a1 = {1};
```

```
A *a = (A*)malloc(sizeof(A));
```



이후 구조체 포인터 안에 있는 data 변수에 접근하려면

```
int testdata = (*a).data;
```

이렇게 접근해야함



### 이때  -> 연산자를 쓴다면

```
a -> data; 
```

와 같이 사용하면 해당 주소 안의 data라는 변수에 접근하는 것과 같다. 

