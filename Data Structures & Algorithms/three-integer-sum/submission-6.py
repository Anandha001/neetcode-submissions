class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if nums[i-1]==nums[i] and i>0:
                continue

            l,r=i+1,len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    l,r=l+1,r-1
                    while l<r and nums[l]==nums[l-1] :
                        l+=1

                
        
        return result


        