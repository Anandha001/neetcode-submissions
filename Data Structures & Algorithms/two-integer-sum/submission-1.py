class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_mapping={}
        for index,num in enumerate(nums):
            diff=target-num
            if diff in index_mapping:
                return [index_mapping[diff],index]
            index_mapping[num]=index
        