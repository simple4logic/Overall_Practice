a, b = input().split()
a=int(a)
b=int(b)

hint = [False,False] + [True]*(b-1)
Ansarr=[]

for i in range(2,b+1):
    if hint[i]:
        #Ansarr.append(i)
        for j in range(i*i, b+1, i):
            hint[j] = False

for k in range(2,a):
    hint[k]=False

for l in range(2,b+1):
    if hint[l]:
        Ansarr.append(l)

for A in Ansarr:
    print(A, end='\n')