#QUESTION
"""
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

 

Example 1:

Input:
N = 6
A[] = {3, 2, 1, 56, 10000, 167}
Output:
min = 1, max =  10000
 

Example 2:

Input:
N = 5
A[]  = {1, 345, 234, 21, 56789}
Output:
min = 1, max = 56789
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function getMinMax() which takes the array A[] and its size N as inputs and returns the minimum and maximum element of the array.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""
#SOLUTION
#User function Template for python3

def getMinMax( a, n):
    m1=[]
    max=a[0]
    for i in range(n):
        if max>a[i]:
            continue
        else:
            max=a[i]
            m1.append(max)
    
    
     
    min=a[0]
    for i in range(n):
        if min<a[i]:
            continue
        else:
            min=a[i]
            m1.append(min)
    return max, min
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[1], end=" ")
        print(product[0])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
