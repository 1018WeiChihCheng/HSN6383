import sys
import ast
class Solution:
    def find_Median(self,A,B):
        med1 = med2 = 0
        i = j = 0
        n = len(A) + len(B)
        if n == 0 :
            return 0
        
        if n == 1 and len(A) == 1: 
            return A[0]
        elif n == 1 and len(B) == 1: 
            return B[0]

        
        while((i + j) < (n / 2) + 1):
            if i < len(A) and j < len(B):
                med1 = med2
                if A[i] < B[j]:
                    med2 = A[i]
                    i+=1
                else:
                    med2 = B[j]
                    j+=1
            elif i < len(A):
                med1 = med2
                med2 = A[i]
                i+=1
            elif j < len(B):
                med1 = med2
                med2 = B[j]
                j+=1
        if n%2 == 0:
            return (med1 + med2) / 2.0
        else:
            return med1
if __name__ == "__main__":
    arr1 = sys.argv[0]
    arr2 = sys.argv[1:]
    input1 = ast.literal_eval(arr2[0])
    input2 = ast.literal_eval(arr2[1])
    obj = Solution()
    num = str(obj.find_Median(input1,input2))
    print('The median is '+ str(obj.find_Median(input1,input2)))
