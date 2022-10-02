#include <stdio.h>
int main()
{
  int data1, data2, math1, math2, sci1, sci2, eng1, eng2;
  scanf("%d %d %d %d", &data1, &math1, &sci1, &eng1);
  scanf("%d %d %d %d", &data2, &math2, &sci2, &eng2);
  
  int sum1 = data1 + math1 + sci1 + eng1;
  int sum2 = data2 + math2 + sci2 + eng2;

  if(sum1 >= sum2)
  printf("%d", sum1);
  else
  printf("%d", sum2);

  return 0;
}