n=int(input())
result=n
word_list=[]
for _ in range(n):
 word_list.append(input())

for word in word_list:
  appear=[word[0]] #초기화, word[0]
    #기존 단어=전 단어 ->다음꺼 흝기
  for i in range(1,len(word)):
    if word[i]==word[i-1]: 
      continue
    #기존 단어 !=전 단어
    if word[i] in appear: #기존 단어가 등장리스트에 이미 있는 경우
      result -=1
      break
    else:
      appear.append(word[i]) #기존 단어가 등장리스트에 없으면 추가해준다
  
print(result)
