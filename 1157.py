s=input().upper()
s_list=list(set(s))

num=[]
for alpha in s_list:
        num.append(s.count(alpha))

a=sorted(num) #유의

if len(a)==1:
    print(s_list[0])

elif a[0]==a[1]:
    print('?')
else:
    print(s_list[num.index(max(num))])