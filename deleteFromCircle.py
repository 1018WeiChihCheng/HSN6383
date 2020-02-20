import sys
import ast
class Solution:
    def Elimination(self,n,m,k):
        A = list(range(n))
        startIdx = 0
        currLen = n
        while len(A) > k:
            delIdx = (startIdx + currLen - m + 1) % currLen
            #print('delIdx',delIdx)
            A.pop(delIdx)
            currLen = len(A)
            startIdx = (delIdx + currLen - 1) % currLen
            #print(A)
        return A
if __name__ == "__main__":
    arr1 = sys.argv[0]
    arr2 = sys.argv[1:]
    # print(arr2[0])
    # print(arr2[1])
    # print(arr2[2])
    n = int(arr2[0])
    m = int(arr2[1])
    k = int(arr2[2])
    obj = Solution()
    print('The last four numbers remaining are '+ str(obj.Elimination(n,m,k)))