**Company: SkyMavis**
# Requirements:
For a given array of integers, perform operations on the array.  
Return the result array after all operations havebeen applied in the ordern given.  
Each operation contains two indices. Reverse the subarray between those zero-based indices, inclusive.

## Example:
arr = [9,8,7,6,5,4,3,2,1,0]
operations = [[0,9],[4,5],[3,6],[2,7],[1,8],[0,9]]

| Operation     | Left          | To Reverse    | Right         | Result        |
| ------------- | ------------- | ------------- | ------------- | ------------- |
|  (0,9)        |  []           |  [9,8,7,6,5,4,3,2,1,0]  |  []        |  [0,1,2,3,**4,5**,6,7,8,9]  |
|  (4,5)        |  [0,1,2,3]    |  [4,5]                  |  [6,7,8,9] |  [0,1,2,3,**5,4**,6,7,8,9]  |
|  (3,6)        |  [0,1,2]      |  [3,5,4,6]              |  [7,8,9]   |  [0,1,2,**6,4,5,3**,7,8,9]  |
|  (2,7)        |  [0,1]        |  [2,6,4,5,3,7]          |  [8,9]     |  [0,1,**7,3,5,4,7,2**,8,9]  |
|  (1,8)        |  [0]          |  [1,7,3,5,4,7,2,8]      |  [9]       |  [0,**8,2,6,4,5,3,7,1,**9]  |
|  (0,9)        |  []           |  [0,8,2,6,4,5,3,7,1,9]  |  []        |  [**9,1,7,3,5,4,6,2,8,0**]  |

In the first operation, all elements are reversed. There are no elements to the right or left.  
In the second operation, only the elements in the "To Reverse" column are reversed.Those to the left and right remain the same.  
Similar logic is applied for further operations.

## Function Description
**The function has the following parameters:**  
*int arr[n]*: an array of integers  
*int operations[q][2]*: a 2-dimensionalarray of starting and ending indices

**Returns:**  
*int[n]*: the final arrayafter all operations have been performed

**Constraints:**  
1 <= n,q <= 10^3
0 <= arr[i] <= 10^3
0 <= operations[i][0] <= operations[i][1] < n
