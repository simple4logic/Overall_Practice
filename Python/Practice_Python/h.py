a, b = input().split()
a=int(a)
b=int(b)

hint = [False,False] + [True]*(b-1)

for i in range(2,b+1):
    if hint[i]:
        for j in range(i*i, b+1, i):
            hint[j] = False

for k in range(2,a):
    hint[k]=False

for l in range(2,b+1):
    if hint[l]:
        print(l, end='\n')