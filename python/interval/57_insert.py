class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res+ intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        
        return res

        # 2种情况:
        #     1. newinterval和intervals无交集。直接加到头或尾。
        #         1. 头 --> 直接Return
        #         2. 尾部 --> 继续和下一个intervals进行比较。
        #     2. 有交集。头取min，尾取max。继续遍历。
            
    