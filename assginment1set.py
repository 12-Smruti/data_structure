def f1():
    print('\n List of student who played both cricket and badminton',{i for i in groupA if i in groupB})

def f2():
    c=[i for i in groupA if i not in groupB]
    d=[i for i in groupB if i not in groupA]
    print('\n List of student who either play cricket or badminton but not both',{i for i in c+d})

def f3():
    #number of student played neither cricket nor badminton
    l1=[i for i in groupC if i not in groupA]
    l2=[i for i in l1 if i not in list(groupB)]
    print('\n number of student who played neither cricket nor badminton',set(l2),len(l2))

def f4():
    #Number of student who played cricket and football not badminton
    l3=[i for i in groupA if i not in groupC]
    l4=[i for i in l3 if i not in list(groupB)]
    print('\n Number of student who play cricket and football but not badminthon',set(l4),len(l4))

groupA=set()
groupB=set()
groupC=set()

A=int(input('\n Enter the number of student for groupA: '))
for i in range(A):
    name=input('\n Enter name:= ')
    groupA.add(name)
print(groupA)

B=int(input("\n Enter the number of student for groupB:"))
for i in range(B):
    name=input('\n Enter name:=')
    groupB.add(name)
print(groupB)

C=int(input('\n Enter the number of student for groupC:'))
for i in range(C):
    name=input('\n Enter name:= ')
    groupB.add(name)
print(groupC)

while(1):
    print('\n 1.List of student who played cricket and badminthon both: ')
    print('\n 2.List of student who played either cricket nor badminton not both:')
    print('\n 3.Number of student who played neither cricket or badminthon:')
    print('\n 4.Number of student who played cricket and football not badminthon')

    c=int(input('\n Enter choice:'))
    if c==1:
        f1()
    elif c==2:
        f2()
    elif c==3:
        f3()
    elif c==4:
        f4()
    else:
        print('\n*************')
        break
