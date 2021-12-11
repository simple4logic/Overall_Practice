# 연결 리스트(Linked-List)에 대해서

![image](https://user-images.githubusercontent.com/68508521/145591784-7b2a39f7-f685-4197-829e-cc0e1a975a3d.png)

## 개념

연결 리스트는 데이터와 다음 노드의 주소(포인터)를 담고 있는 노드들이 한 줄로 연결되어 있는 형태의 자료 구조이다. 연결 리스트의 형태에 따라서 노드의 포인터가 다음이나 이전 노드를 가르키기도 한다.

## 연결 리스트의 장단점
### 장점

1. 일반적인 List와는 다르게 길이가 가변적이다. node를 삽입, 삭제하는 방식을 통해 길이를 동적으로 조절 가능하다.
2. 노드의 삽입, 삭제가 쉽다(=데이터의 삽입, 삭제가 쉽다). 즉 항상 일정한 시간을 소요(=O(1))한다.

### 단점

1. 임의의 노드에 바로 접근할 수 없다. 일일히 거슬러 올라가야만 한다.
2. 다음 노드의 주소를 저장하기 위한 추가적인 공간이 필요하다.
3. 연결 리스트를 거꾸로 탐색하기가 아주 어렵다.
4. **Cache Locality를 활용해 근접 데이터를 사전에 캐시에 저장하기가 어렵다. 

**Cache locality : 대부분의 프로그램은 한 번 사용한 데이터를 다시 사용할 가능성이 높고, 그 주변의 데이터도 곧 사용할 가능성이 높은 데이터 지역성을 가지고 있다. 데이터 지역성을 활용하여 메인 메모리에  있는 캐시 메모리에 불러와 두고, CPU가 필요한 데이터를 캐시에서 먼저 찾도록 하면 시스템 성능을 향상시킬 수 있다.

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

### 기본적인 기능(Append, Print)

```py
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    #헤더부터 탐색해 맨 뒤에 새로운 노드 추가
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

### 노드의 인덱스 구하기
```py
#class LinkedList:
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node
```

### 삽입
```py
#class LinkedList:
    def add_node(self, index, value):
        new_node = Node(value)

        #맨 앞에 노드를 삽입하는 경우
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
            #new_node를 앞에 넣기 위해서는 넣기 전에 
            #new_node.next가 기존 head를 가르키게 해야한다. 
            #그 후 head에 new_node 그대로 넣으면 된다.

        #중간에 삽입하는 경우    
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
```

### 삭제
```py
#class LinkedList:
   def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next
```

## 참고사항
NodeX 객체 그 자체는 array와 마찬가지로 주소값이다.
```py
NodeX = NodeX.next #to the next node
```
따라서 위의 코드처럼 node에 다음 node의 '주소'를 할당하는 방식을 통해 다음 노드로 넘어갈 수 있다. 이때 헷갈리지 말아야 할 점은 NodeX의 element 중 .next에 주소를 할당한 것이 아니라, NodeX 자체에 NodeX.next를 할당했다는 것이다. 즉 NodeX의 value 값도 달라진다.

예를 들어보자.
```py
#making Linked List : 1 -> 2 -> 3 -> 4  
lkdlist = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
lkdlist.next = node1
node1.next = node2
node2.next = node3

print(lkdlist)
>>> 1
lkdlist = lkdlist.next #(=node1)
print(lkdlist)
>>> 2
```
`lkdlist = lkdlist.next`이 문장은 다음 노드로 완전히 넘어가는 것이며, 주소만 바꿔주는 것이 아니다. 노드==주소 이라는 것을 잊으면 안된다.

## Reference
> https://velog.io/@woga1999/파이썬으로-구현하는-링크드-리스트
> https://daimhada.tistory.com/72
