"""
반 학생 명단과 출석한 학생의 명단이 주어진 경우에, 결석한 학생의 이름을
찾아라.

예 )
학생 명단 = ["leo", "kiki", "eden"]
출석 명단 = ["eden", "kiki"]

답 : leo
"""

import numpy as np

def solution(participant, completion):
    participant1 = np.sort(participant)
    completion1 = np.sort(completion)

    print('sorted=', participant1, completion1)

    len1:int = len(participant1)

    diff: int = int(len1/2)
    pos: int = diff

    print('len1=', len1, 'diff=',diff,'pos=', pos)

    while diff >= 1:


        diff = int(diff / 2)

        if participant1[pos] == completion1[pos]:
            if diff > 0 :
                pos = pos + diff
                if pos >= (len1-1):
                    pos = len1 - 1
                    break
            else:
                pos = pos + 1
                break
        else:
            print('right-----')
            if participant1[pos - 1] == completion1[pos - 1]:
                break
            else:
                if diff > 0:
                    pos = pos - diff
                    if pos < 1:
                        break
                else:
                    pos = pos - 1
                    break
        print('diff=',diff,'pos=', pos)
    print('last diff=',diff,'pos=', pos)

    return participant1[pos]
if __name__ == "__main__":
    datas = [[["leo", "kiki", "eden"],
              ["eden", "kiki"], "leo"],
             [["marina", "josipa", "nikola", "vinko", "filipa"],
              ["josipa", "filipa", "marina", "nikola"], "vinko"],
             [["marina", "josipa", "nikola", "vinko", "filipa"],
              ["vinko", "filipa", "marina", "nikola"], "josipa"],
             [["marina", "josipa", "nikola", "vinko", "filipa"],
              ["vinko", "josipa", "marina", "nikola"], "filipa"],
             [["mislav", "stanko", "mislav", "ana"],
              ["stanko", "ana", "mislav"], "mislav"],
             [["mislav", "stanko", "mislav", "ana"],
              ["mislav", "ana", "mislav"], "stanko"]]
    result = []
    for data in datas:
        find = solution(data[0], data[1])
        resultset = (data[2], find, find==data[2])
        result.append(resultset)
    print(result)
    print("success")
