# -*- coding: utf-8 -*-

"""
Unit-Tests for module main
"""

import unittest
import main


class TestMain(unittest.TestCase):

    """Unittest class for module main"""

    def test_add(self):
        # assign
    
        # act
        s = main.add(1, 2)
    
        # assert
        self.assertEqual(s, 3) 


if __name__ == '__main__':
    unittest.main()
