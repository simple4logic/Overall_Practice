n=100
k=25
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    #primes.append(i)
    for j in range(i*i, n+1, i):
        a[j] = False

for x in range(2,k+1):
  a[x]=False
#print(a)

for k in range(2,n+1):
    if a[k]:
        primes.append(k)
print(primes)