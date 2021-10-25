prime = set()

#Functions that put prime numbers under or same N to the list "prime"
#U need to check useless repeatance by checking max input.
def primegen(a: int):
    global prime
    start: int = 2 #check whether it is prime or not from number 2(=variable named start)

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
    Ans = {}

    for i in prime: #since there is no order in set function.
        if x-i in prime:
                if i < x-i:
                    Ans[(x-i)-i]=[i, x-i] #sort the calculated result
                else:
                    Ans[i-(x-i)]=[x-i, i]
    
    keylist=list(Ans.keys())
    print(Ans[min(keylist)][0], Ans[min(keylist)][1])
     

n=int(input()) #n = how many times to repeat

for i in range(n): #n th repeat

    A = int(input())

    primegen(A) #generated list of prime numbers.
    makeAns(A)