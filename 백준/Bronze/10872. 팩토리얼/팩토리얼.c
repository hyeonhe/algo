#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int a, ans = 1;
    scanf("%d", &a);
    for (int i = 1; i <= a; i++) {
        ans *= i;

    }
    printf("%d", ans);

    return 0;
}