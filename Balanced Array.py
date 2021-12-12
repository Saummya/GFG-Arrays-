# QUESTION
"""
Given an array of even size N, task is to find minimum value that can be added to an element so that array become balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of right half.


Example 1:

Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 1
Explanation: 
Sum of first 2 elements is 1 + 5  = 6, 
Sum of last 2 elements is 3 + 2  = 5,
To make the array balanced you can add 1.

Example 2:

Input:
N = 6
arr[] = { 1, 2, 1, 2, 1, 3 }
Output: 2
Explanation:
Sum of first 3 elements is 1 + 2 + 1 = 4, 
Sum of last three elements is 2 + 1 + 3 = 6,
To make the array balanced you can add 2.
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function minValueToBalance() which takes the array a[] and N as inputs and returns the desired result.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

"""
#SOLUTION:
#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        #code here.
        mid=n//2
        sum1=0
        sum2=0
        for i in range(n):
            if i<mid:
                sum1+=a[i]
            else:
                sum2+=a[i]
        
        if sum1>sum2:
            d=sum1-sum2
        elif sum2>sum1:
            d=sum2-sum1
        else:
            return 0
            
        return d
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends
