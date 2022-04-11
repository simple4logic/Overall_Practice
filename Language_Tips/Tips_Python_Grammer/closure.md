# 클로저(closure)

## 개념
데코레이터는 함수의 앞과 뒤에서 실행되는 기능을 추가적으로 구현하고 싶을 때 사용한다.


## 형식
```py
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환, 소괄호 () 사용 금지.
 
c = calc()
print(c(1), c(2), c(3), c(4), c(5))

'''
return :
8 11 14 17 20
'''
```

위 코드가 어떻게 동작하는지 살펴보자.

ref
> https://dojang.io/mod/page/view.php?id=2366
> https://dojang.io/mod/page/view.php?id=2368