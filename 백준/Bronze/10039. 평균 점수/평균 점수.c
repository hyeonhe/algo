#include <stdio.h>
int main()
{
  int a, b, c, d, e;
  scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
  a = a < 40 ? 40 : a;
  b = b < 40 ? 40 : b;
  c = c < 40 ? 40 : c;
  d = d < 40 ? 40 : d;  
  e = e < 40 ? 40 : e;

  printf("%d", (a + b + c + d + e) / 5);
  return 0;
}