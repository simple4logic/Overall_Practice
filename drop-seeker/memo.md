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

**이 부분은 로그인 후 검색버튼을 눌렀을 때 뜨는 강의 목록에서 어떤 식으로 sorting 되어있는 지를 찾은 것이다.

일단 웹드라이버를 깔아서 셀레니움으로 x_path를 구해서 검색 버튼을 눌렀을 때의 html을 가져오는 방식을 생각하고 있다.

관련 참고 게시글들(저번에 띄워놨던 탭들)

> https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chltmddus23&logNo=221793411051

> https://library.gabia.com/contents/9239/

> https://webnautes.tistory.com/779

> https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html

> https://rubber-tree.tistory.com/88


