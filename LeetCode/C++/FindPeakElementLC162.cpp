#include <vector>

using namespace std;

int findPeakElement(vector<int> &nums)
{
    int s = 0;
    int n = nums.size() - 1;

    while (s < n)
    {
        int mid = s + (n - s) / 2;
        if (nums[mid] < nums[mid + 1])
        {
            s = mid + 1;
        }
        else
        {
            n = mid;
        }
    }

    return s;
}