# Prefix, Postfix에 대해서

## 개념
Prefix와 Postfix : 각각 전위연산자, 후위연산자이다. 
우리가 일반적으로 코드상에서 ++a라고 쓰는 것이 전위 연산자이고, a++라고 쓰는 것이 후위 연산자이다.

<script src="https://gist.github.com/simple4logic/2f28e04193bdb390cc79fb6a0db830fe.js"></script>

코드 실행결과

```
postfix
postfix
postfix
postfix
prefix
prefix
prefix
```

## 추가 내용  
일반적으로 루프문에서는 다 후위연산자를 쓴다. while(n--) - postfix로 하면 우리가 일반적으로 의도하는 n번만큼의 반복을 해주지만, while(--n) - prefix로 하면 n-1번만큼의 반복만 해서 의도와 달라지게 된다.