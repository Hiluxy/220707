_=input()
aa=list(map(int,input().split()))
_=input()
bb=list(map(int,input().split()))

for b in bb:
    if b in aa:
        print(1,end=" ")
    else:
        print(0,end=" ")