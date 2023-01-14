"""
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
U: 위쪽으로 한 칸 가기
D: 아래쪽으로 한 칸 가기
R: 오른쪽으로 한 칸 가기
L: 왼쪽으로 한 칸 가기
캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

"""
def solution(dirs):
    pos_dic = {}
    pos_x = 5
    pos_y = 5
    answer = 0
    for dir in dirs:
        pre_x = pos_x
        pre_y = pos_y
        if dir in ['U', 'D']:
            if dir == 'U':
                pos_y += 1 if pos_y < 10 else 0
            if dir == 'D':
                pos_y -= 1 if pos_y > 0 else 0
        if dir in ['L', 'R']:
            if dir == 'L':
                pos_x -= 1 if pos_x > 0 else 0
            if dir == 'R':
                pos_x += 1 if pos_x < 10 else 0
        if (pre_y, pre_x) != (pos_y, pos_x):
           key = str(set(((pre_y, pre_x), (pos_y, pos_x))))
           print(f'{dir} = ({pre_y},{pre_x}),({pos_y},{pos_x}),{answer},{key}')
           if pos_dic.get(key) == None:
               answer += 1
               pos_dic[key] = 1
        else:
           print(f'{dir} = ({pre_y},{pre_x}),({pos_y},{pos_x}),{answer}')
    return answer

if __name__=="__main__":
    datas = ["UUUUUUUUUUUUL", "UDUDUDLRLRUD"]
    for data in datas:
        print(solution(data))
