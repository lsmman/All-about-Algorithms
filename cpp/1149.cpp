// RGB 거리 
// https://www.acmicpc.net/problem/1149

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int loop = 0;
    int cases[1001][3] = {0, };
    int d[1001][3] = {0, };

    std::cin >> loop;
    for (int i=1; i <= loop; i++) {
        std::cin >> cases[i][0] >> cases[i][1]>> cases[i][2];
    }
    for (int i = 1; i <= loop; i++) {
        d[i][0] = min(d[i-1][1], d[i-1][2]) + cases[i][0];
        d[i][1] = min(d[i-1][0], d[i-1][2]) + cases[i][1];
        d[i][2] = min(d[i-1][0], d[i-1][1]) + cases[i][2];
    }
    std::cout << std::min(d[loop][0], min(d[loop][1], d[loop][2])) << std::endl;
    return 0;
}
