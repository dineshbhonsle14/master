from collections import Counter
import unittest
def isPalindromePerm(mystring):
    """
      if at most 1 unique character occurs a non-multiple-of-2 times in the input,
      the output is True otherwise the output is False.
    """
    if not mystring and mystring.strip(): return False
    "remove white spaces"
    instr="".join(mystring.split())
    charstock=Counter()
    for letter in mystring:
         charstock[letter]+=1
    print charstock

    odd_count=0
    for count in charstock.values():
       odd_count += count % 2
    print odd_count
    # only one character should happen non multiple of 2 times.
    return odd_count in [0,1]


isPalindromePerm('12Hello world')
isPalindromePerm('abcddabc')
isPalindromePerm('aaaaaaaaaaaaaaaaa')


isPalindromePerm('Hello world')


class  UT(unittest.TestCase):
    
     #inp1='Hello World'
     inp1='abcxcba'
     inp2='abcdeabc'
     inp3='abcdddabc'
     inp4='abc  dddd   abc'

     def test_1(self):
          self.assertFalse(isPalindromePerm(self.inp1))
     def test_2(self):
          self.assertFalse(isPalindromePerm(self.inp2))
     def test_3(self):
          self.assertTrue(isPalindromePerm(self.inp3))
     def test_4(self):
          self.assertTrue(isPalindromePerm(self.inp4))
     

def suite1():
    suite=unittest.TestSuite()
    suite.addTest(UT('test_1'))
    suite.addTest(UT('test_2'))
    suite.addTest(UT('test_3'))
    suite.addTest(UT('test_4'))
    return suite

if __name__=='__main__':
   runner = unittest.TextTestRunner()
   runner.run(suite1())


