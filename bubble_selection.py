def bubble():
    n=len(arr)
    for i in range(n-i-1):
        if arr[i]>arr[i+1]:
            swap(arr[i],arr[i+1])
            #arr[j],arr[j+1]=arr[j+1],arr[j]
            print('\n Bubble sort=',arr)

def selection():
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min=j
                temp=arr[i]
                arr[i]=arr[min]
                arr[min]=temp
    print('\n Selection Sort ',arr)

arr=[]
m=int(input('\n Enter number of ele='))
for i in range(m):
    ele=float(input('\n Enter percentage: '))
    arr.append(ele)
    print('\n percentage beffore sorting=',arr)

while(1):
    print('\n1.Bubble \n2.Selection')
    ch=('\n Enter chioce=')
    if ch==1:
        bubble()
    elif ch==2:
        selection()
    else:
        print('\n*************')
        break
