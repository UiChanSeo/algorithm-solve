"""
1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해
주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

"""

def solution(board):
    answer = 1234
    maxv = 0
    
    xlen = len(board)
    ylen = len(board[0])
    
    if ylen == 1 or xlen == 1:
        return 1
    
    for i1 in range(1, xlen):
        for i2 in range(1, ylen):
            if board[i1][i2] == 1:
                board[i1][i2] = min(board[i1-1][i2-1],
                                     board[i1-1][i2],
                                     board[i1][i2-1])+1
                maxv = max(maxv, board[i1][i2])
            else:
                board[i1][i2] = 0
    return maxv * maxv
