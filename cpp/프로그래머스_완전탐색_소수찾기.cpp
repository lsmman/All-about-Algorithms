#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <set>

using namespace std;
vector<int> result_nums;
void get_permutation(vector<int> nums, vector<bool> v, int range, int result)
{
    if (range == 0)
    {
        result_nums.push_back(result);
        return;
    }
    for (int i = 0; i < (int)nums.size(); i++)
    {
        if (!v[i])
        {
            v[i] = true;
            vector<bool> temp(v);
            get_permutation(nums, temp, range - 1, result * 10 + nums[i]);
            v[i] = false;
        }
    }
}
int solution(string numbers)
{
    int max_val = 0;
    vector<int> nums(numbers.size());
    for (int i = 0; i < (int)numbers.size(); i++)
    {
        nums[i] = numbers[i] - '0';
    }
    vector<bool> v((int)nums.size(), false);
    for (int i = 0; i < (int)nums.size(); i++)
    {
        get_permutation(nums, v, i + 1, 0);
    }
    max_val = *std::max_element(result_nums.begin(), result_nums.end());
    set<int> s(result_nums.begin(), result_nums.end());
    auto it = s.find(0);
    if (it != s.end())
    {
        s.erase(it);
    }
    it = s.find(1);
    if (it != s.end())
    {
        s.erase(it);
    }
    for (int pivot = 2; pivot <= (int)sqrt(max_val); pivot++)
    {
        for (int q = pivot * pivot; q <= max_val; q = q + pivot)
        {
            it = s.find(q);
            if (it != s.end())
            {
                s.erase(it);
            }
        }
    }
    return s.size();
}

int main()
{
    cout << solution("17"); //3
    return 0;
}