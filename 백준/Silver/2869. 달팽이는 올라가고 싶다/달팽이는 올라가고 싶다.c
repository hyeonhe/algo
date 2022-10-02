#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
    int A, B, V, day = 0;
    scanf("%d %d %d", &A, &B, &V);

    if ((V - A) % (A - B) == 0) {
        day = (V - A) / (A - B) + 1;
        printf("%d", day);
    }
    else {
        day = (V - A) / (A - B) + 2;
        printf("%d", day);
    }
    

    return 0;
}