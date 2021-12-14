#include <stdio.h>

void update(int *a,int *b) {
    // 3 2
    *a = *a + *b; // 5
    if (*a > *b) {
        *b = *a - *b; // 1
    } else {
        *b = *b - *a;
    }
    printf("%d %d", a, b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
