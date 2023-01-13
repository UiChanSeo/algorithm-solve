/***
 입력으로 수열과 쿼리가 주어지는 경우에 쿼리를 참조하여 수열에서 합을 구하라.
 쿼리는 다음과 같이 세 개의 값을 가진다.
   [시작, 끝, 0을 대체하는 수]
 합을 구하면서, 수에 0이 나오는 경우에 위 쿼리에서 "0을 대체하는 수"를 더한다.
 
 예)
   수열 : 1,2,0,4,5
   쿼리 : 1, 3, 5
   
 과정)
   1 + 2 + 5(0을 대체함)
 답)
   8
***/

def findSum(numbers, queries):
    answers = []
    for query in queries:
        print(f'query = {query}')
        answer = 0
        for x in range(query[0],query[1]+1):
            if numbers[x] == 0:
                answer += query[2]
            else:
                answer += numbers[x]
        answers.append(answer)
    return answers

if __name__=="__main__":
    data = [[3,5,10,10,1,3],[[1,2,5]]]

    print(findSum(data[0], data[1]))
