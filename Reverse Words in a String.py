class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        stack=[]
        res=""
        for i in words:
            stack.append(i)
        while len(stack)!=0:
            res+=stack.pop()
            if len(stack)!=0:
                res+=" "
        return res
        




        
