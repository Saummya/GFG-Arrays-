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
