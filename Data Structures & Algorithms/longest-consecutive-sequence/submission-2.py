class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak,numset=0,set(nums)

        for num in nums:
            temp_streak=1
            if num-1 not in numset:
                while num+temp_streak in numset:
                    temp_streak+=1
            
            streak=max(streak,temp_streak)

        return streak
