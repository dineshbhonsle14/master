import unittest

def isunique(string):
   char_set=[False for _ in range(128)] 
   for chr in string:
      val=ord(chr)
      if char_set[val] is False:
          char_set[val]=True
      else:
          print "{} {}".format(chr,char_set[val])
          return False
      print "{} {}".format(chr,char_set[val])
   return True


class Test(unittest.TestCase):
   dataT=[('helo'),('dinesh')]
   dataF=['hello','dineshh']

   def test_1(self):
      for test_string in self.dataT:
           tres=isunique(test_string)
           self.assertTrue(tres)

   def test_2(self):
      for test_string in self.dataF:
           tres=isunique(test_string)
           self.assertFalse(tres)

if __name__=='__main__':
   unittest.main()
