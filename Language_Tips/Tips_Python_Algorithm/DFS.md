DFS(Depth-First-Search)
===

이전에 그래프 탐색 게시글에서 DFS의 개념과 수도코드, 그리고 각종 특징들을 설명한 적이 있다. 이번에는 실제 파이썬 코드로는 어떻게 구현되는지와 그 코드를 풀이하여 설명해보겠다.

# 재귀 구조 풀이
DFS는 기본적으로 스택을 이용하여 구현하는 것이 일반적이나, 재귀적 풀이를 이용하여 더 쉽고 간단하게 구현할 수 있다. 먼저 수도코드를 보자.

## __DFS Pseudo code with recursion__
```md
DFS(G, v)
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
```

이를 실제 파이썬 코드로 구현하면 다음과 같다.

## __DFS python code with recursion__
```py
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered
```

test-run에 쓰이는 그래프는 다음과 같다.

![image](https://user-images.githubusercontent.com/68508521/165530529-c84258db-4e79-470e-87cc-d330de890c54.png)


이를 python dictionary처럼 표현해서 함수로 다룰 수 있도록 변형해보자. 각 노드를 key로, 그 노드(key)에서 향할 수 있는 다음 노드들을 value로 정한다면 다음처럼 표현할 수 있을 것이다.

```py
graph={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}
```

이제 이 딕셔너리 자료형을 인풋으로 받아서 위의 파이썬 코드를 test-run 해보자.

```py
ans = recursive_dfs(1) #시작 vertex = 1
print(ans)
>>> [1,2,5,6,7,3,4]
```

결과를 보면 그래프 위의 모든 점을 성공적으로 읽었음을 확인할 수 있다. 이제 올바르게 동작한다는 것을 확인했으니, 함수를 하나하나 나누어 분석해보자.

## 분석
```py
#전체코드
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered
```

먼저 매개변수부터 확인하자. v는 정점(vertex)으로, 처음 순회를 시작하는 시작점을 뜻한다. discovered라는 리스트는 따로 입력하지 않으면 알아서 빈 리스트를 디폴트로 인수로 가진다. 따로 입력받은 경우에는 그것을 그대로 가져다 쓸 것이다.  

그 다음을 보자. 해당 vertex는 지금 방문해서 읽고 있기 때문에 append로  discovered 리스트에 먼저 추가해준다.  

이제 for문을 보자. for문을 통해 해당 그래프에서 노드 하나에 연결된 다른 노드들을 모두 확인하고 있다. vertex 1을 예시로 보자. 1과 연결된 vertex는 2, 3, 4이다. 따라서 w는 처음에는 2로 시작한다. 이때 2는 discovered 리스트에 들어가 있지 않기 때문에, 2를 현재 노드로 인수로 넣고 이미 1이 들어가있는 discovered 리스트를 인수로 넣어준다. 이렇게 되면 노드 1에서 노드2로 진출한 상태에서 다시 처음 과정을 반복하게 된다.  

이런 방식으로 진행되면 각 노드에 연결된 첫 자식 노드의 끝까지 파고들고, 노드의 끝을 만나면 바로 그 노드의 부모 노드의 다음 번 자식 노드를 탐색하게 된다. 재귀의 특성 때문이다. 이런 이유로 DFS는 일단 "끝"을 볼 때까지 자식 노드를 탐색하게 된다. 그래서 첫 노드(root-node)의 다른 자식 노드를 탐색하기까지는 한참 걸린다. 


# 스택 구조 풀이

## __DFS Pseudo code with stack__
```md
DFS_iterative(G, v)
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)
```

이를 실제 파이썬 코드로 구현하면 다음과 같다.

## __DFS python code with stack__
```py
def iterative_dfs(start_v):
    discovered = []
    stack = []
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
    