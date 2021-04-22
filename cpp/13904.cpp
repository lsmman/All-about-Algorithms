#include <iostream>
#include <array>

using namespace std;

int main()
{
    int i, j, d, w;
    int loop, temp;
    array<array<int, 2>, 1000> cases;
    array<int, 1001> score_pane;
    std::cin >> loop;
    for (i=0; i < loop; i++) {
        std::cin >> cases[i][0] >> cases[i][1];
    }

    for (i=0; i<loop; i++){
        d = cases[i][0];
        w = cases[i][1];
        if (score_pane[d] == 0){
            score_pane[d] = w;
        }
        else{
            for (j=i;j>0;j--){
                if (w > score_pane[j]){
                    temp = score_pane[j];
                    score_pane[j] = w;
                    w = temp;
                }
            }
        }
    }
    int sum=0;
    for (i=0;i<1001;i++){
        sum += score_pane[i];
    }
    return sum;
}