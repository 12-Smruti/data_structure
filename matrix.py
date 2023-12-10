def accept_matrix(M) :
    print("Enter the order of the Matrix (row,col) : ")
    r = int(input("row = "))
    c = int(input("col = "))
    print("Enter the elements of the Matrix : \n")
    for i in range(r) :
       A = []
       for j in range (c) :
          A.append(int(input()))
       M.append(A)
    print("Matrix accepted successfully\n")


def display_matrix(M,r,c): 
   print("Matrix (%d,%d) : "%(r,c))
   for i in range(r) :
      print(end=' ')
      for j in range(c):
          print("%3d"%M[i][j],end=' ')
      print("")	


def addition_matrix(M1,M2,M3,r,c) :
    for i in range(r) :
        A = []        
        for j in range(c): 
           A.append(M1[i][j] + M2[i][j])
        M3.append(A)

def substraction_matrix(M1,M2,M3,r,c) :
    for i in range(r) :
        A = []        
        for j in range(c): 
           A.append(M1[i][j] - M2[i][j])
        M3.append(A)


def multiplication_matrix(M1,M2,M3,r1,c1,c2) :
      for i in range(r1) :
        A = []
        for j in range(c2) : 
            sum = 0
            for k in range(c1) :
                sum = sum + (M1[i][k] * M2[k][j])
            A.append(sum)
        M3.append(A)
        
def find_transpose_matrix(M,r,c,T) :
    for i in range(r):
        A = []
        for j in range(c):
           A.append(M[j][i])
        T.append(A)
def main():   
   while True :
       print("1: Accept Matrix");
       print("2: Display Matrix");
       print("3: Addition of Matrices");
       print("4: Substraction of Matrices");
       print("5: Multiplication of Matrices");
       print("6: Transpose Matrix");
       print("7: Exit");

       ch = int(input("Enter your choice : "))
       M3 = []       
       if (ch == 7):
           print ("End")
           break
       elif (ch==1):
           M1 = []
           M2 = []
           print("Input First Matrix ")
           accept_matrix(M1)
           r1 = len(M1)
           c1 = len(M1[0])
           print("Input Second Matrix ")
           accept_matrix(M2)
           r2 = len(M2)
           c2 = len(M2[0]) 
       elif (ch==2):
           print("First ",end=' ')
           display_matrix(M1,r1,c1)
           print("Second ",end =' ')
           display_matrix(M2,r2,c2)	
       elif (ch==3):
           print("First ",end=' ')
           display_matrix(M1,r1,c1)
           print("Second ",end =' ')
           display_matrix(M2,r2,c2)
           if(r1 == r2 and c1 == c2) :
               addition_matrix(M1,M2,M3,r1,c1)
               print("Addition  ")
               display_matrix(M3,r1,c1)
           else :
               print("Addition not possible (order not same)")

       elif (ch==4):
           print("\tFirst ",end=' ')
           display_matrix(M1,r1,c1)
           print("\tSecond ",end =' ')
           display_matrix(M2,r2,c2)
           if(r1 == r2 and c1 == c2) :
               substraction_matrix(M1,M2,M3,r1,c1)
               print("\tSubstraction  ")
               display_matrix(M3,r1,c1)
           else :
               print("substraction not possible (order not same)")
           
       elif (ch==5):
           print("First ",end=' ')
           display_matrix(M1,r1,c1)
           print("Second ",end =' ')
           display_matrix(M2,r2,c2)
           if(c1 == r2) :
               multiplication_matrix(M1,M2,M3,r1,c1,c2)
               print("Multiplication  ")
               display_matrix(M3,r1,c2)
           else :
               print("Multiplication not possible ")
       elif (ch==6):
           print("First ",end=' ')
           display_matrix(M1,r1,c1)
           find_transpose_matrix(M1,r1,c1,M3);
           print("Transpose  ",end=' ');
           display_matrix(M3,r1,c1)
       else :
           print ("Wrong choice entered !! Try again")

main()
quit()










