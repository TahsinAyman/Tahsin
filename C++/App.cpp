#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int sorting(int, int, int, int);

int main() {

    int a, b, c, d;
    cin >> a >> b >> c >> d;

    cout << sorting(a, b, c, d);

    return 0;
}

int sorting(int a, int b, int c, int d) {
    int max = 0;

    if (a > max) {
        max = a;
    }
    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }
    if (d > max) {
        max = d;
    }
    return max;
}
