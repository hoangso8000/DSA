m=int(input("nhap so hang cua ma tran: "))
n=int(input("nhap so cot cua ma tran: "))  
def qhd(i,j,mat,dp):
    if(i<0 or i>=m or j<0 or j>=n):
        return 0
    if(dp[i][j] !=-1):
        return dp[i][j]
    x,y,z,w=-1,-1,-1,-1 
    if(j<n-1 and ((mat[i][j]+1)==mat[i][j+1])):
        x=1+qhd(i,j+1,mat,dp)
    if(j>0 and (mat[i][j]+1==mat[i][j-1])):
        y=1+qhd(i-1,j,mat,dp)
    if(i>0 and (mat[i][j]+1==mat[i-1][j])):
        z=1+qhd(i+1,j,mat,dp)
    if(i<m-1 and (mat[i][j]+1==mat[i+1][j])):
        w=1+qhd(i+1,j,mat,dp)
    dp[i][j]=max(x,max(y,max(z,max(w,1))))
    return dp[i][j]
def longest(mat):
    result=1
    dp=[[-1 for i in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            if(dp[i][j]==-1):
                qhd(i,j,mat,dp)
            result=max(result,dp[i][j])
    return result
mat = [[1, 2, 3, 4 ],  
    [2, 2, 3, 4 ],  
    [3, 2, 3, 4 ],  
    [4, 5, 6, 7 ]] 
for i in range(m):
    mat.append(list(map(int,input().split())))
print(longest(mat))