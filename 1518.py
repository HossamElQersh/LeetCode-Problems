class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        z = (numBottles // numExchange)
        reminder = (numBottles % numExchange)
        result = numBottles + z
        if (reminder ) + z >= numExchange:
            result +=1
        return result





if '__main__' == __name__:
    obj = Solution()
    print(obj.numWaterBottles(9, 3))