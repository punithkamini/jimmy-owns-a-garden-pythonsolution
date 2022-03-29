l=[]
l1=[]
d=[]
d1=[]

def solution(A):
    for i in range(1,len(A)):
        if i==1:
            if A[i]<A[i-1]:
                l.extend([A[i-1],A[i]])
                d.extend([A[i-1],A[i]])
            elif A[i]>A[i-1] or A[i]==A[i-1]:
                l1.extend([A[i-1],A[i]])
                d1.extend([A[i-1], A[i]])
        else:
            if len(l)!=0:
                tp=0
                if (A[i]>d[-1] and d[-1]<d[-2]) or (A[i]<d[-1] and d[-1]>d[-2]):
                    l.append(A[i])
                    d.append(A[i])
                elif (A[i]>d[-1] and d[-1]>d[-2]) or (A[i]<d[-1] and d[-1]<d[-2]):
                    l.append(A[i])
                    if A[i] != tp and A[i] > d[-1] and A[i] > d[-2] and i == len(A) - 1:
                        d.append(A[i])
                        tp = A[i - 1]

            if len(l1)!=0:
                tp=0
                if (A[i]>d1[-1] and d1[-1]<d1[-2]) or (A[i]<d1[-1] and d1[-1]>d1[-2]):
                    l1.append(A[i])
                    d1.append(A[i])
                elif (A[i]>d1[-1] and d1[-1]>d1[-2]) or (A[i]<d1[-1] and d1[-1]<d1[-2]):
                    l1.append(A[i])
                    if A[i]!=tp and A[i]>d1[-1] and A[i] > d1[-2] and i==len(A)-1:
                        d1.append(A[i])
                        tp = A[i-1]

                elif (A[i] == d1[-1] and d1[-1] < d1[-2]) or (A[i] == d1[-1] and d1[-1] > d1[-2]) or (A[i] == d1[-1] and d1[-1] == d1[-2]):
                    d1.append(A[i])
                elif (A[i] > d1[-1] and d1[-1] == d1[-2]) or (A[i] < d1[-1] and d1[-1] == d1[-2]):
                    d1.append(A[i])
                    l1.append(A[i])
                    l1.pop(1)

    if len(d)>len(l):
        print(len(d)-len(l))
    elif len(d) < len(l):
        print(len(l)-len(d))
    elif len(d1)>len(l1):
        print(len(d1)-len(l1))
    elif len(d1)<len(l1):
        print(len(l1)-len(d1))


solution(A)
