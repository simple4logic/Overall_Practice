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
