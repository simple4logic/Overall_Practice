-- 처음 'testset'이라는 이름의 database 생성
CREATE DATABASE testset;

-- testset이라는 database를 사용할 것임을 명시 (scope를 제한)
use testset;

-- 해당 database안에서 쓸 table을 새로 정의
-- 'persontable'이라는 명칭의 table을 생성하며 (column name, 받는 타입) 형태로 테이블을 구성한다 
CREATE table persontable(
    name VARCHAR(50),
    level VARCHAR(1),
    phone VARCHAR(15),
    address VARCHAR(100)
);

-- table이 어떻게 구성되어있는지 표시
desc persontable;

-- 위에서 구성한 테이블을 실제로 가져옴
SELECT CONCAT(name,'의 레벨은 ',level,'입니다.') from persontable
WHERE name = "박나래";
-- table에 원소를 넣어줌
INSERT INTO testset.persontable (name, level, phone, address) VALUES ('홍길동', "A", '01023456789', '조선 한양읍');
INSERT INTO testset.persontable (name, level, phone, address) VALUES ('손흥민', "A", '0112345434', '영국 런던');
INSERT INTO testset.persontable (name, level, phone, address) VALUES ('박찬호', "B", '01023433456', '충남 공주');
INSERT INTO testset.persontable (name, level, phone, address) VALUES ('김유신', "C", '0187766645', '신라 경주');
INSERT INTO testset.persontable (name, level, phone, address) VALUES ('박나래', "C", '0192929384', '서울특별시 영등포구');
INSERT INTO testset.persontable (name, level, phone, address) VALUES ('강감찬', "B", '01023432123', '고려');

-- 해당 table을 삭제
drop table persontable;

-- 해당 database를 삭제
drop DATABASE testset;