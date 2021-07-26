# Hash 
- 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수  
- python의 딕셔너리 느낌

## C++ (Library x)
- 해시 충돌
    - 해시 결과가 동일한 경우 해시 충돌
    - 해시 충돌 해결 방법
        - 체이닝 (같은 해시값에 연결리스트로 연결)
        - 개방 주소(선형: 뒤에 빈 공간에 삽입)
- 구현할 것
    - Hash table 구조체 (클래스)
    - hash함수
    - hash find 함수 (table에서 해당 data 찾기)
    - hash add 함수 (table에 data 추가)
```cpp
#include <stdio.h>
#include <string.h>
#include <memory.h>
 
#define MAX_KEY 64
#define MAX_DATA 128
#define MAX_TABLE 4096
 
typedef struct
{
    char key[MAX_KEY + 1];
    char data[MAX_DATA + 1];
}Hash;
Hash tb[MAX_TABLE];
 
unsigned long hash(const char *str)
{
    unsigned long hash = 5381;
    int c;
 
    while (c = *str++)
    {
        hash = (((hash << 5) + hash) + c) % MAX_TABLE;
    }
 
    return hash % MAX_TABLE;
}
 
int find(const char *key, char *data)
{
    unsigned long h = hash(key);
    int cnt = MAX_TABLE;
 
    while (tb[h].key[0] != 0 && cnt--)
    {
        if (strcmp(tb[h].key, key) == 0)
        {
            strcpy(data, tb[h].data);
            return 1;
        }
        h = (h + 1) % MAX_TABLE;
    }
    return 0;
}
 
int add(const char *key, char *data)
{
    unsigned long h = hash(key);
 
    while (tb[h].key[0] != 0)
    {
        if (strcmp(tb[h].key, key) == 0)
        {
            return 0;
        }
 
        h = (h + 1) % MAX_TABLE;
    }
    strcpy(tb[h].key, key);
    strcpy(tb[h].data, data);
    return 1;
}
 
 
int main(int argc, char* argv[])
{
    int T, N, Q;
 
    scanf("%d", &T);
 
    for (int test_case = 1; test_case <= T; test_case++)
    {
        memset(tb, 0, sizeof(tb));
        scanf("%d", &N);
        char k[MAX_KEY + 1];
        char d[MAX_DATA + 1];
 
        for (int i = 0; i < N; i++)
        {
            scanf("%s %s\n", &k, &d);
            add(k, d);
        }
 
        printf("#%d\n", test_case);
 
        scanf("%d", &Q);
        for (int i = 0; i < Q; i++)
        {
            char k[MAX_KEY + 1];
            char d[MAX_DATA + 1];
 
            scanf("%s\n", &k);
 
            if (find(k, d))
            {
                printf("%s\n", d);
            }
            else
            {
                printf("not find\n");
            }
        }
    }
    return 0;
}
```
## C++ (STL-hash_map)
- 많은 자료 저장, 검색 속도 빨라야할 때
- 너무 빈번하게 자료 삽입, 삭제하지 않을 때
```cpp
#include<hash_map>
using namespace std;

int main(void) {

	//변수선언!
	hash_map<int, float> hash1;	//hash_map 선언
	hash_map<int, float> *hash2 = new hash_map<int, float>;	//hash_map 동적할당

	//자료추가 = insert() 함수
	hash1.insert(hash_map<int, float>::value_type(10, 45.6f));	//단순 추가
	hash1.insert(hash1.begin(), hash_map<int, float>::value_type(11, 50.2f));	//특정위치에 추가
	hash2->insert(hash1.begin(), hash1.end());	//지정한 구간에 있는것들 추가

	//삭제
	hash1.erase(hash1.begin());		//첫번째 위치의 요소 삭제
	hash1.erase(hash1.begin(), hash1.end());	//처음~마지막 삭제
	hash1.erase(11);		//key가 11인 요소 삭제

	//검색 - key를 사용해 같은 key를 갖고 있는 요소를 찾음(찾으면 iterator 반환, 아니면 end() 반환)
	hash_map<int, float>::iterator Finditer = hash1.find(10);
	if (Finditer != hash1.end())
		Finditer->second = 290.44f;

}
```
## Python 
해시 테이블은 키 밸류를 기반으로 데이터를 저장한다. 파이썬에서는 딕셔너리가 있어서 굳이 만들 필요는 없는데, 아무래도 파이썬으로 코드를 짜면 간단해서 파악하기 쉽다는 장점이 있다.

위 이미지에서 문자열 데이터는 해쉬 함수를 거쳐 숫자로 변경된다. 변경된 이 값(해시)를 배열(buckets)의 키로 삼아 밸류를 저장한다. 

따라서 데이터를 서칭하는 과정에서 배열을 순차적으로 탐색할 필요없이 해시 함수를 거쳐 생성된 해시 값으로 데이터를 빠르게 찾을 수있다. 딕셔너리의key-value구조와 유사하다.

키(key): 인풋데이터 

값(value): 저장할 데이터

해시함수(hash function): 키를 해시로 변경해주는 함수



위 이미지에서 문자열 데이터가 hash function을 거쳐 숫자열 데이터로 변경된다.

ex) john Smaith -> 02



해시(Hash): 인풋 데이터를 고정된 길이의 숫자열로 변화한 결과물



즉 문자열로 들어온 인풋 데이터를 해시 함수를 통해 숫자열로 변경해주고, 이 숫자를 키 값 삼아서 배열(buckets)에 값을 저장하는 구조다. (파이썬 해시 함수의경우 환경마다 아웃풋이 달라서 hashlib의 sha1, sha256을 쓰기도 한다.)



