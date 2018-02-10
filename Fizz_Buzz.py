class Solution:
    

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """        
        List = [] 
        for num in range (1,n+1):
            if ((num % 3 == 0 ) and (num % 5 == 0)):
                List.append("FizzBuzz") 
                
            elif num % 3 == 0 :
                List.append("Fizz") 
            elif num % 5 == 0 :
                List.append("Buzz") 
            else :
                List.append(str(num))              
        return (List)
            
            
        
