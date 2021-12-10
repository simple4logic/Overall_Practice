# 연결 리스트(Linked-List)에 대해서

![image](https://user-images.githubusercontent.com/68508521/145591784-7b2a39f7-f685-4197-829e-cc0e1a975a3d.png)

## 개념

연결 리스트는 데이터와 다음 노드의 주소(포인터)를 담고 있는 노드들이 한 줄로 연결되어 있는 형태의 자료 구조이다. 연결 리스트의 형태에 따라서 노드의 포인터가 다음이나 이전 노드를 가르키기도 한다.

## 연결 리스트의 장단점
### 장점

1. 일반적인 List와는 다르게 길이가 가변적이다. node를 삽입, 삭제하는 방식을 통해 길이를 동적으로 조절 가능하다.

2. 노드의 삽입, 삭제가 쉽다(=데이터의 삽입, 삭제가 쉽다).

### 단점

1. 임의의 노드에 바로 접근할 수 없다. 일일히 거슬러 올라가야만 함.
2. 다음 노드의 주소를 저장하기 위한 추가적인 공간이 필요하다.
3. 연결 리스트를 거꾸로 탐색하기가 아주 어렵다.

## 노드

연결 리스트의 기본적인 단위인 노드는 데이터와 다음(혹은 이전) 노드의 주소를 담고 있다. 구현은 다음과 같다.

```py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #아직 연결 전이라서 None이 디폴트 값
```

## 연결 리스트

위에서 구현한 노드들을 하나로 이어서 만든 선형 구조의 자료가 바로 연결 리스트이다. 노드를 중간 혹은 맨 앞, 뒤에 넣기 위한 기본적인 함수들을 구현해보자.

```py
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    #헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
	
    #모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
```

