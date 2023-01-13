# -*- coding: utf-8 -*-
"""

문제 설명

1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. (단, 정
사각형이란 축에 평행한 정사각형을 말합니다.)
예를 들어
1   2   3   4
0   1   1   1
1   1   1   1
1   1   1   1
0   0   1   0
가 있다면 가장 큰 정사각형은 9

"""

import math

def solution(board):
    answer = 0

    y_depth = len(board)

    if y_depth == 0:
        return 0

    x_depth = len(board[0])
    if x_depth == 0:
        return 0

    answer = max(board[0])

    if x_depth== 1:
        return max([x[0] for x in board])

    for y in range(1, len(board)):
        for x in range(1, len(board[0])):
            if board[y][x] == 1:
                top1 = board[y-1][x-1]
                top2 = board[y-1][x]
                left = board[y][x-1]
                min_val = min([top1, top2, left])
                if min_val > 0:
                    board[y][x] = min_val + int(math.sqrt(min_val))*2 + 1
                    if answer < board[y][x]:
                        answer = board[y][x]
                elif min_val == 0:
                    max_val = max([top1, top2, left])
                    if max_val == 0:
                        answer = 1
    return answer

if __name__=="__main__":
    datas = [[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]],
             [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
             [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]],
             [[1,1,1,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]],
             [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]],
             [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
             [[1,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,1]],
             [[1,0],[1,0]],
             [[1,1,],[1,1]],
             [[0,0,1,0,]],
             [[0],[1],[0]],
             [[]],
             []]
    
    for data in datas:
        result = solution(data)
        print(data,result)
