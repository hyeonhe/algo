#include <stdio.h>
int main()
{
  int a, b, c, d, e, f;
  scanf("%d\n%d", &a, &b);
  int b1= b % 10;
  int b10 = (b / 10) % 10;
  int b100 = b / 100;
  c = a * b1;
  d = a * b10;
  e = a * b100;
  f = a * b;
  printf("%d\n", c);
  printf("%d\n", d);
  printf("%d\n", e);
  printf("%d\n", f);

  return 0;
}