// Online C++ compiler to run C++ program online
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void dfs(vector<vector<int>> &grid, vector<vector<int>> stack, int row, int col, int &result)
{
    int rows = grid.size();
    int cols = grid[0].size();

    if (row >= rows || col >= cols)
    {
        return;
    }

    if (row == rows - 1 && col == cols - 1)
    {
        int tmp = 0;
        for (auto var : stack)
        {
            tmp += grid[var[0]][var[1]];
        }

        if (tmp > result)
        {
            for (auto var : stack)
            {
                cout << var[0] << " " << var[1] << "\n";
            }
            result = tmp + grid[rows - 1][cols - 1];
        }

        return;
    }

    stack.push_back({row, col});

    dfs(grid, stack, row + 1, col, result);
    
    dfs(grid, stack, row, col + 1, result);
    if (!stack.empty())
    {
        stack.pop_back();
    }

    return;
}

int main()
{
    int result = -10000;
    vector<vector<int>> stack;
    vector<vector<int>> grid = {
        {1, 3, 6, 1},
        {2, 5, 9, 6},
        {4, 8, 5, 3},
        {0, 50, 2, 1}};

    dfs(grid, stack, 0, 0, result);

    cout << result;

    return 0;
}

/*

1, 3, 6, 1
2, 5, 9, 6
4, 8, 5, 3
0, 50, 2, 1

*/