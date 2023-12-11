A=[]
n=int(input('\n Enter the number of student:'))
for i in range(n):
    a=int(input("\n Enter roll no of student"))
    print(A.append(a))
print(A)

key=int(input('\n Enter the key'))
def ls(A,key):
    for i in range(len(A)):
        if A[i]==key:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        print('\n Student of rollno ',A[i],' is present')
    else:
        print('\n Student of rollno ',A[i],' is not present')

def SS(A,key):
    size=key
    A.append(key)
    i=0
    while(key!=A[i]):
        i+=1
    if i==size:
        print('\n Student is not present')
    else:
        print('\n Student is not prsent')
print('\n1.Linear Search \n2.Sentinal Search')
ch=int(input('\n Enter the choice:'))
if ch==1:
    ls(A,key)
if ch==2:
    SS(A,key)
else:
    print('\n****************')
    #break
    
