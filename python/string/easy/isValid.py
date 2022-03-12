from stringprep import map_table_b2

from numpy import False_


class Solution:
    def isValid(self, s: str) -> bool:
        # hashmap + stack --> 将括号作为hashmap
        # 遍历字符串
        # 判断是否为value
        # 是--> 保存value 不是--> 判断是否是key
        # > 如果是，再判断key是否对应map
        # > 不是，返回False
        
        stack = []
        closep = { ")":"(", "}":"{" , "]":"["}
        for c in s:
            if c in closep:
                temp = closep[c]
                # save times for not repeating calulate the hashmap
                if stack and stack[-1] == temp:
                    # stack.pop()
                    del stack[-1]
                else:
                    return False
            else:
                stack.append(c)
        # return True if not stack else False
        # return len(stack) == 0
        return stack == []
