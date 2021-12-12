#QUESTION
"""
Given an array Arr of N positive integers and a number K where K is used as a threshold value to divide each element of the array into sum of different numbers. Find the sum of count of the numbers in which array elements are divided.

Example 1:

Input:
N = 4, K = 3
Arr[] = {5, 8, 10, 13}
Output: 14
Explanation: Each number can be expressed as sum 
of different numbers less than or equal to K as
5 (3 + 2), 8 (3 + 3 + 2), 10 (3 + 3 + 3 + 1), 
13 (3 + 3 + 3 + 3 + 1). So, the sum of count 
of each element is (2+3+4+5)=14.

Example 2:

Input:
N = 5, K = 4
Arr[] = {10, 2, 3, 4, 7}
Output: 8
Explanation: Each number can be expressed as sum of
different numbers less than or equal to K as
10 (4 + 4 + 2), 2 (2), 3 (3), 4 (4) and 7 (4 + 3).
So, the sum of count of each element is 
(3 + 1 + 1 + 1 + 2) = 8.

Your Task:
You don't need to read input or print anything. Your task is to complete the function totalCount() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""
#SOLUTION
#User function Template for python3

class Solution:
    def totalCount(self, arr, n, k):
        # code here
        sum=0
        for i in range(n):
            if k>arr[i]:
                sum+=1
            else:
                if arr[i]%k==0:
                    q=arr[i]//k
                    sum+=q
                else:
                    q=arr[i]//k
                    sum+= q+1
        
        return sum
                
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.totalCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
