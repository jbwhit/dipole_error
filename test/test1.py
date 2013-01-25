#!/usr/bin/env python

import unittest


class MyClassTest(unittest.TestCase):
    def test_creation(self):
        """Tests that the class can be created."""
        my_obj = myclass.MyClass()
        self.assert_(my_obj)
    
    def test_genfn(self):
        """tests length of of output."""
        res = genfn()
        self.assert_(len(res) == 32, 'generated string = "%s"' % res)
    
if __name__ == "__main__":
    unittest.main()
    
# assertEqual(a, b)
# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)