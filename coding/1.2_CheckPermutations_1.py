import unittest
def isstringsame(string1,string2):
   if len(string1) != len(string2):
      return False
   l1=[0 for _ in range(128)] 
   l2=[0 for _ in range(128)] 
   #[l1[ord(chr)]=l1[ord(chr)]+1  for chr in string1]
   #[l2[ord(chr)]=l2[ord(chr)]+1  for chr in string2]
   l1=[l1[ord(chr)]+1  for chr in string1]
   l2=[l2[ord(chr)]+1  for chr in string2]
   
   if cmp(l1,l2) is not 0:
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
       self.assertTrue(isstringsame(self.a1,self.a2))
    def test_case2(self):
       self.assertTrue(isstringsame(self.b1,self.b2))
    def test_case3(self):
       self.assertFalse(isstringsame(self.c1,self.c2))


if __name__=='__main__':
   unittest.main()
