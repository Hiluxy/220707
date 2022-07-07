#로또
def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    zero_cnt=lottos.count(0)
    cnt=0
    for i in lottos:
        if i in win_nums:
            cnt+=1
    
    answer = [rank[cnt+zero_cnt],rank[cnt]]
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))