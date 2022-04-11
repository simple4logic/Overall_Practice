# 참고 프로젝트
> https://github.com/16Yongjin/hufs-drop-ranking-react/tree/main/src

## 

일단 최소한의 기능 구현

1. 강의명
2. 교수
3. 현재인원
을 학교 사이트로부터 가져와서 실시

학사 강의 대상으로 검색 실시.

```html
<div class="course-info-item">
    <div class="left">
        <label class="cc-check-item round full">
            
            <input type="radio" name="check" value="0" 

            여기에 있는 value = "0" 에 따라서 sorting 된것 같음.

            이 value 순으로 가져오면 될듯?!
```
** 주의. 다음 페이지로 넘어가기 전에 그 페이지에서만 !!! value 0부터 9까지 (한 페이지당 10개씩 노출)


**이 부분은 로그인 후 검색버튼을 눌렀을 때 뜨는 강의 목록에서 어떤 식으로 sorting 되어있는 지를 찾은 것이다.

일단 웹드라이버를 깔아서 셀레니움으로 x_path를 구해서 검색 버튼을 눌렀을 때의 html을 가져오는 방식을 생각하고 있다.

관련 참고 게시글들(저번에 띄워놨던 탭들)

> https://library.gabia.com/contents/9239/

> https://webnautes.tistory.com/779

> https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html

> https://rubber-tree.tistory.com/88


<!-- ******************************************참고************************************************  -->

> https://m.blog.naver.com/draco6/221664143794

이 페이지에서 말하는 바는 다음과 같다.

셀레니움은 사람 한명이 일일히 페이지에 들어가서 긁어오는 방식이랑 완전히 동일하다.

따라서 이 방식을 훨씬 더 빠르게 자동화 하기 위해서는 selenium이 아닌 requests 방식을 써야 한다.

이 방식은 selenium으로 정보를 가져와서, 그 쿠키를 request에 복사시켜서 로그인 이후에는 request로 훨씬 빠르게 데이터를 가져오는 방식을
취하자는 것이다.

일단 셀레니움으로 일일히 구현해보고, 나중에 빠른 속도가 필요하면 이를 가속화하는 방식을 꼭 도전해보자.