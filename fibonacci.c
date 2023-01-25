/* 
 아래의 코드는 피보나치 수열을 구하는 코드입니다.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define _DBG
//#undef _DBG

int solution(int n) {
    unsigned long left = 0;
    unsigned long right = 1;

    if (n == 0) return 0;
    if (n == 1) return 1;

    for (int i = 2;i <= n;i++) {
        unsigned long tmp = right;
        right = left + right;
        left = tmp;
    }

#ifdef _DBG
    printf("\n\tleft = %lu, right = %lu\n", left, right);
#endif
    return (int)(right % 123456789);
}

int main() {
    int ns[] = {1, 2, 3, 4, 5, 10,
                50, 100, 99996, 99997, 99998, 99999};
    int lens = 12;

    for (int i = 0;i < lens;i++) {
        printf("%02d's %5d = %d\n", i, ns[i], solution(ns[i]));
    }
}
~
