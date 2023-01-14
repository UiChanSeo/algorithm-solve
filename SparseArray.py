#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
페이스북에서 제출된 문제입니다.

0이 대다수를 차지하는 큰 배열이 있습니다.

더 공간 효율적인 자료구조인 SparseArray를 다음과 같은 인터페이스로 구현하세요.

init(arr, size): 큰 원본 배열과 사이즈를 인자로 받아 초기화 합니다.
set(i, val): 인덱스 i 를 val 값으로 업데이트 합니다.
get(i): 인덱스 i 번째 값을 반환합니다.
"""

import pytest

class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self.map = {}

        orig_arr_size = len(arr)
        for i, e in enumerate(arr):
            if i>= orig_arr_size:
                break
            if e != 0:
                map[i] = e

    def check_bounds(self, i):
        if i < 0 or i>= self.size:
            print(f'IndexError {i}')
            raise IndexError()

    def set(self, i, val):
        self.check_bounds(i)
        print(f'set {i} = {val}')
        self.map[i] = val

    def get(self, i):
        self.check_bounds(i)
        v = self.map.get(i)
        if v is None:
            print(f'get {i} is None')
            return 0

        print(f'get {i} is {v}')
        return v
      
if __name__=="__main__":
    arr = SparseArray([0,0,0], 5)

    assert arr.get(0) == 0
    assert arr.get(3) == 0

    with pytest.raises(IndexError):
        assert arr.get(-1)
        assert arr.get(0, 0)
        assert arr.get(5)
        assert arr/get(5,0)

    arr.set(0,1)
    assert arr.get(0) == 1
    arr.set(4,1)
    assert arr.get(4) == 1
