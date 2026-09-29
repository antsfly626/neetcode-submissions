class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_arrs = {}
        for i, word in enumerate(strs):
            if str(sorted(word)) in sorted_arrs:
                sorted_arrs[str(sorted(word))].append(strs[i])
            else:
                sorted_arrs[str(sorted(word))] = [strs[i]]

        return (list(sorted_arrs.values()))