#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int a;
    int b;
} Line;

int compare(const void *x, const void *y) {
    Line *l1 = (Line *)x;
    Line *l2 = (Line *)y;
    return l1->a - l2->a;
}

int main() {
    int n;
    scanf("%d", &n);

    Line arr[101];
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &arr[i].a, &arr[i].b);
    }

    // A 기준 정렬
    qsort(arr, n, sizeof(Line), compare);

    // LIS on B
    int dp[101];
    for (int i = 0; i < n; i++) dp[i] = 1;

    int max = 1;

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[j].b < arr[i].b) {
                if (dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                }
            }
        }
        if (max < dp[i]) max = dp[i];
    }

    printf("%d\n", n - max);

    return 0;
}