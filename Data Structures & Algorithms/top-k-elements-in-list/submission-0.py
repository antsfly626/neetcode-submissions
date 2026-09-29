class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for i in nums:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1
        sorted_freqs = sorted(frequencies, key=frequencies.get, reverse=True)
        r = list(sorted_freqs)
        print(r)
        return r[:k]