"""
길이가 n인 배열에 1부터 n까지 숫자가 중복 없이 한 번씩 들어
있는지를 확인하려고 합니다.
1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는 경우 true를,
아닌 경우 false를 반환하도록 함수 solution을 완성해주세요.
"""

import numpy as np
def solution1(arr):
    sum1 = np.sum(arr)
    len1 = len(arr)
    sum2 = int(((1+len1)*len1) / 2 )
    return True if sum1 == sum2 else False


import numpy as np
def solution2(arr):
    arr1 = np.aort(arr)
    return True if arr1[-1] == len(arr) else False
