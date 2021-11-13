prime = []

#Functions that put prime numbers under or same N to the list "prime"
#U need to check useless repeatance by checking max input.
def primegen(a: int, b: int): #a input, b is before max.
    global prime
    start: int = 2 #check whether it is prime or not from number 2(=variable named start)
    
    if a > b:
        print("new prime is now generating!\n")
        start = b #start point is previous max num.

    hint = [False,False] + [True]*(a-1)

    for i in range(start,a+1):
        if hint[i]:
            for j in range(i*i, a+1, i):
                hint[j] = False

    for l in range(start,a+1):
        if hint[l]:
            prime.append(l)

#this function print answers by using generated list & input.
'''
in order to prevent timeout, we need to modify the part "in".
for A in B function is very comfortable, but this function searches all of the list.
Therefore it's very time consuming. Let's implement the concept "LIS(Longest Increasing Subsequnce)"
'''
def makeAns(x: int): #x is input num
    global prime
    AnsI: int = 0
    for i in prime[len(prime)//2:]: #starting from center is time-efficient method. in this, i is bigger than x
        if i <= x-i:
            #print(f"this is i: {i}\n")
            if x-i in prime[len(prime)//2:]:
                    AnsI=i
        else :
            break
    print(f"{AnsI} {x-AnsI}\n")
    return  
                
# 1 2 3 4 5

n=int(input()) #n = how many times to repeat
max: int =0
for i in range(n): #n th repeat
    A = int(input())

    if A > max: #when input is bigger than before.
        primegen(A, max)
        makeAns(A)
        max = A
        print(f"now max is : {max}\n")
        print(prime, end='\n')
    
    else: #when new input is smaller than before
        makeAns(A)
        print(prime, end='\n')
