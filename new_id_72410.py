import re
def solution(new_id):
    answer = ''
    #1단계
    new_id=new_id.lower()
    #2단계
    new_id=re.split('[^a-z0-9-_.]',new_id)
    new_id=''.join(list(filter(lambda x:x != '',new_id)))
    #3단계
    while '..' in new_id:
        new_id=new_id.replace('..','.')
    #4단계
    if new_id and new_id[0]=='.':
        new_id=new_id[1:]
    if new_id and new_id[-1]=='.':
        new_id=new_id[:-1]
    #5단계
    if new_id=='':
        new_id='a'
    #6단계
    if len(new_id)>15:
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id[:-1]
    #7단계
    while len(new_id)<3:
        new_id+=new_id[-1]
    
    return new_id
'''
알게된점
문자열.replace(치환하고싶을문자, 치환할문자)
'''
