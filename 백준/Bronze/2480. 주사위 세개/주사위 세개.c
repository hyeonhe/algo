#include <stdio.h>
int main()
{
  int a, b, c, money;
  scanf("%d %d %d", &a, &b, &c);
  if(a==b && b==c){
    money = 10000 + a * 1000;
  }
  else if(a == b || b == c || c == a){
    if(a==b)
      money = 1000 + a * 100;
    else if(b==c)
      money = 1000 + b * 100;
    else
      money = 1000 + c * 100;
  }
  else{
    if((a>b && b>c) || (a>c && c>b))
      money = a * 100;
    else if((b>a && a>c) || (b>c && c>a))
      money = b * 100;
    else
      money = c * 100;
  }
  printf("%d", money);
  return 0;
}