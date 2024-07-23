from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashTabe = {}
        for i in range(len(names)):
            hashTabe[heights[i]] = names[i]
        sortedNames = sorted(hashTabe.items())
        res = []
        for name in sortedNames[::-1]:
            res.append(name[1])

        return res
if __name__ == '__main__':
    obj = Solution()
    names = ["Alice","Bob","Bob"]
    heights = [155,185,150]
    print(obj.sortPeople(names, heights))