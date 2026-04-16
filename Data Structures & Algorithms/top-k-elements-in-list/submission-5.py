import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_mapping={}
        for num in nums:
            freq_mapping[num]=freq_mapping.get(num,0)+1
        
        heap=[]
        for num, freq in freq_mapping.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)

        result=[num for freq,num in heap]

        return result