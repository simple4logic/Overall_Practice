# 데코레이터(Decorator)

## 개념
```py
# @(at) method
@decorator
def old_func():

# function-like method
new_func = decorator(old_func)
```
데코레이터는 장식시킬 함수의 앞과 뒤에서 코드를 실행하는 역할을 한다. 


## 필요성
```py
def print_A():
  print("my name is A")

def print_B():
  print("my name is B")

def print_C():
  print("my name is C")
```

이름 A, B, C를 소개하는 세 개의 함수가 있다고 하자. 이 세개의 함수를 실행하기 전에 "hello?", 이후에 "how are you?"를 출력하려고 한다. 

```py
def print_A():
  print("hello?")
  print("my name is A")
  print("how are you?")

def print_B():
  print("hello?")
  print("my name is B")
  print("how are you?")

def print_C():
  print("hello?")
  print("my name is C")
  print("how are you?")
```
이런식으로 만드는 것에는 한계가 있다, 함수의 수가 수 백개라면? 함수가 곳곳에 흩어져 있다면? 이런 경우를 편리하게 해결하기 위해서 데코레이터가 있다. 후에 설명하겠지만, 데코레이터를 적용하면 다음과 같이 정리할 수 있다.

```py
def hello_decorator(func):
  def wrapper():
    print("hello?")
    func()
    print("how are you?")
  return wrapper

@hello_decorator
def print_A():
  print("my name is A")

@hello_decorator
def print_B():
  print("my name is B")

@hello_decorator
def print_C():
  print("my name is C")
```

이렇게 하면 위의 토그돠 동일한 출력을 얻을 수 있다.

## 사용

데코레이터의 사용 방식에는 두 가지가 있다. 

### @(at) method

ㅊ추후 추가!!

> https://yeomko.tistory.com/12
> https://dojang.io/mod/page/view.php?id=2427
