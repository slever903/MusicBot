import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from musicbot.utils import avg

class Utils_Test(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(avg([1,5]), 3)

if __name__ == '__main__':
    unittest.main()