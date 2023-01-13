"""
주어진 문장에서 앞과 뒤가 일치하는 부분을 찾아서 그 끝 위치를 반환하시요

예)
  adnddaaddddaaddifr
  data.  ==> aaddddaa, 13
  return ==> 13
"""
def solution(s):
    if len(s) == 0:
        return 0
    lists = list(s)
    listr = lists[::-1]
    print(f'{lists}')
    print(f'{listr}')
    lenofs = len(lists)
    lastpos = 0
    find = False
    for x in range(0, lenofs):
        for y in range(lenofs-1, x, -1):
            len1 = y - x
            if len1 >= 2:
                leftend = 0
                rightstart = 0
                #print(f'{x}, {y}')
                if lists[x] == lists[y]:
                    endpos = x + int(len1/2)
                    s1 = ''.join(lists[x:endpos+1])
                    newstartpos = lenofs - y - 1
                    newendpos = newstartpos + int(len1/2)
                    s2 = ''.join(listr[newstartpos:newendpos+1])
                    #print(f'{s1} == {s2}')
                    #print(f'{x}:{endpos}:{y}:{len1}:{lenofs}')
                    if s1 == s2:
                        find = True
                        lastpos = y
                        break
                #else:
                #    print(f'different {lists[x]}, {lists[y]}')
            else:
                break
        if find:
            break

    return lastpos + 1 if find == True else lastpos

if __name__=="__main__":
    datas = [["abcdcba",7],
             ["abacde",3],
             ["",0],
             ["abcdefggfedcba",14],
             ["dbsldsbcdefggfedcbadsdasda",18],
             ["ab",0]]

    for data in datas:
        print('next --------')
        print(f'result == {data[1]} == {solution(data[0])}')
