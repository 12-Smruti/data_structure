import numpy as np

def ADD():
    print('\n The element wise addition of matrix is:')
    print(np.add(x,y))

def SUB():
    print('\n The element wise subtraction:')
    print(np.subtract(x,y))

def MUL():
    print('\n the element wise multiplication of matrix:')
    print(np.multiply(x,y))

def TRAN():
    print('\n The transpose of given matxir:')
    print(x.T)

row1=int(input('\n Enter the rows for matrix 1:'))
col1=int(input('\n Enter the cols for matrix 1:'))
print('\n Please write the element in single line separated by spcae:')
ele=list(map(int,input().split()))
print(ele)
x=np.array(ele).reshape(row1,col1)
print(x)

row2=int(input('\n Enter the rows for matrix 2:'))
col2=int(input('\n Enter the cols for matrix 2:'))
print('\n Please write the element in single line separated by spcae:')
ele=list(map(int,input().split()))
y=np.array(ele).reshape(row2,col2)
print(y)

while(1):
    print('\n1. Addition of Matrix:')
    print('\n2. Subtraction of Matrix:')
    print('\n3. Multiplication of Matrix:')
    print('\n4. Transpose of Matrix:')

    c=int(input('\n Enter choice:'))
    if c==1:
        ADD()
    elif c==2:
        SUB()
    elif c==3:
        MUL()
    elif c==4:
        TRAN()
    else:
        print('\n***********')
        break
