#include <stdio.h>
int main()
{
  int x, y, w, h, min, a, b;
  scanf("%d %d %d %d", &x, &y, &w, &h);

  if(x > w-x){
    a = w-x;
  }
  else{
    a = x;
  }

  if(y > h-y){
    b = h-y;
  }
  else{
    b = y;
  }

  if(a > b){
    min = b;
  }
  else{
    min = a;
  }
  printf("%d", min);

  return 0;
}