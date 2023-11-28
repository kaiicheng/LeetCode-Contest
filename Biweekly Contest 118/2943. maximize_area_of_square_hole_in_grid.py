from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def getMax(ls):

            # max: count maximum of consecutive
            # c: count current consecutive
            cmax, c = 1, 1
            ls.sort()
            
            for i in range(1, len(ls)):
                if ls[i] == ls[i-1] + 1:
                    c += 1 
                else:
                    c = 1
                cmax = max(cmax, c)
            return cmax

        minmax = min(getMax(hBars), getMax(vBars))
        return (minmax + 1) ** 2
    

        # # Input:
        # # 2
        # # 4
        # # [3,2]
        # # [4,2]
        # # Output:
        # # 9
        # # Expected:
        # # 4
        
        # hBars.sort()
        # vBars.sort()
        # if len(hBars) == 1:
        #     height = 2
        # else:
        #     height = hBars[-1] - hBars[0] + 1
        # # for 2 in range(len)
            
        # if len(vBars) == 1:
        #     width = 2
        # else:
        #     width = vBars[-1] - vBars[0] + 1

        
            
        # span = max(height, width)
        # # print(span)
        # return span*span