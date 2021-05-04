#include <stdio.h>
#define MAXN 30

int bottle1[10] = {0};
int bottle2[10] = {0};
char str1[MAXN];
char str2[MAXN];

void printS(char* s);
int toInt(char c);
int check();
int checkBottle();
int main(void) {
  scanf("%s", str1);

  if (check() == 1){
    printf("Yes\n");
  } else {
    printf("No\n");
  }
  printf("%s\n", str2);
  // printf("str1 = %s\n", str1);
  // printf("str2 = %s\n", str2);
  // printf("bottle1:\n");
  // for (int i = 0; i < 10; i++){
    // printf("%d ", bottle1[i]);
  // }
  // printf("bottle2:\n");
  // for (int i = 0; i < 10; i++){
    // printf("%d ", bottle2[i]);
  // }
  return 0;
}

int check(){
  int ret = 1;
  int len1 = 0;
  int len2 = 0;
  int begin = 0;
  int temp;
  while(str1[len1] != '\0'){
    temp = toInt(str1[len1]);
    if (temp < 10)
      bottle1[temp]++;
    len1++;
  }
  len2 = len1;
  if (toInt(str1[0]) >= 5){
    ret = 0;
    str2[0] = '1';
    len2++;
    begin = 1;
  } 
  str2[len2] = '\0';
  len2--;
  int shiwei = 0;
  int gewei = 0;
  for ( ; len2 >= begin; len2--){
    temp = toInt(str1[len2 - begin]);
    temp = temp * 2 + shiwei;
    shiwei = temp / 10;
    gewei = temp % 10;
    str2[len2] = gewei + '0';
  }

  len2 = 0;
  while(str2[len2] != '\0'){
    temp = toInt(str2[len2]);
    bottle2[temp]++;
    len2++;
  }
  if (!checkBottle())
    ret = 0;

  return ret;
}
int toInt(char c){
  return c - '0';
}
int checkBottle(){
  int ret = 1;
  for (int i = 0; i < 10; i++){
    if (bottle1[i] != bottle2[i]){
      ret = 0;
      break;
    }
  }

  return ret;
}
