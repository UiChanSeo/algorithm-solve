'''
아파트에 설치할 안테나의 수를 구하라.
예를 들어 기존에 다음과 같이 안테나가 설치 된 아파트 단지가 있다.
그런데, 안테나를 새로 설치할려고 한다. 새로 설치하는 안테나가 성능은 좋으나 커버리지가 작아져서 신규로 설치해야 한다.
그럴 경우에 추가 되는 안테나의 수는 몇 개인가?
예 )
   1 2 3 4 5 6 7 8 9 10 11
         *              *
   coverage 4 -> 1
   
   추가 될 안테나의 수 3개 (8,5,1)
   
입력은 전체 동수 (n), 기존 안테나의 위치(stations), coverage(w) 이다.
'''

def solution(n, stations, w):
    answer = 0


    pos = n

    #print(f'n={n}{type(n)}, stations={stations}')
    if len(stations) > 0:
        antenna = stations.pop()
    else:
        antenna = 0

    has_antenna = False

    new_antenna = []

    while pos > w:
        print(f'....{antenna}:{pos}')
        if ((pos - w) <= antenna) and (antenna <= pos):
            print(f'has antenna {antenna}:{pos}')
            pos = antenna - 1
            if len(stations) > 0:
                antenna = stations.pop()
            else:
                antenna = 0
            has_antenna = True
        else:
            if has_antenna:
                print(f'none1___ {antenna}:{pos}')
                pos = pos - w
                has_antenna = False
                print(f'none2___ {antenna}:{pos}')
            else:
                antenna1 = pos - w
                print(f'new  ___ {antenna}:{antenna1}')
                new_antenna.append(antenna1)
                pos = pos - w - 1
                answer += 1
                has_antenna = True

    return answer, new_antenna



if __name__=="__main__":
    datas = [[11, [4, 11], 1, 3],
             [16, [9], 2, 3],
             [16, [0], 4, 2],
             [16, [], 4, 2],
             [16, [], 1, 2],
             [12, [3,10,12], 3, 1],
            ]

    for data in datas:
        print(f'{data[0]},{data[1]},{data[2]},{data[3]},{solution(data[0], data[1], data[2])}')
