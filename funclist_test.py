import unittest
from funclist import *

class TestFuncList(unittest.TestCase):

    def test_only_values_matching(self):
        pass


    def test_all_values_above(self):
        pass


    def test_apply_to_all(self):
        def mult_by_two(item):
            return item*2
        self.assertEqual(convert_to_funclist([2, 4, 6]), apply_to_all( convert_to_funclist([1, 2, 3]), mult_by_two))


    def test_mult_all(self):
        self.assertEqual(convert_to_funclist([2, 4, 6]), mult_all(convert_to_funclist([1, 2, 3]), 2))
        self.assertEqual(
            convert_to_funclist(["AAA", "zxzxzx", ""]), 
            mult_all(convert_to_funclist(["A", "zx", ""]), 3)
        )











    def test_convert_to_funclist(self):
        reglist = [1, 2, 3, 4]
        funclist = FuncList(1, FuncList(2, FuncList(3, FuncList(4,None))))

        self.assertEqual(funclist, convert_to_funclist(reglist))
        self.assertNotEqual(funclist.tail, convert_to_funclist(reglist))
        self.assertEqual(None, convert_to_funclist([]))
        self.assertEqual(FuncList(7, None), convert_to_funclist([7]))


    def test_convert_to_reglist(self):
        reglist = [1, 2, 3, 4]
        funclist = FuncList(1, FuncList(2, FuncList(3, FuncList(4,None))))

        self.assertEqual(reglist, convert_to_reglist(funclist))
        self.assertNotEqual([2, 3, 4], convert_to_reglist(funclist))
        self.assertEqual([], convert_to_reglist(None))
        self.assertEqual([7], convert_to_reglist(FuncList(7, None)))
        