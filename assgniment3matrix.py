def ADD():
    print ("The element wise addition of matrix is : ")
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(len(matrix1))
    for row in range(len(matrix1)):
        for column in range(len(matrix1[0])):
            result[row][column] = matrix1[row][column]+ matrix2[row][column]
    for r in result:
        print(r)
   
   
def SUB():
    print ("The element wise subtraction of matrix is : ")
    Sub_result = [[matrix1[row][column] - matrix2[row][column]for column in range(len(matrix1[0]))]for row in range(len(matrix1))]
    for r in Sub_result:
        print(r)
    
def MUL():
   print ("The element wise multiplication of matrix is : ")
   result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
   for i in range(len(matrix1)):
       for j in range(len(matrix2[0])):
           for k in range(len(matrix2)):
               result[i][j] += matrix1[i][k] * matrix2[k][j]
   for r in result:
        print(r)

def Trans():
    print ("The transpose of given matrix is : ")
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
                result[i][j]=matrix2[j][i]
    for r in result:
         print(r)
    
    

Rowsx = int(input("Give the number of rows:"))  
Columnsx = int(input("Give the number of columns:"))    
matrix1 = []  
print("Please give the entries row-wise:")   
for i in range(Rowsx):  
    r1 = []  
    for j in range(Columnsx):  
        r1.append(int(input()))  
    matrix1.append(r1)  
  
for i in range(Rowsx):  
    for j in range(Columnsx):  
        print(matrix1[i][j], end=" ")  
    print()  
    
Rowsy = int(input("Give the number of rows:"))  
Columnsy = int(input("Give the number of columns:"))  
matrix2 = [[int(input()) for c in range (Columnsy)] for r in range(Rowsy)]  
print(matrix2)  


while(1):
    print("1:Addition of Matrix\n2:Substraction of Matrix \n3:Multiplication of Matrix\n4:Transpose of Matrix")
    c=int(input("Enter Choice:"))
    if c==1:
        ADD()
    elif c==2:
        SUB() 
    elif c==3:
        MUL()
    elif c==4:
        Trans()
    else:
        break
