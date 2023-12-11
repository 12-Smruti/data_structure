A=[]
n=int(input('\n Enter no of students:'))
for i in range(n):
    a=int(input('\n Enter Roll no :'))
    A.append(a)
print(A)
key=int(input('\n Enter the roll no'))

def LS(A,key):
    for i in range(len(A)):
        if A[i]==key:
            flag=1;
            break
        else:
            flag=0
    if flag==1:
        print('\n Studen of roll no',A[i],' is present')
    else:
        print('\n Studen of roll no',A[i],' is not present')

def SS(A,key):
    key=int(input('\n Enter the roll no'))
    size=len(A)
    A.append(key)
    i=0
    while(key!=A[i]):
        i+=1

    if i==size:
        print('\n Student is not present')
    else:
        print('\n Student is present')
print('\n 1.Linear Search \n2.Sequencial Search')
while(1):
    c=int(input('ENter the choice:'))
    if c==1:
        LS(A,key)
    elif c==2:
        SS(A,key)
    else:
        print('\n***********')
        break
