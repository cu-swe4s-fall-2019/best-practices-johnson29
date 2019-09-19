import unittest
import math
import random
import numpy as np
import get_column_stats as g

class test_answers(unittest.TestCase):
    
    def test_mean(self):
        V = [5, 4, 0]
        self.assertEqual(g.getmean(V), 3)
        
    def test_SD(self):
        V = [5, 4, 0]
        self.assertAlmostEqual(g.getsd(V,3), 2.160246899)
        
    def test_Rmean(self):
        V = []
        for i in range(100):
            V.append(random.randint(1,100))
        self.assertEqual(g.getmean(V), sum(V)/len(V))
    
    def test_RSD(self):
        V = []
        for i in range(100):
            V.append(random.randint(1,100))
            m=sum(V)/len(V)
        self.assertEqual(g.getsd(V, m),math.sqrt(sum([(m-x)**2 for x in V]) / len(V)) )
    
    def test_empty(self):
        V = []
       # m = 0
        self.assertIsNone(g.getmean(V))
        
    def test_string(self):
        V = ['d', 'a']
        self.assertFalse(g.stringcheck(V))
        

    
if __name__ == '__main__':
    unittest.main()