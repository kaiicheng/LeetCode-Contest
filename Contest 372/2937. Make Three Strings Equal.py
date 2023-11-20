class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
        # "abc", "abb", "ab"
        # "dac", "bac", "cac"
        # "aca", "abcc", "accba"
        
        step=0
        inp=[s1, s2, s3]
        
        # border case
        if s1[0]!=s2[0] or s2[0]!=s3[0] or s3[0]!=s1[0]:
            return -1
        if s1 == s2 and s2 == s3 and s3:
            return 0
        
        ls=[[len(s1), 1], [len(s2), 2], [len(s3), 3]]
        ls.sort()
        # print(ls)  # [[2, 3], [3, 1], [3, 2]]
    
        short=inp[ls[0][1]-1]
        med=inp[ls[1][1]-1]
        long=inp[ls[2][1]-1]
        
        # [[3, 1], [4, 2], [5, 3]]
        # aca abcc accba
        # print(short, med, long)
        
        gap_1=0
        gap_2=0
        
        if len(long) - len(short) > 0:
            gap_1=len(long) - len(short)  # 2
            print("gap_1: ", gap_1)
        
        if len(med) - len(short) > 0:
            gap_2=len(med) - len(short)  # 1
            print("gap_2: ", gap_2)
        
        # print("step:", step)

        # # s1, s2, s3 has same length
        # if gap_1 is None:
        #     while long != short and long != med and med != short:
        #         long = long[:-1]
        #         med = med[:-1]
        #         short = short[:-1]
        #         step+=3
        #     return step
        # # s1, s3 has different length
        # else:
            
            # print(short, med, long)

        # trim the longest length to the shortest length
        long = long[:len(long)-gap_1]
        step+=gap_1
        print("long: ", long) # acc

        # # s1, s2 has different length
        # if gap_2 is not None:
        med = med[:len(med)-gap_2]
        step+=gap_2
        print("med: ", med) # abc

        print("short: ", short)
        
        print("step:", step)

        while long != short or long != med or med != short:
        # while long != short and long != med and med != short:
            long = long[:len(long)-1]
            med = med[:len(med)-1]
            short = short[:len(short)-1]
            step+=3
            print("long: ", long)
            print("med: ", med)
            print("short: ", short)
            print("step:", step)
        return step

        # for i in range(1, max(len(s1), len(s2), len(s3))+1):
        # while s1!=s2 and s2!=s3 and s3!=s1:
            # if s1[i]!=s2[i] or s2[i]!=s3[i] or s3[i]!=s1[i]:
            
        # print(s1, s2, s3)
        # print(max(len(s1), len(s2), len(s3)))
        # print(max(len(s3), 0))
