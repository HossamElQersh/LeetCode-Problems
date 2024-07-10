from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            if '..' in log and level != 0:
                level -= 1
            elif '.' in log:
                continue
            else:
                level += 1
        return level
if __name__ == '__main__':
    solution = Solution()
    print(solution.minOperations(["d1/","../","../","../"]))