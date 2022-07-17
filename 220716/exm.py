from itertools import product



def Count(ob,no_len,no_list):

    #100에서
    if ob=='100':
        return print(0)
    
    num_list=['0','1','2','3','4','5','6','7','8','9']
    able_list=[i for i in num_list if i not in no_list]

    combi=[]
    for i in range(1,len(able_list)):
      combi+=list(product(able_list,repeat=i))


    m=int(ob)
    for tu in combi:
        number="".join(tu)
        m=min(abs(int(ob)-int(number)),m)

    cnt=m+len(ob)
    print(cnt)

ob=input()
no_len=input()
if no_len=='0':
    print(len(ob))
else:
    no_list=set(input().split())
    Count(ob,no_len,no_list)