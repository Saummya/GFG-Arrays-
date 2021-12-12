A and B are good friend and programmers. They are always in a healthy competition with each other. They decide to judge the best among them by competing. They do so by comparing their three skills as per their values. Please help them doing so as they are busy.

Set for A are like [a1, a2, a3]
Set for B are like [b1, b2, b3]

Compare ith skill of A with ith skill of B
if a[i] > b[i] , A's score increases by 1
if a[i] < b[i] , B's score increases by 1
if a[i] = b[i] , nothing happens

 

Example 1:

Input : 
A = {4, 2, 7}
B = {5, 6, 3}
Output : 
1 2

Example 2:

Input : 
A = {4, 2, 7}
B = {5, 2, 8}
Output : 
0 2
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function scores() which takes the array A[], B[] as inputs and two reference variables ca and cb to store the final answer. Store the score of A in ca and score of B in cb.


Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

 SOLUTION:
 
 #User function Template for python3

class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
        
        
        for i in range(3):
            if a[i]>b[i]:
                cc[0]=cc[0]+1
            elif a[i]<b[i]:
                cc[1]=cc[1]+1
            
                
        return cc
 

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	a = [int(x) for x in input().strip().split()]
    	b = [int(x) for x in input().strip().split()]
    	
    	cc = [0, 0]
    	ob=Solution()
    	ob.scores(a, b, cc)
    	print(*cc)
    	
    	T -= 1

if __name__ == "__main__":
    main()







# } Driver Code Ends