```python
# Hash Table
class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key
   	def hashFunction(self, key):
        return key % self.size
    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
    def save(self, key, value):
        hash_address = self.getAddress(key)
        self.hash_table[hash_address] = value
    def read(self, key):
        hash_address = self.getAddress(key)
        return self.hash_table[hash_address]
   	def delete(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
       	else:
            return False

#Test Code
h_table = HashTable(8)
h_table.save('a', '1111')
h_table.save('b', '3333')
h_table.save('c', '5555')
h_table.save('d', '8888')
print(h_table.hash_table)
print(h_table.read('d'))

h_table.delete('d')

print(h_table.hash_table)
    
```

출력


```
[0, '1111', '3333', '5555', '8888', 0, 0, 0]
8888
[0, '1111', '3333', '5555', 0, 0, 0, 0]
```



문제점: 해시 충돌(Hash Collision)

해시 테이블에는 치명적인 문제점이 있다. 인풋 데이터를 해시 값으로 바꿔주는 과정에서 두 데이터가 다른 문자열임에도 불구하고 같은 숫자로 변환되는 경우가 있다. 이 문제를 해시 충돌이라고 한다.



해시 충돌을 해결하는 대표적인 방법에는 오픈해싱과 클로즈 해싱이 있다.

## Python - 오픈 해싱(Open Hashing)

오픈 해싱은 해시 테이블의 충동 문제를 해결하는 대표적인 방법중 하나로 체이닝(Separate Chaining) 기법이라고도 한다. 만약 해시 값이 중복되는 경우, 먼저 저장된 데이터 링크드 리스트를 이용하여 중복 해시 데이터를 연결한다.



파이썬에서는 굳이 링크드 리스트를 안 쓰고 슬롯을 이중 리스트로 활용해서 간단하게 구현할 수 있다.

```python
# open hashing
class OpenHash:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
    def getkey(self, data):
        self.key = ord(data[0])
        return self.key
    def hashFunctions(self, key):
        return key % self.size
    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address
	def save(self, key, value):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
        	for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    self.hash_table[hash_address][a][1] = value
                    return
            self.hash_table[hash_address].append([key, value])
        else:
            slef.hash_table[hash_address] = [[key, value]]
            
	def read(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    return
                return False
            else:
                return False
            
	def delete(self, key):
        hash_address = self.getAddress(key)
        
        if self.hash_table[hash_address] != 0:
            for a in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][a][0] == key:
                    self.hash_table[hash_address] = 0
				else:
                    del self.hash_table[hash_address][a]
				return
			return False
        else:
            return False

#Test Code
h_table = OpenHash(8)

h_table.save('aa', '1111')
h_table.read('aa')

data1 = 'aa'
data2 = 'ad'

print(ord(data1[0]))
print(ord(data2[0]))

h_table.save('ad,'2222)
print(h_table.hash_table)

h_table.read('aa')
h_table.read('ab')

h_table.delete('aa')
print(h_table.hash_table)
print(h_table.delete('Data'))
h_table.delete('ad')
print(h_table.hash_table)
```

출력

```
97
97
[0, [['aa', '1111'], ['ad', '2222']], 0, 0, 0, 0, 0, 0]
[0, [['ad', '2222']], 0, 0, 0, 0, 0, 0]
False
[0, 0, 0, 0, 0, 0, 0, 0]
```

## Python - 클로즈 해싱(Close hashing) / Open Addressing

클로즈 해싱은 해시 테이블의 충돌 문제를 해결하는 방법 중 하나로 Linear Probing, Open Addressing이라고 부르기도 한다.

구조는 간단하다. 위 이미지에서 Johs Smith와 Sandra Dee의 해시는 똑같이 873이다. 이때 먼저 들어온 John이 873이라는 해시를 먼저 키 값으로 취했고, 다음으로 들어온 Sandra는 바로 다음 값인 874를 키 값으로 가진다. 해시 중복이 발생하면 해당 해시 값부터 순차적으로 빈 공간을 찾기 시작한다. 가장 처음 찾는 빈 공간에 키와 밸류를 저장한다.

저장 효율을 높이는 방법이다.

```
# close hashing
class CloseHash:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
    
    def getKey(self, data):
        self.key = ord(data[0])
        return self.key

    def hashFunction(self, key):
        return key % self.size
    
    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    def save(self, key, value):
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] != 0:
            for a in range(hash_address, len(self.hash_table)):
                if self.hash_table[a] == 0:
                    self.hash_table[a] = [key, value]
                    return
                elif self.hash_table[a][1] ==key:
                    self.hash_table[a] =value
                    return
            return None
        else:
            self.hash_table[hash_address] = [key, value]
    
    def read(self, key):
        hash_address =self.getAddress(key)

        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a][0] == key:
                return self.hash_table[a][1]
        return None

    def delete(self, key):
        hash_address = self.getAddress(key)

        for a in range(hash_address, len(self.hash_table)):
            if self.hash_table[a] == 0:
                continue
            if self.hash_table[a][0] ==key:
                self.hash_table[a] = 0
                return
        return False

# Test Code
h_table = CloseHash(8)

data1 = "aa"
data2 = "ad"
print(ord(data1[0]),ord(data2[0]))

h_table.save('aa', '3333')
h_table.save('ad', '9999')
print(h_table.hash_table)

h_table.read("ad")

h_table.delete('aa')
print(h_table.hash_table)

h_table.delete("ad")
print(h_table.hash_table)
```

출력

```
97 97
[0, ['aa', '3333'], ['ad', '9999'], 0, 0, 0, 0, 0]
[0, 0, ['ad', '9999'], 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
```

