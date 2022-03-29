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
            #print(l)
        else:
            #print(A[i])
            if len(l)!=0:
                if (A[i]>d[-1] and d[-1]<d[-2]) or (A[i]<d[-1] and d[-1]>d[-2]):
                    l.append(A[i])
                    d.append(A[i])
                elif (A[i]>d[-1] and d[-1]>d[-2]) or (A[i]<d[-1] and d[-1]<d[-2]):
                    d.append(A[i])
            if len(l1)!=0:
                if (A[i]>d1[-1] and d1[-1]<d1[-2]) or (A[i]<d1[-1] and d1[-1]>d1[-2]):
                    l1.append(A[i])
                    d1.append(A[i])
                elif (A[i]>d1[-1] and d1[-1]>d1[-2]) or (A[i]<d1[-1] and d1[-1]<d1[-2]):
                    d1.append(A[i])
                elif (A[i] == d1[-1] and d1[-1] < d1[-2]) or (A[i] == d1[-1] and d1[-1] > d1[-2]) or (A[i] == d1[-1] and d1[-1] == d1[-2]):
                    d1.append(A[i])
                elif (A[i] > d1[-1] and d1[-1] == d1[-2]) or (A[i] < d1[-1] and d1[-1] == d1[-2]):
                    d1.append(A[i])
                    l1.append(A[i])
                    l1.pop(1)

    if len(l)!=0:
        print(len(d)-len(l))
    elif len(l1) != 0:
        print(len(d1)-len(l1))

solution(A5)

A=[5,3,5,7,5]
A1=[5,2,6,4,7,3]
A2=[2,5,4,6,3,7]
A3=[1,3,1,2]
A4=[5,5,3,4,5]
A5=[5,5,6,4,5]
