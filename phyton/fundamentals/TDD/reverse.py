import unittest
class Testing(unittest.TestCase):
    def test_list1(self):
        a = [1, 2, 4, 3, 5]
        b = [1, 2, 4, 3, 5]
        self.assertEqual(a, b)
    def test_list2(self):
        seqList = [1, 2, 4, 3, 5]
        ot=(list(reversed(seqList)))
        self.assertNotEqual(ot,seqList)
    def test_list3(self):
        seqList = [5,3,1]
        ot=(list(reversed(seqList)))
        self.assertNotEqual(seqList,ot)

if __name__ == '__main__':
    unittest.main()
