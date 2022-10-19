
def palindromo (palabra): 
    for i in range(0,int (len(palabra))):
        if palabra [i] !=palabra[-i-1]: 
            return False
        return True 

import unittest 
class PalindromoTest(unittest.TestCase):    
    def test_anna(self):
        self.assertEqual(palindromo('anna'),True)
          

    def test_tini(self): 
        self.assertEqual(palindromo('tini'),False)
    

if __name__ == '__main__':
    unittest.main()
