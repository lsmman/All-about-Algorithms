// 1, 2, 3 더하기
// https://www.acmicpc.net/problem/9095

#include <iostream>
#include <algorithm>
#include <array>

using namespace std;

int main()
{
    int loop;
    array<int, 11> cases;
    std::cin >> loop;
    for (int i=0; i < loop; i++) {
        std::cin >> cases[i];
    }
    int max_val = *max_element(cases.begin(), &cases[loop]);
    int m = max_val + 1;
    int arr[m];
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;
    for (int i = 4; i < m; i++) arr[i] = arr[i-1] + arr[i-2] + arr[i-3];
    for (int i=0; i < loop; i++) std::cout << arr[cases[i]] << std::endl;
    
    return 0;
}

    
    // 1 1
    // 2 2
    // 3 4
    // 4 7
    // 5 13
    // 6 24
    // 7 44
    // // 
    // 1+1+1+1+1
    // 1+1+1+2
    // 2+1+1+1
    // 1+2+1+1 
    // 1+1+2+1
    // 2+2+1
    // 2+1+2
    // 1+2+2
    // 3+2
    // 2+3
    // 3+1+1
    // 1+3+1
    // 1+1+3
    // // 
    // 1+1+1+1+1+1 - 1
    // 1+1+1+1+2 - 5 
    // 2+2+2 - 1
    // 2+2+1+1 - 6
    // 3+2+1 - 6
    // 3+1+1+1 - 4
    // 3+3 - 1
    
    