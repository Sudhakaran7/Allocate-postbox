Given the list of houses and an integer k. where houses[i] is the location of the ith house along a street, your task is to allocate k postboxes in the street.
Return the minimum total distance between each house and its nearest postbox.
Note:The answer is guaranteed to fit in a 32-bit signed integer.
https://assets.leetcode.com/uploads/2020/05/07/sample_11_1816.png

Input Description:
First line contains, n,k. n is the size of the house lists.
Second line contains, n elements of integers in a single line.

Output Description:
Print the minimum total distance between each house and its nearest postbox.

Sample Input:
5 3
1 4 8 10 20

Sample Output:
5

Explanation:
Allocate postboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest postboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 

Sample Input:
6 2
2 4 6 8 10 12

Sample Output:
8

Sample Input:
4 3
12 45 78

Sample Output:
0

Sample Input:
6 2
33 44 55 66 77 88

Sample Output:
44

Sample Input:
7 1
1 2 3 4 5 6 7

Sample Output:
12

Sample Input:
8 4
33 45 67 82 34 12

Sample Output:
12
