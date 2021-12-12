#QUESTION
"""
Given a sorted array consisting 0’s and 1’s. The task is to find the index of first ‘1’ in the given array.

 

Example 1:

Input : 
arr[] = {0, 0, 0, 0, 0, 0, 1, 1, 1, 1}
Output : 
6
Explanation:
The index of first 1 in the array is 6.


Example 2:
Input : 
arr[] = {0, 0, 0, 0}
Output : 
-1
Explanation:
1's are not present in the array.
 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function firstIndex() which takes the array A[] and its size N as inputs and returns the index of first 1. If 1 is not present in the array then return -1.


Expected Time Complexity: O(Log (N))
Expected Auxiliary Space: O(1)
  """
#SOLUTION
#User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
    # Your code goes here
        arr.sort()
        for i in range(n):
            if arr[i]==1:
                return i
    
        return -1
    
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstIndex(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
