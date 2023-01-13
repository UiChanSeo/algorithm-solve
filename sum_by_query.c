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

long* findSum(int numbers_count, int* numbers, int queries_rows, int queries_columns, int** queries, int* result_count) {
    long * answers = (long*)malloc(queries_rows * sizeof(long));
    for(int i = 0;i < queries_rows;i++) {
        long answer = 0L;
        for(int x = queries[i][0]-1;x < queries[i][1];x++) {
            if (numbers[x]==0)
                answer += (long)queries[i][2];
            else
                answer += (long)numbers[x];
        }
        answers[i] = answer;
    }
    *result_count = queries_rows;
    return answers;
}
