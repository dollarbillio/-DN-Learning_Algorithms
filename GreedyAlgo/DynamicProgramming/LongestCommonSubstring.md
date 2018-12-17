**Problem**
* Given a word and a bag of words, find the one that has the longest common substring with the given word
---
**Solution**
* Make a grid again

| TwoWords | H | I | S | H |
|:--------:|:-:|:-:|:-:|:-:|
|     F    | 0 | 0 | 0 | 0 |
|     I    | 0 | 1 | 0 | 0 |
|     S    | 0 | 0 | 2 | 0 |
|     H    | 0 | 0 | 0 | 3 |

* Pseudocode:
```py
if word1[i] == word2[j]:
  cell[i][j] = cell[i-1][j-1]
else:
  cell[i][j] = 0
```
