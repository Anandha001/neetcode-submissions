class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele_first_freq_mapping={}
        for num in nums:
            ele_first_freq_mapping[num]=ele_first_freq_mapping.get(num,0)+1

        count_first_freq_mapping=[]
        for num,freq in ele_first_freq_mapping.items():
            count_first_freq_mapping.append([freq,num])

        count_first_freq_mapping.sort()

        result=[]
        while len(result)<k:
            result.append(count_first_freq_mapping.pop()[1])

        return result

        