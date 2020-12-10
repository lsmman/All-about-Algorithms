#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool is_right(vector<int> pattern, int i, int ans)
{
    return pattern[(i % pattern.size())] == ans;
}

vector<int> solution(vector<int> answers)
{
    int ans, max_score;
    vector<int> answer;
    vector<int> scores(4);

    vector<int> first_p = {1, 2, 3, 4, 5};
    vector<int> second_p = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> third_p = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    for (int i = 0; i < answers.size(); i++)
    {
        ans = answers[i];
        if (is_right(first_p, i, ans))
        {
            scores[1]++;
        }
        if (is_right(second_p, i, ans))
        {
            scores[2]++;
        }
        if (is_right(third_p, i, ans))
        {
            scores[3]++;
        }
    }

    max_score = *max_element(scores.begin(), scores.end());
    for (int i = 0; i < scores.size(); i++)
    {
        if (scores[i] == max_score)
        {
            answer.push_back(i);
        }
    }
    return answer;
}