## 자바 HashMap

HashMap은 Map 인터페이스를 구현한 대표적인 Map 컬렉션이다.

Map인터페이스를 상속하고 있기에 Map의 성직을 그대로 가지고 있습니다.

Map은 키와 값으로 구성된 Entry객체를 저장하는 구조를 가지고 있는 자료구조입니다. 여기서 키와 값은 모두 객체입니다. 값은 중복 저장될 수 있지만 키는 중복 저장될 수 없다.

만약 기존에 저장된 키와 동일한 키로 값을 저장하면 기존의 값은 없어지고 새로운 값으로 대치된다. HashMap은 이름 그대로 해싱(Hashing)을 사용하기 때문에 많은 양의 데이터를 검색하는데 있어서 뛰어난 성능을 보인다. 

HashMap은 내부에 '키'와 '값'을 저장하는 자료 구조를 가지고 있다.

HashMap은 해시 함수를 통해 키와 값이 저장되는 위치를 결정하므로 사용자는 그 위치를 알 수 없고, 삽입 되는 순서와 들어있는 위치 또한 관계가 없다.

- HashMap선언

```
HashMap<String, String> map1 = new HashMap<String, String>();//Hashmap생성
HashMap<String, String> map2 - new HashMap<>();//new에서 타입 파라미터 생략가능
HashMap<String, String> map3 = new HashMap<>(map1);//map의 모든 값을 가진 HashMap생성
HashMap<String, String> map4 = new HashMap<>(10);//초기 용략(capacity)지정
HashMap<String, String> map5 = new HashMap<>(10, 0.7f);//초기 capacity, load factor지정
HashMap<String, String> map6 = new HashMap<String, String>(){{//초기값 지정
	put("a","b");
}}
```

HashMap을 생성하려면 키 타입과 값 타입을 파라미터로 주고 기본생성자를 호출하면 된다.

- HashMap은 저장 공간보다 값이 추가로 들어오면 List처럼 저장공간을 추가로 늘리는데 List처럼 저장공간을 한 칸씩 늘리지 않고 __약 두배로__ 늘린다.여기서 과부하가 많이 발생합니다. 
- 그렇기에 초기에 저장할 데이터 개수를 알고 있다면 Map의 초기 용량을 지정해 주는것이 좋다. 



- HashMap 값 추가

```
HashMap<Integer, String> map = new HashMap<>();//new에서 타입 파라미터 생략가능
map.put(1, "사과"); //값 추가
map.put(2, "바나나");
map.put(3, "포도");
```

HashMap에 값을 추가하려면 put(key,value) 메소드를 사용하면 된다.

만약 입력되는 키 값이 HashMap 내부에 존재한다면 기존의 값은 새로운 입력되는 값으로 대치

- HashMap 값 삭제

```
map.remove(1); //key값 1 제거
map.clear(); //모든 값 제거
```



- HashMap 값 출력

```
HashMap<Integer, String> map = new HashMap<Integer, String(){{
	put(1,"사과");
	put(2,"바나나");
	put(3,"포도");
}}

System.out.println(map); //전체 출력: {1=사과, 2=바나나, 3=포도}
System.out.println(map.get(1)); //key값 1의 value얻기 : 사과

//entrySet() 활용
for (Entry<Integer, String> entry : map.entrySet()){
	System.out.println("[Key:]"+entry.getKey() + "[Value]:"+ entry.getValue());
}
//[Key]:1 [Value]:사과
//[Key]:2 [Value]:바나나
//[Key]:3 [Value]:포도

//KeySet() 활용
for(Integer i : map.keySet()){
	System.out.println("[Key]:"+i+"[Value]:"+map.get(i));
}
//[Key]:1 [Value]:사과
//[Key]:2 [Value]:바나나
//[Key]:3 [Value]:포도
```

전체 출력에는 entrySet()

키 값만 필요한 경우 keySet()

단 key값을 이용해서 value를 찾는 과정에서 시간이 많이 소모되므로 많은 양의 데이터를 가져와야 한다면 entrySet()이 효율적. (약 20%~200%의 성능저하)



- Iterator사용

```
HashMap<Integer,String> map = new HashMap<Integer,String>(){{//초기값 지정
    put(1,"사과");
    put(2,"바나나");
    put(3,"포도");
}};

//entrySet().iterator()
Iterator<Entry<Integer, String>> entries = map.entrySet().iterator();
while(entries.hasNext()){
	Map.Entry<Integer, String> entry = entries.next();
	System.out.println("[Key:]"+entry.getKey() + "[value]:"+ entry.getValue());
}
//[Key]:1 [Value]:사과
//[Key]:2 [Value]:바나나
//[Key]:3 [Value]:포도

//keySet().iterator()
Iterator<Integer> keys = map.keySet().iterator();
while(keys.hasNext()){
	int key = keys.next();
	System.out.println("[key]:"+ key + "[value]"+ map.get(key));
}
//[Key]:1 [Value]:사과
//[Key]:2 [Value]:바나나
//[Key]:3 [Value]:포도
```





