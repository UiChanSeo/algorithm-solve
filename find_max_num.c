/***
 2021/03/10 swhors@naver.com
 
 아래 코드는 주어진 수열의 조합으로 최대 값을 찾는 코드입니다.
 예로 [1,3,5] 주어진 경우에, 531을 반환하는 것입니다.
 
 아래의 값이 입력 된 경우의 출력은 다음과 같습니다.
 
 {1,2,3,4}, {8,2,13,4,11,10,22}, {1,10,17,107,3}
 
 
simpson@205:~/work/c$ g++ solution.c
simpson@205:~/work/c$ ./a.out
result = 4321
result = 84222131110
result = 317110710
simpson@205:~/work/c$
 
 ***/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define _DBG 0
#undef _DBG

/* 수의 10의 자리수를 반환 합니다. */
int get_num_length(int a) {
    int cnt = 1;
    int b = a / 10;

    while( b != 0 ) {
        b = b / 10;
        cnt = cnt * 10;
    }

    return cnt;
}

/* 수열의 정렬합니다. */
/* 정렬 기준은 두 수를 조합해서 최고의 값이 나오는 순서입니다. */
int *boglebogle(int *a, int len) {
    int *pos = (int*) malloc(sizeof(int)*len);
    for (int i = 0;i < len;i++) {
        pos[i] = get_num_length(a[i]);
    }

    for (int x = 0;x < len; x++) {
        for(int y = x + 1;y < len;y++) {
            int num1 = a[x] * pos[y] * 10 + a[y];
            int num2 = a[x] + a[y] * pos[x] * 10;
            //printf("%d[%d], %d[%d]\n", num1, a[x], num2, a[y]);
            if (num1 < num2) {
                int tmpv = a[x];
                int tmpp = pos[x];
                pos[x] = pos[y];
                a[x] = a[y];
                pos[y] = tmpp;
                a[y] = tmpv;
            }
        }
    }
    return a;
}

char *find_max_num(int *a, int len) {
    /* 1. 앞자리의 수가 큰 순으로 정렬 */
    int *sorted = boglebogle(a, len);

#if defined _DBG

    /* 2. 데이터 확인 */
    for(int i = 0;i < len;i++)
    {
        printf("%d, ", sorted[i]);
    }
    printf("\n");
#endif


    /* 3. 수 들을 JOIN */
    char *num = (char*)malloc(10);
    sprintf(num, "%d", sorted[0]);
    for (int i = 1;i< len;i++) {
        char tmp[10];
        sprintf(tmp, "%d", sorted[i]);

        strcat(num, tmp);
    }

#if defined _DBG
    /* 4. 데이터 확인 */
    printf("sorted %s\n", num);
#endif

    /* 5. 반환 */
    return &num[0];
}

int main() {
    int data[4] = {1,2,3,4};
    int data1[7] = {8,2,13,4,11,10,22};
    int data2[5] = {1,10,17,107,3};
    int data_len = 4;
    int data_len1 = 7;
    int data_len2 = 5;

    printf("result = %s\n",
           find_max_num((int*)&data0[0], data_len0));

    printf("result = %s\n",
           find_max_num((int*)&data1[0], data_len1));

    printf("result = %s\n",
           find_max_num((int*)&data2[0], data_len2));
}
