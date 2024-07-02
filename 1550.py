
from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<= 2:
            return False
        for i in range(0, len(arr) - 2 ):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False
if __name__ == '__main__':
    obj = Solution()
    print(obj.threeConsecutiveOdds([1,1,1]))