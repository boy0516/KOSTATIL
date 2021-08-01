## C++ 네임스페이스

출처: https://boycoding.tistory.com/171

# 네임스페이스, std (namespace)

이름 충돌은 두 개 이상의 식별자가 같은 스코프에 있는 경우 컴파일러가 어느 식별자를 사용해야 하는지 명확하게 알 수 없을 때 일어난다. 이렇게 되면 컴파일러나 링커가 모호함을 해결하기에 충분한 정보가 없으므로 오류를 발생시킨다. 프로그램이 점점 더 커지면 식별자의 수가 증가하므로 이름 충돌이 일어날 확률이 증가한다.

이름 충돌의 예를 살펴보자. 다음 예제 foo.h 와 goo.h는 이름과 매개 변수가 같은 함수를 포함하는 헤더 파일이다.

###### foo.h:

```cpp
// This doSomething() adds the value of its parameters
int doSomething(int x, int y)
{
    return x + y;
}
```

###### goo.h:

```cpp
// This doSomething() subtracts the value of its parameters
int doSomething(int x, int y)
{
    return x - y;
}
```

###### main.cpp:

```cpp
#include <iostream>
#include "foo.h"
#include "goo.h"

int main()
{
    std::cout << doSomething(4, 3); // which doSomething will we get?
    return 0;
}
```

foo.h 파일과 goo.h 파일이 따로 컴파일되면 위 프로그램은 문제없이 컴파일된다. 그러나 예제처럼 같은 프로그램에 이 둘을 같이 포함하면 이름과 매개 변수가 같은 함수가 같은 스코프에 있음으로써 이름 충돌이 발생한다. 따라서 컴파일러가 다음과 같은 오류를 발생시킨다.

```
c:\VCProjects\goo.h(4) : error C2084: function 'int __cdecl doSomething(int,int)' already has a body
```

이런 이름 충돌 문제를 해결하기 위해 **네임스페이스 (namespace)** 개념이 도입되었다.

------

## 네임스페이스가 뭔가요? (What is a namespace?)

**네임스페이스는 모든 식별자(변수, 함수, 형식 등의 이름)가 고유하도록 보장하는 코드 영역을 정의한다.**

기본적으로 전역 변수와 일반 함수는 전역 네임스페이스에서 정의된다. 예를 들어, 다음 코드를 살펴보자.

```cpp
int g_x = 5;

int foo(int x)
{
    return -x;
}
```

전역 변수 `g_x`와 함수 `foo()`는 모두 전역 네임스페이스에서 정의된다.

첫 번째 예제의 경우, main() 함수에서 doSomething() 함수를 호출했을 때 foo.h와 goo.h 헤더 파일 각각에서 doSomething() 함수가 전역 네임스페이스에서 정의되어 있으므로 이름 충돌이 발생했다.

두 개 이상의 독립된 코드가 함께 사용될 때 서로 이름이 충돌하는 문제를 방지하기 위해 C++ 에서는 namespace 키워드를 통해 자체 네임스페이스를 선언할 수 있다.

사용자 정의 네임 스페이스 내부에 선언된 모든 것은 전역 네임 스페이스가 아니라 해당 네임 스페이스에 속하게 된다.

###### 첫 번째 예제에 `namespace` 키워드를 사용해서 다시 작성해보자.

###### foo.h:

```cpp
namespace Foo
{
    // This doSomething() belongs to namespace Foo
    int doSomething(int x, int y)
    {
        return x + y;
    }
}
```

###### goo.h:

```cpp
namespace Goo
{
    // This doSomething() belongs to namespace Goo
    int doSomething(int x, int y)
    {
        return x - y;
    }
}
```

이제 foo.h 헤더파일의 "Foo 네임스페이스" 안에 `doSomething()` 함수가 있고, goo.h 헤더 파일의 "Goo 네임스페이스" 안에 `doSomething()` 함수가 있다.

###### main.cpp:

```cpp
int main()
{
    std::cout << doSomething(4, 3); // which doSomething will we get?
    return 0;
}
C:\VCProjects\Test.cpp(15) : error C2065: 'doSomething' : undeclared identifier
```

무슨 일이 일어났는가 하면, 컴파일러는 전역 네임스페이스를 검색해서 `doSomething` 함수에 대한 정의를 찾기 시작했다. 그러나 더는 전역 네임스페이스에는 `doSomething()` 함수가 없으므로 정의를 찾지 못했다!

