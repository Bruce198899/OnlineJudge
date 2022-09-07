/*
输出一个整数序列中最大的数和最小的数的差。

输入格式
第一行为 M，表示整数个数，整数个数不会大于 10000；

第二行为 M 个整数，以空格隔开，每个整数的绝对值不会大于 10000。

输出格式
输出 M 个数中最大值和最小值的差。
*/

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
