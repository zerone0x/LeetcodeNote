class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        # sort的key 通过lambda 设置条件来排序
        out = [intervals[0]]
        # out初始化 --> 第一个interval
        for start, end in intervals[1:]:
            if out[-1][1] < start:
                out.append(start, end)
            else:
                out[-1, 1] = max(out[-1][1], end)
        return out
    
    # 条件是比较第一个序列的尾和下一个的头
    #med
    #整体算简单。用到了sort 的 key