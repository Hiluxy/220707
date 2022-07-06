s_list=list(input())
time=0

for s in s_list:
    if ord(s)<68:
        time+=3
    elif ord(s)<71:
        time+=4
    elif ord(s)<74:
        time+=5
    elif ord(s)<77:
        time+=6
    elif ord(s)<80:
        time+=7
    elif ord(s)<84:
        time+=8
    elif ord(s)<87:
        time+=9
    else:
        time+=10

print(time)