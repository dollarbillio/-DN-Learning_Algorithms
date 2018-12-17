**Problem**
* Given a word and a bag of words, find the word that has the most number of similar letters at the same place as the given word
---
**Solution**
* Make a grid

| TwoWords | B | L | U | E |
|:--------:|:-:|:-:|:-:|:-:|
|     T    | 0 | 0 | 0 | 0 |
|     R    | 0 | 0 | 0 | 0 |
|     U    | 0 | 0 | 1 | 1 |
|     E    | 0 | 0 | 1 | 2 |

* Code:
```py
if word1[i] == word1[j]:
  // similar to longest common substring
  cell[i][j] = cell[i-1][j-1] + 1
else:
  '''
  Still keep track of number of similarities between 
  two words even the substring discontinue
  '''
  cell[i][j] = max(cell[i-1][j] , cell[i][j-1]))

```
