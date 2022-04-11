# Asterisk(*)에 대하여

*Reference - Python Algorithm Interview Q31 sol #2

## 역할
Asterisk의 역할은 C에서의 포인터 변수 역할을 했던 것과는 완전히 다르다. 바로 unpacking 이다.  

제대로 된 명칭은 시퀀스 언패킹 연산자(Sequence Unpacking Operator)로, 시퀀스를 풀어헤치는 연산자를 뜻한다. 즉 튜플이나 리스트와 같은 시퀀스를 언팩한다.

## 예시

```py
>>> fruit = ['lemon', 'apple', 'pear']
>>> fruits
['lemon', 'apple', 'pear']
```

위와 같은 fruit라는 리스트가 존재하는 상황에서, 각 요소의 값을 하나하나 출력하고 싶은 경우를 생각해보자.

```py
#첫번째 방법
print(fruit[0], ...)

#두번째 방법
for f in fruit:
    print(f, end=' ')
```
위의 방법보다 훨씬 깔끔한 방법은 *로 언패킹하는 것이다.

```py
>>> print(*fruit)
lemon apple pear
```

## 활용
asterisk를 이용해서 반대로 패킹(packing)을 할 수도 있다.  

다음의 함수를 보자.

```py
def func(*param):
    print(params)

>>> func('a', 'b', 'c')
('a', 'b', 'c')
```

위 함수는 분명 하나의 파라미터만을 받는 함수지만, 3개의 파라미터를 전달했음에도 불구하고 asterisk에 의해 "하나의 파라미터"로 패킹되어 처리된다. 몇 개의 파라미터를 넘기는 모두 처리된다. 책에서 언급해주었는데, 위의 형식은 파이썬 3에서 print함수의 기본 동작원리와 같다고 한다.

```py
>>> print('a', 'b')
a b

>>> print('a', 'b', 'c')
a b c
```

다른 활용을 보자.

```py
>>> a, *b = [1,2,3,4]
>>> a
1
>>> b
[2,3,4]

>>> *a, b =[1,2,3,4]
>>> a
[1,2,3]
>>> b
4
```

변수 할당 시에 *로 묶어서 처리가 가능하다. 일반적인 케이스에서는 변수는 값을 하나만 취하나 *로 처리하는 경우는 "나머지" 모든 값을 취한다.  

*를 두 번 쓰는 경우도 있다. *를 한 번 쓰는 경우는 위에서 언급했던 경우인 __리스트__, __튜플__ 등의 시퀀스 언패킹이며 **를 두 번 쓰는 경우는 __키/값 페어__ 를 언패킹하는 경우이다.  

다음의 예를 보자.

```py
>>> date_info = {'year': '2020', 'month': '01', 'day': '13'}
>>> new_info = {*date_info}
>>> new_info
{'day', 'year', 'month'}

>>> new_info = {**date_info}
{'year': '2020', 'month': '01', 'day': '7'}

>>> new_info = {**date_info, 'day' : 14}
{'year': '2020', 'month': '01', 'day': '14'}
```

**를 이용해서 date_info 키/값 페어의 모든 요소를 언패킹할 수 있고, 심지어는 day의 값을 새로운 값으로 업데이트할 수도 있다.