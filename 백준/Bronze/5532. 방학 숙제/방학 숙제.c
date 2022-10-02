#include <stdio.h>
int main()
{
  int l, a, b, c, d;
  scanf("%d\n%d\n%d\n%d\n%d", &l, &a, &b, &c, &d);
  
  int kor, math;
  if(a % c == 0){
    kor = a / c;
  }
  else{
    kor = a / c + 1;
  }
  
  if(b % d == 0){
    math = b / d;
  }
  else{
    math = b / d + 1;
  }
  
  int day;
  if(kor > math){
    day = l - kor;
  }
  else
    day = l - math;
  
  printf("%d", day);
  
  return 0;
}
