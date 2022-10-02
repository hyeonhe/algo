#include <stdio.h>
int main()
{
  int a, b, c, d;
  scanf("%d %d %d %d", &a, &b, &c, &d);
  
  int m, s;
  s = (a + b + c + d) % 60;
  m = (a + b + c + d) / 60;

  printf("%d\n%d", m, s);

  return 0;
}