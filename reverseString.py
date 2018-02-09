class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
  #      print (s[len(s)-1])
        new_list = ""
        for each in range(0,len(s)) :
            new_list  = new_list + s[len(s)-1 - each]
  #          print (new_list)
        return new_list
        
