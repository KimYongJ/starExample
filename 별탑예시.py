while True:
    print("1 입력시 정삼각형 출력")
    print("2 입력시 정삼각형 출력")
    print("3 입력시 정삼각형 출력")
    a=input("무엇을 출력할까요? : ")
    if a.isdigit()==True:
        a=int(a)
        if a>=1 and a<=3:
            x=input("몇층의 별을 만들지 입력해주세요 : ")
            if x.isdigit()==True:
                x=int(x)
                if a==1:
                    for i in range(x):
                        print( (' '*(x-i)) + ('*'*(i+1))+ ('*'*i) )
                elif a==2:
                    for i in range(x):
                        print( (' '*i)+('*'*(x-i))+('*'*(x-i-1))  )
                else:
                    for i in range(x):
                        print( (' '*(x-i-1)) + ('*'*(i+1))+ ('*'*i) )
                    for i in range(x):
                        if i==0:
                            continue
                        print( (' '*i)+('*'*(x-i))+('*'*(x-i-1))  )
            else:
                print('\n\n숫자를 입력해주세요!!\n\n')
        else:
            print("\n\n1, 2, 3 중에 하나만 입력해주세요.\n\n")
    else:
        print("\n\n숫자를 입력해주세요\n\n")




