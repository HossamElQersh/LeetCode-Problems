from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitTime = 0
        currentTime = customers[0][0]
        nOfCustomers = len(customers)
        for i in customers:
            if currentTime < i[0]:
                currentTime = i[0]
            currentTime += i[1]
            waitTime += currentTime - i[0]
        return waitTime / nOfCustomers
if __name__ == '__main__':
    s = Solution()
    print(s.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))