import sys
import ast
class Solution:
	def Anagrams(self,A):
	    res = []
	    dict1 = {}
	    for i in A:
	        currStr = i
	        currStr = ''.join(sorted(currStr))
	        if currStr not in dict1:
	            dict1[currStr] = [i]
	        else:
	            dict1[currStr].append(i)
	    for k,v in dict1.items():
	        res.append(v)
	    return res
if __name__ == "__main__":
    arr1 = sys.argv[0]
    arr2 = sys.argv[1:]
    arr_ = list(map(str,arr2[0].strip('[]').split(',')))
    obj = Solution()
    print('Anagram groups are: '+ str(obj.Anagrams(arr_)))	
