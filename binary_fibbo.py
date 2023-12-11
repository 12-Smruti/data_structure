def BS(l,u,A,key):
    l=0
    u=len(A)-1
    mid=(l+u)//2
    if(A[mid]==key):
        print('\n student of roll no ',A[i],'is present')
    elif A[mid]>key:
        BS(A[0],mid-1,A,key)
    else:
        BS(mid+1,len(A)-1,A,key)

def fibbo(A,key,n):
    f2=0
    f1=1
    f=f2-f1
    while(f<n):
        f2=f1
        f=f2+f1
        offset=-1
    while(f>1):
        i=min(offset+f2,len(A)-1)
        if(a[i]<key):
            f=f1
            f1=f2
            f2=f-f1
        elif(a[i]>key):
            f=f2
            f1=f1-f2
            f2=f-f1
        else:
            print('\n Element found!!')

        if(f1 and a[n-1==key]):
            print('\nElement found',len(A)-1)
        else:
            print('\n Element not found',len(A)-1)
            
A=[]
n=int(input('\n Enter the number of student:'))
for i in range(n):
    a=int(input('\n Enter the roll no:'))
    A.append(a)
print(A)
key=int(input('\n Enter the roll no to search:'))

print('\n1.Binary Search \n2.Fibonacci Search')
while(1):
    c=int(input('\n Enter choice:'))
    if c==1:
        BS(A[0],len(A)-1,A,key)
    elif c==2:
        fibbo(A,key,n)
    else:
        break
