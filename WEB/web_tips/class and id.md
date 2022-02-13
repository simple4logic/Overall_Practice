# Class와 id

## 사용

```html
<!--class-->
<div class = 'item'> "contenets" </div>

<!--id-->
<div id = 'item'> "contenets" </div>
```

class와 id 모두 html의 content의 uniqueness를 부여하기 위해 사용한다. 위의 코드처럼 태그 안에 인자? 로서 들어간다. 

여기서 차이점은 id는 유일하나 class는 유일하지 않을 수 있다는 것이다. 내가 만약 모든 제목들에 대해서 bold 성분을 주고 싶고, 모든 단락들에 대해서 italic 성분을 주고 싶다면 

```html
<div class = 'title'> 제목입니다 </div>

.title {
    font-weight: bold;
}

<div class = 'content'> 내용입니다 </div>

.content {
    font-style: italic;
}
```

이런 방식으로 코드를 짜면 모든 title class가 부여된 내용들에 대해 전부 bold를 줄 수 있고, 모든 content class가 부여된 내뇽들에 대해서는 전부 italic을 줄 수 있다.

class는 중복으로도 적용 가능하다. 위의 코드와 같은 상황에서 볼드와 이탤릭을 모두 부여하고 싶다면

```html

```

