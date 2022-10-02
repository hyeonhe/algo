#include <stdio.h>
int main()
{
  int n, t, c, p, money;
  scanf("%d %d %d %d", &n, &t, &c, &p);
  if(n % t == 0)
    money = (n / t - 1) * c * p;
  else
    money = n / t * c * p;
  printf("%d", money);
}