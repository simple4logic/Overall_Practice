# Vector Container에 대해서
___

## 개념
vector container는 메모리가 자동으로 할당되는 배열이다. STL(standard template library)의 일종인데 STL이 무엇인지는 나중에 다뤄보도록 하겠다. Linked List처럼 맨 뒤쪽에 자료를 삽입하거나 삭제할 수 있는 구조이다.  
그러나 배열 기반인만큼 삽입과 삭제가 빈번하게 일어난다면 비효율적이라고 한다. 

## 사용 방법  
사용하기 위해서는 먼저 <vector> 헤더파일을 추가해야 한다.  
벡터를 만들 때 형식은 "vector<자료형> 변수명"이다. 다른 예시들을 보자.

vector<int> v;
- 비어있는 vector v를 생성합니다.

vector<int> v(5);
- 기본값(0)으로 초기화 된 5개의 원소를 가지는 vector v를 생성합니다.

vector<int> v(5, 2);
- 2로 초기화된 5개의 원소를 가지는 vector v를 생성합니다.

vector<int> v2(v1);
- v2는 v1 vector를 복사해서 생성됩니다.


https://blockdmask.tistory.com/70 참고해서 마저 작성