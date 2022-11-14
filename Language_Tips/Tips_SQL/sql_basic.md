# SQL 기초 문법

너무 기초적인 SELECT, FROM 같은 것은 생략하고 헷갈릴 수 있는 내용 위주로 다루겠다.

## 1. WHERE
data를 "어디에서" 가져올지를 정하는 문법이다. 데이터베이스의 형태는 일반적으로 table형태로 되어있는데, 
해당 table에서 특정 column만을 가져오고 싶을때 쓸 수 있다. 참고로, column은 vertical하고 row는 horizontal하다. 

Dataset
|id|type|category|content|
|:---:|:---:|:---:|:---:|
|1|number|date|2019-10-11|
|2|number|integer|34|
|3|text|name|Hyun|
|4|text|food|chocolate| 
|5|text|food|white chocolate| 
|5|text|food|apple| 

예를 들어 이런 식의 table이 있다고 하자.

이 table에서 type이 number로 되어있는 자료만을 가져오고 싶다면

```sql
--데이터 전체 선택
SELECT *
--데이터 파일 이름
FROM dataset
-- text, date의 경우 quote 해줘야함
WHERE type = "number";
```
이렇게 작성하면 된다.

## 2. LIKE
정확히 특정 문자열이 있는지 없는지는 NOT과 '='를 이용해서 판별하면 되지만, 특정 문자열을 "포함"하는 다른 문자열이 있는지 넓게 찾기 위해서는 LIKE이 필요하다. 위 table에서 "chocolate"이 들어간 모든 자료를 가져오려면 다음과 같이 작성한다.

```sql
WHERE content LIKE "%chocolate%";
```
여기서 %는 wildcard이며, 앞에만 붙이면 "~ chocolate", 뒤에만 붙이면 "chocolate ~", 둘 다 붙이면 "~ chocolate ~" 를 찾아준다.

다른 종류의 wildcard는 아래를 참고하자.
```sql
--A로 시작하는 문자를 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A%'

--A로 끝나는 문자 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A'

--A를 포함하는 문자 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A%'

--A로 시작하는 두글자 문자 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A_'

--첫번째 문자가 'A''가 아닌 모든 문자열 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE'[^A]'

--첫번째 문자가 'A'또는'B'또는'C'인 문자열 찾기--
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '[ABC]'
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '[A-C]'
```


## 3. NULL
데이터가 NULL 인지 아닌지 판별하는건 "="를 이용해서는 불가능하다. 다음 두 가지 문법을 이용하자.

```sql
Type is NULL
Type is NOT NULL
-- Type = NULL 은 불가능
```