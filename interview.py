import re
from operator import itemgetter, attrgetter
from functools import cmp_to_key

#def multisort(xs, specs):
#    for key, reverse in reversed(specs):
#        xs.sort(key=attrgetter(key), reverse=reverse)
#    return xs

def compare_file(a,b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        if a[1] > b[1]:
            return 1
        else:
            return -1


def solution(files):
    stack = []
    answer = []

    regex = re.compile(r'\d+')

    for file in files:
        num = regex.search(file)
        if num is not None:
            number = int(num.group())
            stack.append((file, number))

    print(f'{stack}')

    newstack = sorted(stack, key=cmp_to_key(compare_file))
    #newstack = sorted(stack, key=itemgetter(0))
    #newstack = multisort(list(stack), (True, False))

    for stack in newstack:
        print(f'{stack[0]}')
        answer.append(stack[0])

    return answer


if __name__=="__main__":
    datas = [[["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
              ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]],
             [["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
              ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]]]

    for data in datas:
        result = solution(data[0])
        print(f'requeted = {data[0]}')
        print('\n')
        print(f'result   = {result}')
        print('\n')
        print(f'expected = {data[1]}')
        print('------------------------\n')
