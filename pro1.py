def solution(s):
    result=len(S)
    for i in range(1,len//2+1):
        c=""
        prev=s[0:i]
        cnt=1

        for j in range(i,len(s),i):
            if prev==s[i:i+j]:
                cnt+=1
            else:
                c += str(cnt)+prev if cnt>=2 else prev
                prev=s[j:j+i]
                cnt=1
            
        c+=str(cnt)+prev if cnt>=2 else prev
        result=min(result,len(c))
    return result
