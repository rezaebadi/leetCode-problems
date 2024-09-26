class Solution:
    def has_repeated(self,s:str):
        if len(''.join(set(s)))!=len(s):
            return True
        return False
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        ans=s[0]
        for a in range(0,len(s)):
            for b in range(a+1,len(s)):
                sub_string=s[a:b]
                res=self.has_repeated(sub_string) 
                if res is False and len(ans)<=len(sub_string):
                    ans=sub_string
        return(len(ans))
                
sol=Solution()
print(sol.lengthOfLongestSubstring(s="au"))