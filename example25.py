def solution(A):
    stack=[]
    #count=0
    count1=0
    if len(A)%2!=0:
        l=A.copy()
        for i in range(len(l)):
            k=l.pop(i)
            l1=l.copy()
            #print(l1)
            l.insert(i,k)
            stack.append(l1)
        for ele in stack:
            count=0
            if len(ele)%2==0:
                l2=ele.copy()
                #print(l2)
                for i in range(1,len(ele)):
                    if i%2!=0:
                        if ele[i]<ele[i-1]:
                            break
                        else:
                            count+=1
                    elif i%2==0:
                        if ele[i]>ele[i-1]:
                            break
                        else:
                            count+=1
            #print(count)
            if count==len(ele)-1:
                count1+=1
            elif count==0:
                count1=-1
        if count1==1:
            count1=0
        print(count1)

    elif len(A)%2==0:
        ele=A.copy()
        count2=0
        for i in range(1,len(ele)):
            if i%2!=0:
                if ele[i]<ele[i-1]:
                    break
                else:
                    count2+=1
            elif i%2==0:
                if ele[i]>ele[i-1]:
                    break
                else:
                    count2+=1
        if count2==len(ele)-1:
            count1+=1
        else:
            count1=-1

        if count1==1:
            count1=0
        print(count1)


a=solution([1,3,1,2])
