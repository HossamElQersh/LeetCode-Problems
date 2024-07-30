class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = [0] * len(s)
        for i in range(len(s)-2 , -1 , -1):
            a_count[i] = a_count[i + 1]
            if s[i + 1] == 'a':
                a_count[i] +=1
            else:
                pass
        b_count = 0
        res = len(s)
        for i, c in enumerate(s):
            deletions = b_count + a_count[i]
            res = min(res, deletions)
            if c=='b':
                b_count += 1
        return res





if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumDeletions("aababbab"))