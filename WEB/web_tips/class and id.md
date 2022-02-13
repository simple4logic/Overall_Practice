# Class와 id

## 사용

```html
<!--class-->
<div class = 'item'> "contenets" </div>

<!--id-->
<div id = 'item'> "contenets" </div>
```

class와 id 모두 html의 content의 uniqueness를 부여하기 위해 사용한다. 위의 코드처럼 태그 안에 인자? 로서 들어간다. 

## 차이점

사용 방식과 목적은 비슷하지만 한 가지 큰 차이점이 존재한다. 바로 id는 유일하나 class는 유일하지 않을 수 있다는 것이다. 내가 만약 모든 제목들에 대해서 bold 성분을 주고 싶고, 모든 단락들에 대해서 italic 성분을 주고 싶다면 

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
<div class = "title content"> 둘다 적용할 내용 </div>
```

이런식으로 중복해서 class를 적용할 수 있다. 여러 클래스를 적용하고 싶다면 띄어쓰기로 두 클래스를 구분하면 된다.

위에 언급했던 것처럼 id는 클래스와는 다르게 오직 하나의 element? 만 존재할 수 있기 때문에 중복 적용이 불가하다.

## CSS 적용 시 차이점

```html
<!-- html file -->
<div class = "class"> </div>

<div id = "id"> </div>
```

```css
/*css file*/
.class {
    color: black;
}

#id {
    color: blue;
}
```

위의 코드에서 쉽게 차이점을 발견할 수 있을 것이다. class의 경우에 css 파일에서 style을 부여할 때 "."과 함께 해당 class 명으로 시작한다.  

이와 반대로 id는 "#"과 함께 해당 id 명으로 시작한다.