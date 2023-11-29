class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack=[]
        for i in strs:
            stack.append(len(i))
        
        
        ans=""
        k=strs[stack.index(min(stack))]
        print(strs)
        print(stack)
        print(k)
        for i in range(min(stack)):
            count=0
            for char in strs:
                if char[i] == k[i]:
                    count+=1
                else:
                    return ans
            if count == len(strs):
                ans+=char[i]
        return ans
            

            
      