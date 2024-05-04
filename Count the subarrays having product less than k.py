class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        
        i=0
        j=0
        product=1
        ans=0
        while i<n:
            product *= a[i]
            while j<= i and product>=k:
                product /=a[j]
                j+=1
            ans += (i-j+1)
            i+=1
        return ans 