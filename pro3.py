import re

def solution(new_id):

    #1단계 소문자 
    a=new_id.lower

    #2단계 제거
    a=re.sub('[^a-z0-9\-_,]','',a)

    #3단계 . 2개 이상을 1개로 압축
    a=re.sub('\.\.+','.',a)

    #4단계 양끝 .제거
    a=a.strip('.')

    #5단계 빈 문자열이면 a대입
    if a=='':a='a'

    #6단계 처음15개의 문자만 남기고 제거, 끝에.있으면 제거
    a=a[:15].rstrip('.')

    #7단계 길이가2자 이하라면 마지막문자 붙여서 3만들기
    a+=a[-1]*(3-len(a))
 

    return a