class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i in range(len(words)):
            # print("i: ", i)
            # print("words[i]: ", words[i])
            if x in words[i]:
                ans.append(i)
        # print(ans)
        return ans
