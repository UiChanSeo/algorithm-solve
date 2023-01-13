/* 
 Programmers의 자카드 유사도에 관한 문제입니다.
이 문제에서 결과치는 자카드 유사도에 65536을 곱하고
소스점을 버리고 반환합니다.
 */
def get_jakard_member(arr):
    new_arr = []
    for x in range(0, len(arr)-1):
        if arr[x].isalpha() and arr[x+1].isalpha():
            print(f'{x} {arr[x]}, {arr[x+1]}')
            new_arr.append(arr[x]+arr[x+1])
    return new_arr

def solution(str1, str2):
    arr1 = list(str1.upper())
    arr2 = list(str2.upper())

    arr3 = set(get_jakard_member(arr1))
    print('--------------------')
    arr4 = set(get_jakard_member(arr2))
    print('--------------------')

    print(f'arr3 = {arr3}')
    print('--------------------')
    print(f'arr4 = {arr4}')

    print('--------------------')

    s1 = arr3 & arr4
    s2 = arr3 | arr4
    print(f's1 =  {s1}')
    print(f's2 =  {s2}')
    if len(s1) == 0 or len(s2) == 0:
        return 65536

    return (int)((len(s1) / len(s2)) * 65536)


if __name__=='__main__':

    ```
    아래의 데이터에서 첫 번째 컬럼이 data1이고, 두 번째 컬럼이 data2입니다.
    그리고, 세 번째 컬럼이 원하는 값입니다.
    ```
    datas = [['FRANCE', 'FRENCH', 16384],
             ['FRANCE', 'french', 16384],
             ['handshake', 'shake hands', 65536],
             ['aa1+aa2', 'AAAA12', 43690],
             ['E=M*C^2', 'e=m*c^2', 65536]]

    for data in datas:
        ans = solution(data[0], data[1])
        print(f'jakard = {ans}, {ans==data[2]}')
