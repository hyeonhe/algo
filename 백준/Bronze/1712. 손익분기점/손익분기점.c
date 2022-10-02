#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
    unsigned int a, b, c;
    int count = 0;
    scanf("%d %d %d", &a, &b, &c);

    if (c <= b) 
        printf("-1");
    
    else {
        count = a / (c - b) + 1;
        printf("%d", count);
    }

    return 0;
}