/****
 2021/03/11 swhors@naver.com
 
 동일한 크기의 직각삼각형이 주어 진 경우에, 가로와 세로의 길이를 1로 할 경우에 
 얻을 수 있는 사각형의 수를 구하라.
 
   | | | | |
   |     | |
   |   |   |
   | |     |
   | | | | | w = 4 h = 5 인 경우, 6 * 2 = 12
   
 ****/

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int w, int h) {
    long long answer = 0;
    float ratio = (float)h/(float)w;
    for (int i = w-1; i >= 1; i--) {
        answer += (int)(ratio * i);
    }
    return answer * 2;
}

int main() {
    printf("1 = 8,12 %lli\n", solution(8,12));
    printf("2 = 4,4  %lli\n", solution(4,4));
    printf("3 = 4,4  %lli\n", solution(4,4));  
    printf("4 = 4,8  %lli\n", solution(4,8));
    printf("5 = 10,4 %lli\n", solution(10,4));
    printf("6 = 4,10 %lli\n", solution(4,10));
    printf("7 = 1,1  %lli\n", solution(1,1));
}
