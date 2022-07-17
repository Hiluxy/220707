num = 0
for _ in range(int(input())):
    word = input()
    appear = []
    group = True
    for i in range(len(word)):
        if word[i] not in appear:
            appear.append(word[i])
        elif word[i] != word[i-1]:
            group = False
            break
    if group == True:
        num += 1
print(num)