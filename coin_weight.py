#có n đồng xu nặng w1,w2,...kg ---> tìm số lượng đồng xu bé nhất để tổng khối lượng của chúng bằng S
def coinWeight():
    n, S = map(int, input().split())
    w = list(map(int, input().split()))
    dp = [0] * (S + 1)
    dp[0] = 0
    
    for P in range(1, S + 1):
        dp[P] = min(dp[P - x] for x in w if x <= P) + 1
    
    print(dp)
    print(dp[S])
#Xâu con chung dài nhất
def longestSubString(): 
    n1, n2 = map(int, input().split())
    s1, s2 = input().split()
    t = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i, x1 in enumerate(s1, 1):
        for j, x2 in enumerate(s2, 1):
            if x1 == x2:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])
    
    print(t[-1][-1])
longestSubString()