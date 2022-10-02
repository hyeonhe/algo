#include <stdio.h>
int main()
{
  int t, a, b, c;
  scanf("%d", &t);

  if(t % 10 != 0){
    printf("-1\n");
  }
  else{
    a = t / 300;
    b = (t % 300) / 60;
    c = ((t % 300) % 60) / 10;
    printf("%d %d %d", a, b, c); 
  }

  return 0;
}