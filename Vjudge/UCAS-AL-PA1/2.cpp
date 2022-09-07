#include <iostream>

using namespace std;

int main() {
    int M, max = -10000, min = 100000;
    int t;
    cin >> M;
    for (M; M > 0; M--) {
        cin >> t;
        max = t > max ? t : max;
        min = t < min ? t : min;
    }
    cout << max - min;
}
