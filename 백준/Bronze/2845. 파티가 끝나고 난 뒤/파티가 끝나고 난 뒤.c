#include <stdio.h>

int main()
{
    int l, p, m, y;

    scanf("%d %d", &l, &p);
    m = l * p;

    for(int i = 0; i < 5; i++){
      scanf("%d", &y);
      printf("%d ", y-m);
    }

    return 0;
}
