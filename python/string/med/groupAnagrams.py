class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        
        # for i in strs:
        #     count = [0] * 26
        #     for s in i:
        #         count[ord(s.lower()) - ord('a')] += 1
        #     res[tuple(count)].append(i)
        # return res.values()
        
        
        d = {}
        for i in sorted(strs):
            ii = tuple(sorted(i))
            d[ii] = d.get(ii, []) + [i]
        return d.values()
            # use hashmap to classification