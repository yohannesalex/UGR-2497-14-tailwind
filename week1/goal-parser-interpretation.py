class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        l=0

        while l<len(command):
            if command[l] == "G":
                ans+='G'
                l+=1
            elif command[l] == "(" and command[l+1]==")":
                ans+="o"
                l+=2
            elif command[l]=="(" and command[l+1] == "a":
                ans+="al"
                l+=4
        return ans