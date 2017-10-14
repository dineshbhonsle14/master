import unittest
from collections import defaultdict
def isstringsame(string1,string2):
   if len(string1) != len(string2):
      return False
   d1=defaultdict(int)
   
   for letter in string1:
      d1[letter]+=1
   print d1
   for letter in string2:
      d1[letter]-=1
   print d1
   for v in d1.values():
       if  v!=0 :
          return False
   return True 
 

class Testing(unittest.TestCase):
    a1="HeloWorld"
    a2="HelloWorld"
    b1="HelloWorld"
    b2="WorldHello"
    c1="WorldHello"
    c2="WrldHello"
    
    def test_case1(self):
       self.assertFalse(isstringsame(self.a1,self.a2))
    def test_case2(self):
       self.assertTrue(isstringsame(self.b1,self.b2))
    def test_case3(self):
       self.assertFalse(isstringsame(self.c1,self.c2))


if __name__=='__main__':
   unittest.main()
