class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long_seq=0
        for num in set(nums):
            if num-1 not in nums:
                temp_long_seq = 1
                while num + temp_long_seq in nums:
                    temp_long_seq+=1
                long_seq = max(temp_long_seq, long_seq)
        return long_seq


        