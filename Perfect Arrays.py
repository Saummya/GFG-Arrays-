## QUESTION

"""
Given an array of size N and you have to tell whether the array is perfect or not. An array is said to be perfect if it's reverse array matches the original array. If the array is perfect then print "PERFECT" else print "NOT PERFECT".

Example 1:

Input : Arr[] = {1, 2, 3, 2, 1}
Output : PERFECT
Explanation:
Here we can see we have [1, 2, 3, 2, 1] 
if we reverse it we can find [1, 2, 3, 2, 1]
which is the same as before.
So, the answer is PERFECT.

Example 2:

Input : Arr[] = {1, 2, 3, 4, 5}
Output : NOT PERFECT

User Task:
The task is to complete the function IsPerfect(), which takes an array (a), size of the array (n), and return the boolean value true if it Perfect else false. The drivercode automatically adds a new line.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
"""

## SOLUTION

#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        return arr==arr[: : -1]
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    if(ob.IsPerfect(arr,n)):
        print("PERFECT")
    else:
        print("NOT PERFECT")
    
# } Driver Code Ends
