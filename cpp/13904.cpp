#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool cmp(const pair<int, int> &v1, const pair<int, int> &v2)
{
    return v1.second > v2.second;
}

int main()
{
    int N, d, w, i;
    int answer(0), sum_v(0);
    vector<int> work(1001);
    vector<pair<int, int> > v;
    vector<std::pair<int, int> >::iterator vit;

    cin >> N;
    for (i = 0; i < N; i++)
    {
        cin >> d >> w;
        v.push_back(pair<int, int>(d, w));
    }

    sort(v.begin(), v.end(), cmp);
    for (vit = v.begin(); vit != v.end(); vit++)
    {
        for (i = vit->first; i > 0; i--)
        {
            if (vit->second > work[i])
            {
                work[i] = vit->second;
                break;
            }
        }
    }
    for (i = 0; i < 1001; i++)
    {
        sum_v += work[i];
    }
    cout << sum_v;
    return 0;
}