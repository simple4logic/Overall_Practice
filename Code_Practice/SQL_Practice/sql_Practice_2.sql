-- 이걸로 database server랑 연결
-- Active: 1668412798092@@127.0.0.1@3306@testset2

create DATABASE testset2;

drop DATABASE testset2;

use testset2;

CREATE Table exam(
    name VARCHAR(50),
    math int(10),
    english int(10),
    korean int(10)
);

CREATE Table exam2(
    name VARCHAR(50),
    math int(10),
    english int(10),
    korean int(10)
);

INSERT INTO testset2.exam (name, math, english, korean) values ("황", 100, 100, 100);
INSERT INTO testset2.exam (name, math, english, korean) values ("김", 80, 74, 79);
INSERT INTO testset2.exam (name, math, english, korean) values ("정", 88, 70, 92);
INSERT INTO testset2.exam (name, math, english, korean) values ("최", 98, 100, 75);
INSERT INTO testset2.exam (name, math, english, korean) values ("곽", 90, 94, 99);

desc exam;


INSERT INTO testset2.exam2 (name, math, english, korean) values ("황", 100, 100, 100);
INSERT INTO testset2.exam2 (name, math, english, korean) values ("김", 80, 74, 79);
INSERT INTO testset2.exam2 (name, math, english, korean) values ("강", 83, 71, 94);
INSERT INTO testset2.exam2 (name, math, english, korean) values ("장", 100, 90, 72);
INSERT INTO testset2.exam2 (name, math, english, korean) values ("권", 98, 91, 92);

select * from exam