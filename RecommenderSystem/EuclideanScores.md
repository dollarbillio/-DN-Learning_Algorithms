# Pearson Correlation
---
* Using Pearson Correlation Covar(x, y) / (std(y) * std(x))
* Beta slope: Covar(x,y) / Var(x)
* Compare 2 people at a time, using only 2D axes to represent 2 people
* Correlation =  nominator = n(∑xy) - (∑x)(∑y) / 
    * denominator = sqrt([(∑ x^2) - (∑x)^2][(∑y^2) - (∑y)^2])
    * nominator = (∑xy) - (∑x)(∑y)
---
```python
from math import sqrt

def pearson_corrcoef(data, p1, p2):
    """Return the value of PEARSON Corr_coeff"""
	
    # Determine shared_items
    shared_items = {}
    for item in data[p1]:
        if item in data[p2]:
            shared_items[item] = 1
    # If there is no similar items between them
    n = len(shared_items)
    if n == 0:
        return 0
	
    # (∑x) and (∑y) related
    sum1 = sum([data[p1][item] for item in shared_items])
    sum2 = sum([data[p2][item] for item in shared_items])
	
    # (∑xy)
    sum_product = sum([data[p1][item] * data[p2][item] for item in shared_items])
	
    (∑ x^2) and (∑ y^2)
    sumSq1 = sum([pow(data[p1][item], 2) for item in shared_items])
    sumSq2 = sum([pow(data[p2][item], 2) for item in shared_items])
	
    # Formula with each denom and nom multiplied by n
    nom =  sum_product - sum1 * sum2 / n
    denom = sqrt((sumSq1 - pow(sum1, 2) / n) * (sumSq2 - pow(sum2, 2) / n))
	
    return nom/demon
```
