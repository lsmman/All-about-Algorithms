#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int T = 0;
    int x, y, length, d = 0;
    int move_count = 0;
    
    scanf("%d", &T);
    for (int i = 0; i < T; i++){
        scanf("%d %d", &x, &y);
        length = y-x;
        
        d = sqrt(length);
        if (pow(d, 2) == length){
            move_count = 2*d - 1;
        }
        else if (pow(d, 2) + d >= length){
            move_count = 2*d;
        }
        else {
            move_count = 2*d+1;
        }
        cout << move_count << endl;
    }
}