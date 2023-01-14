# -*- coding: utf-8 -*-

"""
2진수로 변활 할 경우, 1의 수가 같은 큰 수 중에서 최소수를 찾아라.

예 78 => 1001110
   83 => 1010011
"""
def dec2bin(num):
    bin_num = []
    bin_num.append(num % 2)
    leave = num % 2
    num = int(num / 2)
    while num > 0:
        leave = num % 2
        bin_num.insert(0, leave)
        num = int(num / 2)
    return bin_num

def solution(n):
    bin_num = dec2bin(n)

    print(f'bin_num = {bin_num}')
    changed = False
    for i in range(len(bin_num)-1, 0, -1):
        print(f'{i} = {bin_num[i]}')
        if bin_num[i-1] < bin_num[i]:
            changed = True
            bin_num[i-1] = 1
            bin_num[i] = 0
            if i < (len(bin_num) - 1):
                for y in range(len(bin_num)-1, i, -1):
                    if bin_num[y-1] > bin_num[y]:
                        bin_num[y-1] = 0
                        bin_num[y] = 1
            break
    if changed == False:
        bin_num[0] = 0
        bin_num.insert(0, 1)
    print(f'chnaged = {bin_num}')
    bin_num = [str(x) for x in bin_num]
    bin_num = '0b' + ''.join(bin_num)
    return int(bin_num, 2)


if __name__=="__main__":
    datas = [[78,83], [15,23]]

    for data in datas:
        print(f'{data[0]} = {solution(data[0])}, {data[1]}')

if __name__=="__main__":
    datas = [[78,83], [15,23]]

    for data in datas:
      
