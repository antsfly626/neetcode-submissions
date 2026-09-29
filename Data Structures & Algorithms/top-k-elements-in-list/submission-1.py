class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for i in nums:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        
        buckets = [[] for i in range (len(nums)+1)]

        for val, freq in frequencies.items():
            buckets[freq].append(val)
        res = []
        buckets.reverse()
        for bucket in buckets:
                
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res

            
        return (res)


            