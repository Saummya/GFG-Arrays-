## QUESTION
"""
Given an array Arr of size N, swap the Kth element from beginning with Kth element from end.

Example 1:

Input:
N = 8, K = 3
Arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: 1 2 6 4 5 3 7 8
Explanation: Kth element from beginning is
3 and from end is 6.
Example 2:

Input:
N = 5, K = 2
Arr[] = {5, 3, 6, 1, 2}
Output: 5 1 6 3 2
Explanation: Kth element from beginning is
3 and from end is 1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function swapKth() which takes the array of integers arr, n and k as parameters and returns void. You have to modify the array itself.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
"""

## SOLUTION:

#User function Template for python3
class Solution:
	
	def swapKth(self,arr, n, k):
		# code here
		
		start1=k+1
		end1=n-k
		
		temp=arr[k-1]
		arr[k-1]=arr[n-k]
		arr[n-k]=temp
		
		return arr
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.swapKth(arr, n, k)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
