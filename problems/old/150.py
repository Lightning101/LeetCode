from collections import deque
class Solution:

    def isOpp(self,token):
        return token =='+' or token =='-' or token =='*' or token =='/'

    def runOpp(self,n1,n2,opp):
        if(opp == '+'):
            return n1 + n2
        elif(opp == '-'):
            return n1 -n2
        elif(opp == '*'):
            return n1 *n2
        else:
            return int(n1/n2)

    def evalRPN(self, tokens) -> int:
        st = deque()
         
        size = len(tokens)
        if(size==1):
            return int(tokens[0])
        
        for i in range(size):
            token = tokens[i]
            if(self.isOpp(token)):
                num1 = st.pop()
                num2 = st.pop()
                st.append(self.runOpp(num2,num1,token))
            else:
                st.append(int(token))   
        return st[-1]
        
        
    
s = Solution()
print(s.evalRPN(["4","13","5","/","+"])) 
print(s.evalRPN(["2","1","+","3","*"])) 
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) 
print(s.evalRPN(["3","11","+","5","-"])) 
