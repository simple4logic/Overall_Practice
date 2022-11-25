import collections

dic = collections.defaultdict(list)

for a, b in [[1, 'a'], [2, 'b'], [1, 'c'], [1, 'd']]:
    dic[a].append(b)

##충격 기괴 공포 !! for에 쓰인 임시 변수들은 아래서도 쓰일 수 있다............

# print(dic)

# dic[1].remove('d')
# dic[1].remove('c')
# dic[1].remove('a')
# dic[2].remove('b')

# print((dic.values()))

# if len(dic) == 0:
#     print("it's empty")


a = [1, 2, 3, 4, 5]

for N in a:
    print("this is ",N)
    a.remove(N)
    a.insert(0, N)
    print(a)