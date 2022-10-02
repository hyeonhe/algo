#include <stdio.h>

int main()
{
  int N, time, sumY = 0, sumM = 0;
  int moneyY = 10;
  int mnneyM = 15;

  scanf("%d", &N);
  for(int i = 0; i < N; i++){
    scanf("%d", &time);
    sumY += (time / 30 + 1) * 10;
    sumM += (time / 60 + 1) * 15; 
  }

  if(sumY < sumM)
    printf("Y %d", sumY);
  else if(sumM < sumY)
    printf("M %d", sumM);
  else
    printf("Y M %d", sumY);

  return 0;
}