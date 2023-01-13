"""
수가 쓰인 돌들이 수열과 같이 있을 때, 
그 돌을 1개씩 건너서 만들어 지는 최대 값을 구하라.
예를 들어 다음과 같이 
  [ 1, 2, 3, 4]
  [ 5, 6, 7, 8]
  [ 9, 8, 7, 6]
있을 때, 1열에 하나, 2열에 하나, 3열에 하나 씩 더하여 최대값을 구하여라.
단 1열을 1번 돌을 건너면, 2열의 1번 돌을 밟을 수 없다. 다른 돌도 마찬가리로
자신의 아래 돌은 밟을 수 없다.

위의 경우는
 4 + 7 + 9 = 20 or 3 + 8 + 9 = 20
이 된다.
"""

def get_max(l, e):
    max_val = -9999
    max_pos = 0
    for i in range(0, len(l)):
        if (i != e) and (max_val <l[i]):
            max_val = l[i]
            max_pos = i
    return max_val, max_pos

def solution1(land):
    max_poss = []
    for y in range(1, len(land)):
        for x in range(0, len(land[0])):
            max_val, max_pos = get_max(land[y-1], x)
            max_poss.append(max_pos)
            land[y][x] = max_val + land[y][x]
    return max(land[len(land)-1]), max_poss


if __name__=="__main__":
    datas = [[[1,2,3,5],[5,6,7,8],[4,3,2,1]],
            [[1,2,3,5],[5,6,7,8],[4,3,2,1],[9,8,7,6]],
            [[1,2,3,5],[5,6,7,8],[4,3,2,1],[9,8,7,6],[2,4,-1,3]]]

    for data in datas:
        print(solution1(data))
