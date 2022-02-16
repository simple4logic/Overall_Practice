# 화살표 함수

## 사용

```js
let func = (arg1, arg2, ...argN) => expression
```

위와 같은 표현형을 화살표 함수(arrow function)이라 부른다. 위의 형태는 아래의 코드와 완전히 동일한 기능을 한다.

```js
let func = function(arg1, arg2, ...argN) {
  return expression;
};
```

화살표 함수는 파이썬에서의 lambda와 비슷한 용법이다. 기존의 함수 선언보다 훨씬 단순하게 함수를 생성할 수 있다. 다른 예시를 통해 위 함수의 동작을 알아보자.

## 예시

```js
let sum = (a, b) => a + b;

/* the code above is same as

let sum = function(a, b) {
  return a + b;
};

*/

alert( sum(1, 2) ); // return 3
```

## 참고사항

1. 인수가 없는 경우에는 소괄호 안을 아예 비워놓으면 된다.

```js
let sayHi = () => alert("안녕하세요!");

sayHi();
```

2. 화살표 함수 뒤의 코드가 한줄 이상이라면 중괄호와 return을 써주어야 한다.

```js
let sum = (a, b) => {
  let result = a + b;
  return result;
};
```
중괄호를 사용한 경우에는 반드시 return 을 이용해주어야 한다.

## 추가 자료
여기서는 화살표 함수의 기본적인 문법에 대해 다루었다. 화살표 함수의 심화된 특징에 대해서는 차후에 다른 글에서 다루겠다. 

심화 설명 자료 
> https://ko.javascript.info/arrow-functions#ref-1741


