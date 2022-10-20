#Link: https://www.spoj.com/problems/AGGRCOW/
 
t=int(input())
while t:
    n,c=list(map(int,input().split()))
    x=[]
    for i in range(n):
        x.append(int(input()))

    def f(dist,pos1):
        i=0
        j=1
        ans=0
        while j<len(pos1):
            if pos1[j]-pos1[i]>=dist:
                # print(f"i {pos1[i]},j {pos1[j]}")
                ans+=1
                i=j
                j+=1      
            else:
                j+=1
        return ans+1
    def bsearch(pos,c):
        pos.sort()
        l=0
        h=pos[-1]-pos[0]
        while l<h:
            mid=l+(h-l+1)//2
            if f(mid,pos)>=c:
                l=mid
            else:
                h=mid-1
        return l
    if len(x)==0 or len(x)==1:
        print(0)
    else:
        print(bsearch(x,c))
    t-=1
                
    
