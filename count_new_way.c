/***
 2021/03/10 swhors@naver.com
 
 아래의 코드는 새로운 길의 수를 구하는 프로그램입니다.
 가로와 세로 10/10의 크기를 갖는 격자 무늬 공간에서 처음 가로 5와 세로 5의 위치에서
 시작하여, 주어지는 방향에 따라 이동하면서 새로운 길의 수를 새는 것입니다.
 
 즉, 갔던 길은 제외하고, 새로운 길만을 새는 코드입니다.
 ***/

#include <stdio.h>
#include <string.h>

/****

 Example :

  "ULURRDLLU"
  "LULLLLLLU"

 ****/

int solution(char *dirs) {
    int hpath[11][10];
    int vpath[10][11];

    int len = strlen(dirs);

    int count = 0;

    int startx = 5;
    int starty = 5;

    for(int i = 0;i < 11;i++) {
        memset(&hpath[i],0, sizeof(int)* 10);
    }


    for(int i = 0;i < 10;i++) {
        memset(&vpath[i],0, sizeof(int)* 11);
    }


    for (int i = 0;i < len;i++) {
       char dir = dirs[i];

       printf("%d's %c %d:%d %d:%d\n",
              i, dir, startx, starty,
              hpath[startx][starty],
              vpath[startx][starty]);

       switch(dir) {
           case 'U':
               if (starty < 9) {
                   starty += 1;
                   if (hpath[startx][starty] == 0){
                       hpath[startx][starty] = 1;
                       count++;
                   }
               }
               break;
           case 'D':
               if (starty > 0) {
                   starty -= 1;
                   if (hpath[startx][starty] == 0){
                       hpath[startx][starty] = 1;
                       count++;
                   }
               }
               break;
           case 'L':
               if (startx > 0) {
                   startx -= 1;
                   if (vpath[startx][starty] == 0){
                       vpath[startx][starty] = 1;
                       count++;
                   }
               }
               break;
           case 'R':
               if (startx < 9) {
                   startx += 1;
                   if (vpath[startx][starty] == 0){
                       vpath[startx][starty] = 1;
                       count++;
                   }
               }
           default:
               break;
       }
    }

    return count;
}

int main() {
    char * data1 = "ULURRDLLU";
    char * data2 = "LULLLLLU";
    printf("solution1 = %d\n", solution(data1));
    printf("solution2 = %d\n", solution(data2));
}
