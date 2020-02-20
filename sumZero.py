import sys
import ast
class Solution:
	def twoSum(self,B,target):
	    left = 0
	    right = len(B) - 1
	    res = []
	    #print(B,target)
	    while left < right:
	        sumNum = B[left] + B[right]
	        if  sumNum == target:
	            res.append(B[left])
	            res.append(B[right])
	            return res
	        elif sumNum < target:
	            left+=1
	        else:
	            right-=1
	    return res
	def threeSum(self,A):
	    A.sort()
	    vecRes = []
	    for i in range(len(A)):
	        target = A[i]
	        res = self.twoSum(A[i + 1:],-target)
	        if len(res) > 0:
	            res.append(target)
	            vecRes.append(res) 
	            res = []
	    return vecRes
if __name__ == "__main__":
    arr1 = sys.argv[0]
    arr2 = sys.argv[1:]
    #print(arr2[0])
    input1 = ast.literal_eval(arr2[0])
    obj = Solution()
    print('All triplets summed 0 are: '+ str(obj.threeSum(input1)))	