# "101"
# "100"
# "0111"
# "0100001"
# "0100011"
# "0101011"
# "0101010101"
# "0100001"
# "0100011"

class Solution:
    def minimumSteps(self, s: str) -> int:
        
        print("-------Start-------")
        
        string=s
        ans=0
        left=0
        right=len(s)-1
        half_len=len(string)
        print("half length: ", half_len//2)
        
        # new_str=i
        
        for i in range(len(string)):
            # while left<=right:
            while left<right:
                # print("left: ", left)
                # print("right: ", right)
                # print("string[left]: ", string[left])
                # print("string[right]: ", string[right])

                if string[left]=="1" and string[right]=="0":
                    # print("In 1!")
                    # temp=string[left]
                    # string[left]=string[right]
                    # string[right]=temp

                    ans+=right-left
                    left+=1
                    right-=1
                elif string[right]=="1" and string[left]=="1":
                    # print("In 2!")
                    right-=1
                elif string[left]=="0" and string[right]=="1":
                    # print("In 3!")
                    left+=1
                elif string[right]=="0" and string[left]=="0":
                    # print("In 4!")
                    left+=1

#                 print("ans: ", ans)

#                 print("left: ", left)
#                 print("right: ", right)

#                 print("-------End of one iteration-------")

                # print("left: ", left)
                # print("right: ", right)

                # if left==right:
                #     print("ans: ", ans)
                #     return ans

                # if res[i]=="1":
                #     print("in 1")
                #     if res[i+1] != None and res[i+1] == 0:
                #         print("in 2")
                #         res[i+1]="1"
                #         res[i]=res[i+1]
                  
        print("ans: ", ans)
        return ans