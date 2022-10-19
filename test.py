import unittest 
from palindromos import palindromo


class PalindromoTest(unittest.TestCase):    
    def test_anna(self):
        self.assertEqual(palindromo('anna'),True)
          

    def test_tini(self): 
        self.assertEqual(palindromo('tini'),False)
    

if __name__ == '__main__':
    unittest.main()
