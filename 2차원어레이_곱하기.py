# -*- coding: utf-8 -*-

"""
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한
결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
"""
def solution(arr1, arr2):
    len_1_y = len(arr1)
    len_2_y = len(arr2)
    len_1_x = len(arr1[0])
    len_2_x = len(arr2[0])

    arr = [[0 for x in range(0, len(arr1[0]))] for y in range(0, len(arr1))]

    if len_1_x != len_2_y:
        return [0,0]
    for y in range(0, len(arr1)):
        for x in range(0, len(arr1[0])):
            for x1 in range(0, len(arr1[0])):
                print(f'{y}, {x}, {x1}')
                arr[y][x] += arr1[y][x1] * arr2[x1][x]
    return arr

if __name__=="__main__":
    datas = [[[[1,4],[3,2],[4,1]],
              [[3, 3],[3, 3]],
              [[15,15],[15,15],[15,15]]],
             [[[2,3,2],[4,2,4],[3,1,4]],
              [[5,4,3],[2,4,1],[3,1,1]],
              [[22,22,11],[36,28,18],[29,20,14]]]]
    for data in datas:
        result = solution(data[0], data[1])
        print(result, (result == data[2]))
