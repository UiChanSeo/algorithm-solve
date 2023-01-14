"""
2021-03-18 swhors@naver.com

사용자의 ID를 받아서 아래의 예제와 같은 결과가 나오도록 수정

예)
  '..Philgineer...com#-kakao..,' ==> 'Philgineer.com-kakao'
"""

import re


def solution(id):
    i = 0
    id_list = list(id)
    answer = []

    pre = ''

    for c in id_list:
        if c.isalpha() or c.isdigit():
            answer.append(c)
            pre = c
        else:
            if len(pre) > 0 and pre != c:
                if c == '-' or c == '.':
                    answer.append(c)
                    pre = c

    if answer[len(answer) -1].isalpha() == False and \
       answer[len(answer) -1].isdigit() == False:
       answer.pop()
    return ''.join(answer)

if __name__=="__main__":
    datas = [['..Philgineer...com#-kakao..,',
              'Philgineer.com-kakao']]

    for data in datas:
        ret = solution(data[0])
        print(f'{data[0]} = {ret==data[1]} / {data[1]}')
