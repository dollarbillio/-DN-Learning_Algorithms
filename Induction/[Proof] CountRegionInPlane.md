# Counting regions in the Plane
---
* Lines are in general position (no parallel, no 3 lines join 1 point)
  * N = 1, regions = 2
  * N = 2, regions = 4
* Hypothesis: if there is one line added to n - 1 lines, then the regions increase by n
* Prove that: if there is one line added to n lines, then the regions increase by n + 1
---
### PROOF
* Know that a line go through each region will split that region in to 2 halves => x2 number of regions (to be added back)
* Take the **Nth** line away and assume that **(N+1)th** act as **Nth**
* **(N+1)th** line added to **[N-1]** lines => increase N regions (hypothesis)
* **(N+1)th** line added to **[N-1]** lines => increase [N-1] (containing R1_half region) + R2_half region 
* **Nth** without **(N+1)th** also increases [N-1] regions (containing a R3_half) + a half_R4 
* **Pay attention to R region**
* When **Nth** meets **(N+1)th** 
  * R is divided into 4 quarters
  * One_quarter_region can be considered to be a part of **+[N-1] regions** after adding back **Nth**
  * One quarter in the non-adding (can be considered to be a region already added in the previous [N-1] regions increase by **(N+1)th**
  * Two other quarters are parts of the R2_half region 
* Adding back **Nth** will make **(N+1)th** contributes: Increase **[N-1] regions** + 2 R2_quarters (parts of R2_half) => Increase **[N + 1] regions**

<p align="center">
  <img width="500" height="350" src="https://dobicode.files.wordpress.com/2018/10/plane.png">
</p
