from sys import maxint 
def maxSubArraySum(a,size): 
       
    max_so_far = -maxint - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        print(11, i, max_ending_here)
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
        
        print(22, i, max_so_far)
  
        if max_ending_here < 0: 
            max_ending_here = 0   
        print(33, i, max_ending_here)
    return max_so_far 
   
# Driver function to check the above function  
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))