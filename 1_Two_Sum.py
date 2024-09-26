class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                if nums[a]+nums[b]==target:
                    ans.append(a)
                    ans.append(b)
                    return ans
                    



            

