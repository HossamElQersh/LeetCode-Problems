from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
            res = []
            filtered = []
            for row in matrix:
                pair = [min(row),max(row)]
                filtered.append(pair)
            print(filtered)

if __name__ == '__main__':
    sol = Solution()
    sol.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])