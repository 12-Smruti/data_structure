def f1():
    word=S.split()
    print('\n Word ',word)
    long=max(word,key=len)
    print('\n Longest word:',long)

def f2():
    res={i:S.count(i) for i in set(S)}
    ch=input('\n Enter character to check frquency of occurence:')
    print("\n Frequency of occerence of particular character",res[ch])

def  f3():
    S1=input('\n Enter string to check palindrome:')
    if S1==S1[::-1]:
        print('\nPalindrome')
    else:
        print('\n not Plindrome')

def f4():
    sub=input('\n Enter substring')
    print(S.find(sub))

def f5():
    word_list=S.split()
    print('\n Word list:',word_list)
    res={i:word_list.count(i) for i in set(word_list)}
    print('\n Count the occurence of each word',res)

S=input('\n Enter string:=')
while(1):
    print('\n 1.To dispaly longest word count:')
    print('\n 2.To determine Frequency of occerence of particular characterof string ')
    print('\n3.To check the string is palindrome or not ')
    print('\n4.To display index of substring ')
    print('\n5.To count occurence of each word in the given string:')

    c=int(input('\n Enter the choice: '))
    if c==1:
        f1()
    elif c==2:
        f2()
    elif c==3:
        f3()
    elif c==4:
        f4()
    elif c==5:
        f5()
    else:
        print('\n****************')
        break
