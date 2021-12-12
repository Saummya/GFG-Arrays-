#QUESTION
"""
Given an array of N integers. Write a program to check whether an arithmetic progression can be formed using all the given elements. 
 

Example 1:

Input:
N=4
arr[] = { 0,12,4,8 }
Output: YES
Explanation: Rearrange given array as
{0, 4, 8, 12}  which forms an
arithmetic progression.
Example 2:

Input:
N=4
arr[] = {12, 40, 11, 20}
Output: NO
 

Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function checkIsAP() that takes array arr and integer N as parameters and return true for "Yes" and false for "No".

 

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(1).

 
 """
#SOLUTION:
#User function Template for python3


class Solution:
    
    def checkIsAP(self, arr, n):
        # code here
        arr.sort()
        
        c1=arr[1]-arr[0]
        for i in range(n-1):
            if arr[i+1]-arr[i]!=c1 :
                return False
            
        return True
        
        
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    # l=list(map(int,input().split()))
    # n=l[0]
    # x=l[1]
    # y=l[2]
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.checkIsAP(a,n)
    if(ans==True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends
