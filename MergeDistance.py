"""
스냅챗에서 출제된 문제입니다.
중첩될 수 있는 인터벌들을 갖는 리스트가 있습니다. 중첩되는 인터벌들을 하나로 합친 새로운 리스트를 반환하세요.
입력 리스트는 정렬되어 있지 않습니다.
예를 들어, [(1, 3), (5, 8), (4, 10), (20, 25)] 가 주어지면, [(1, 3), (4, 10), (20, 25)] 를 반환해야 합니다.
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
def solution0(data):
    new_list = sorted(data, key=lambda x:(x[0],x[1]))
    print('sorted = ', new_list)
    for x in range(0, len(new_list)):
        for y in range(len(new_list)-1, x, -1):
            print(new_list[x][1], new_list[y][1])
            if new_list[x][1] > new_list[y][1]:
                del new_list[y]
            elif new_list[x][1] < new_list[y][1]:
                del new_list[x]
        if x > y:
            break
        print('--next-- x=', x, 'y=', y, ',len=', len(new_list))
    return new_list

if __name__=="__main__":
    datas = [[[(1,3),(5,8),(4,10),(20,25)],
              [(1,3),(5,8),(20,25)]],
             [[(2,7),(3,3),(14,16),(1,9),(15,100)],
              [1,9],[14,16],[15,100]],
             [[(3,5),(2,17),(5,7),(1,10),(10,20),(1,100)],
              [(1,100)]]]
    for data in datas:
        print('resolved = ', solution0(data[0]))
        print('origin   = ', data)
        print('-----------------------')
