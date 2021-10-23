prime = set()

#Functions that put prime numbers under or same N to the list "prime"
#U need to check useless repeatance by checking max input.
def primegen(a: int):
    global max, prime
    start: int = 2 #check whether it is prime or not from number 2(=variable named start)

    if a < max:
        return #already generated, so escape.
    
    if a > max:
        start = max #start point is previous max num.

    hint = [False,False] + [True]*(a-1)

    for i in range(start,a+1):
        if hint[i]:
            for j in range(i*i, a+1, i):
                hint[j] = False

    for l in range(start,a+1):
        if hint[l]:
            prime.add(l)

#this function print answers by using generated list & input.
'''
in order to prevent timeout, we need to modify the part "in".
for A in B function is very comfortable, but this function searches all of the list.
Therefore it's very time consuming. Let's implement the concept "LIS(Longest Increasing Subsequnce)"
'''
def makeAns(x: int): #x is input num
    global prime
    AnsI: int = 0 # init of variable is mandatory.
    for i in prime:
        if i <= x-i:
            if x-i in prime:
                    AnsI=i
        else :
            break
    print(f"{AnsI} {x-AnsI}\n")
    return  
                
# 1 2 3 4 5

n=int(input()) #n = how many times to repeat

for i in range(n): #n th repeat
    max = 0
    A = int(input())
   
    if max < A:
        max = A #max init to prevent useless primegen loop.

    primegen(A) #generated list of prime numbers.
    makeAns(A)