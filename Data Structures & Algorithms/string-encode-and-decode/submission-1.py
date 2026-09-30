class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            s_len = len(s)
            res.append(f"{s_len}_")
            res.append(s)
        res = "".join(res)
        return(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  

        while i < len(s):
            delim_index = s.find("_", i)
            num = int(s[i:delim_index])
            start = delim_index+1
            end = num+start
            res.append(s[start:end])
            i = end

        return res