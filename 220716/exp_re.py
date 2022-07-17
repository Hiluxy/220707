from itertools import product



def Count(ob,no_len,no_list):

    #100에서 시작
    if ob=='100':
        return print(0)
    
    num_list=['0','1','2','3','4','5','6','7','8','9']
    able_list=[i for i in num_list if i not in no_list]

    #가능한 모든 조합
    combi=[]
    for i in range(1,len(ob)+2):
      combi+=list(product(able_list,repeat=i))

    number_list=[]
    #모든 조합을 number_list에 넣기
    for tu in combi:
        number_list.append("".join(tu))

    #목표 번호와의 차이가 최소가 되는 m
    m=int(ob)
    for num in number_list:
      m=min(abs(int(ob)-int(num)),m)
    
    ob_num_list=[str(ob-m),str(ob+m)]
    real=[]
    for i in range(len(ob_num_list)):
      if ob_num_list[i] in number_list:
        real.append(ob_num_list[i])
    button_push=real[0]
        
    #(처음 번호 누르는 횟수)+(+- 횟수) 
    cnt=button_push+m
    print(cnt)

ob=input()
no_len=input()
if no_len=='0':
    print(len(ob))
else:
    no_list=set(input().split())
    Count(ob,no_len,no_list)