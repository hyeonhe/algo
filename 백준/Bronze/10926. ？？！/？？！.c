#include <stdio.h>
#include <string.h>
int main()
{
  char a[51], b[4] = "\?\?!";
  scanf("%s", a);
  strcat(a, b);

  printf("%s\n", a);
  return 0;
}