컴파일러에 사용할 `doSomething()` 함수의 버전을 알려주는 방법은 **스코프 분석 연산자(`::`)**를 통한 방법과 **`using` 명령문**을 사용하는 방법 두 가지가 있다.

------

## 스코프 분석 연산자(::) (scope resolution operator (::))

컴파일러가 특정 네임스페이스에서 식별자를 찾게 하는 첫 번째 방법은 스코프 분석 연산자(`::`)를 사용하는 것이다. 이 연산자를 사용하라면 식별자 이름 앞에 사용할 네임스페이스를 붙이면 된다.

다음은 `::` 연산자를 사용해서 컴파일러에 명시적으로 "Foo 네임스페이스"에 있는 doSomthing() 함수를 사용할것 이라고 알려주는 예제다.

```cpp
int main(void)
{
    std::cout << Foo::doSomething(4, 3);
    return 0;
}

// 7
```

###### "Goo 네임스페이스"에 있는 `doSomething()` 함수 버전을 대신 사용하려면 :

```cpp
int main(void)
{
    std::cout << Goo::doSomething(4, 3);
    return 0;
}

// 1
```

스코프 분석 연산자(`::`)는 검색하려는 네임 스페이스를 구체적으로 선택할 수 있도록 해 주므로 매우 유용하다. 아래와 같은 작업도 수행할 수 있다.

```cpp
int main(void)
{
    std::cout << Foo::doSomething(4, 3) << '\n';
    std::cout << Goo::doSomething(4, 3) << '\n';
    return 0;
}

// 7
// 1
```

또한, 네임스페이스 없이 `::` 연산자를 사용할 수도 있다. (Ex. `::doSomething()`) 이 경우 전역 네임스페이스를 나타낸다.

------

## 중첩된 네임스페이스 (Nested namespaces)

네임스페이스는 다른 네임스페이스 안에 중첩될 수 있다.

###### 예:

```cpp
#include <iostream>

namespace Foo
{
    namespace Goo // Goo is a namespace inside the Foo namespace
    {
        const int g_x = 5;
    }
}

int main()
{
    std::cout << Foo::Goo::g_x;
    return 0;
}
```

네임스페이스 "Goo"는 네임스페이스 "Foo"내부에 있으므로 `Foo:Goo:g_x`로 접근한다.

C++17에서 중첩된 네임스페이스를 다음과 같이 선언할 수도 있다.

```cpp
#include <iostream>

namespace Foo::Goo // Goo is a namespace inside the Foo namespace (C++17 style)
{
    const int g_x = 5;
}

int main()
{
    std::cout << Foo::Goo::g_x;
    return 0;
}
```

중첩된 네임스페이스 내의 변수 또는 함수의 정규화된 이름을 입력하는 것은 매우 길기 때문에 C++에서 **"네임스페이스 별칭"**을 만들 수 있다.

```cpp
namespace Foo
{
    namespace Goo
    {
        const int g_x = 5;
    }
}

namespace Boo = Foo::Goo; // Boo now refers to Foo::Goo

int main()
{
    std::cout << Boo::g_x; // This is really Foo::Goo::g_x
    return 0;
}
```

네임스페이스는 이름 충돌을 방지하기 위한 메커니즘으로 설계되었다. 이를 증명하기 위해 모든 표준 템플릿 라이브러리는 단일 네임스페이스 `std::` 아래에 있다.

------

## std

원래 C++을 설계할 때는 C++ 표준 라이브러리(Ex. cin, cout)의 모든 식별자를 직접 사용할 수 있었다. 이는 곧 사용자의 식별자 이름과 충돌을 의미한다. 또 표준 라이브러리에 도입된 새로운 기능이 충돌할 수 있으므로 한 버전의 C++에서 컴파일될 프로그램이 향후 버전의 C++에서 컴파일되지 않을 수 있다. 그래서 **C++은 표준 라이브러리의 모든 기능을 `std namespace`라는 특별한 영역으로 옮겼다.**

```cpp
std::cout << "Hello world!";
```

`std::cout`에서 실제로 함수 이름은 `cout` 이고, 이 함수가 정의된 네임스페이스 이름이 `std` 다. C++ 표준 라이브러리의 모든 기능은 `std`라는 `namespace` 안에 있다. `std`는 "**standard(표준)**"의 약자다. 이런 방식으로 표준 라이브러리의 기능이 사용자가 만든 식별자와 이름 충돌할 걱정이 없다.



