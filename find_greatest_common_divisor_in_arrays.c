/* 
 2021-03-10 swhors@naver.com
 
 주어진 수열의 최대 공약수를 구하는 코드 입니다.
 */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int getgcd(int a, int b) {
    int big = (a>b?a:b);
    for (int i = big; i> 0; i--) {
        if ((a % i == 0) && (b % i == 0)) return i;
    }
    return 0;
}

int solution(int *arr, size_t arr_len) {
    int gcm = arr[0];
    for (int i = 1;i < arr_len;i++) {
        printf("left = %d, right = %d\n", gcm, arr[i]);
        int gcd = getgcd(gcm, arr[i]);
        gcm = gcd * (arr[i]/gcd) * (gcm/gcd);
        printf("gcd  = %d, gcm   = %d\n", gcd, gcm);
    }
    return gcm;
}

typedef struct TestData{
    int data[25];
    int len;
} TestData;

int main() {

    TestData datas[6] = {
        {.data = {2,6,8,14}, .len=4},
        {.data = {1,2,3}, .len=3},
        {.data = {3,6,7}, .len=3},
        {.data = {7,15,20}, .len=3},
        {.data = {60,28,21}, .len=3},
        {.data = {7,21,35}, .len=3}
    };


    for( int i = 0; i < 6; i++ ) {
        printf("%d = %d\n",
               i,
               solution(datas[i].data, datas[i].len));
    }

}
