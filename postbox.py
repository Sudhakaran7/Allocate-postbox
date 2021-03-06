class Solution(object):
    def minDistance(self, houses, k):
        def cost(prefix, i, j):
            return (prefix[j+1]-prefix[(i+j+1)//2])-(prefix[(i+j)//2+1]-prefix[i])
        houses.sort()
        prefix = [0]*(len(houses)+1)
        for i, h in enumerate(houses):
            prefix[i+1] = prefix[i]+h
        dp = [cost(prefix, 0, j) for j in range(len(houses))]
        for m in range(1, k):
            for j in reversed(range(m, len(houses))):
                for i in range(m, j+1):
                    dp[j] = min(dp[j], dp[i-1]+cost(prefix, i, j))
        return dp[-1]
val=Solution()
n,k,=map(int,input().split())
arr=list(map(int,input().split()))
print(val.minDistance(arr,k))
