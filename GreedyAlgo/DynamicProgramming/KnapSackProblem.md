**Dynamic Programming**
* Start by solving smaller subproblems before solving bigger problems
---
**Typical Problem**: Knapsack problem 
- Take highest-value items within cost-constraints

| Item   | Cost  | Value |
|--------|-------|-------|
| Guitar | 1 lbs | $1.5k |
| Stereo | 4 lbs | $3k   |
| Laptop | 3 lbs | $2k   |
---
**Solution**

| Items/Weights |   1 lbs  |   2 lbs  |  3 lbs |    4 lbs   |
|:-------------:|:--------:|:--------:|:------:|:----------:|
|     Laptop    |     0    |     0    | 2k - L |   2k - L   |
|     Guitar    | 1.5k - G | 1.5k - G | 2k - L | 3.5k - G+L |
|     Stereo    | 1.5k - G | 1.5k - G | 2k - L | 3.5k - G+L |

* Work through the first row: take/not take, given that a bag can hold 1/2/3/4 lbs
* Formula for remaining rows: ```cell[i][j]``` = max (```cell[i-1][j]``` , ```currentItemValue + cell[i-1][j-currentItemCost]```) 
* The order of rows doesn't matter
---
**Notes**
* The subproblems don't depend on each other
* It is impossible to have more than 2 sub-knapsack
* It is possible for those sub-knapsack to have their own sub-knapsacks
* It is possible that the best solution doesn't fill the knapsack completely: Steal a $3 mil - 2.5lbs diamond and there is still 0.5lbs left that can't store anything more

