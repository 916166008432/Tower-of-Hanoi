def solve(n,A,B,C,cnt):
    if n==1:
        cnt[0]=cnt[0]+1
        return cnt
    solve(n-1,A,C,B,cnt)
    solve(1,A,B,C,cnt)
    solve(n-1,B,A,C,cnt)
            
def  towerOfHanoi(n, fromm, to, aux):
        # code here
    cnt=[0]
    solve(n,fromm,to,aux,cnt)
    return cnt[0]
n=list(map(int,input().split()))
print(towerOfHanoi(n))