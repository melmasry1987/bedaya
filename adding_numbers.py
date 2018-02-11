class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while True:   
            x = 0
            if num < 10 : 
                break
            print("Masry is adding %s"%num)
            for i in range(0,len(str(num))):
                print("num  %s"%num)
                print(x)
                str_num = str(num)  
                x= int(str_num[i])+ x
            num = x 
            #    print(num)
            print(x)
        return num 
