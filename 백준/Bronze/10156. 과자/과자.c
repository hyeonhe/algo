#include <stdio.h>
int main()
{
  int k, n, m, mother;
  scanf("%d %d %d", &k, &n, &m);

  mother = m - k * n  > 0 ? 0 : k * n - m;
  
  printf("%d", mother);
  
  return 0;
}