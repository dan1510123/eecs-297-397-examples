import timeout_decorator
import unittest
from assignment3 import store_checkout as sc
from assignment3 import highest_frequency_count as hfc

class TestStringMethods(unittest.TestCase):

    def test_both_empty(self):
        self.assertEqual(0, sc([], []))
    
    def test_empty_inventory(self):
        self.assertEqual(0, sc([], ["a"]))

    def test_empty_items(self):
        self.assertEqual(0, sc([("a", 1, ".")], []))

    def test_one_inventory_one_purchase(self):
        self.assertEqual(11, sc([("a", 11, '.')], ["a"]))

    def test_one_inventory_multiple_purchase(self):
        self.assertEqual(22, sc([("a", 11, '.')], ["a", "a", "c"]))

    def test_multiple_inventory_multiple_purchase(self):
        self.assertEqual(26, sc([("a", 11, '.'), ("c", 4, '.')], ["a", "a", "c"]))
    
    @timeout_decorator.timeout(10)
    def test_large_inputs(self):
        self.assertEqual(5_000_050_000, sc([(str(i), i, str(i)) for i in range(1, 100_001)], [str(i) for i in range(1, 100_001)]))


    def test_empty_word_count(self):
        self.assertEqual(0, hfc([]))

    def test_one_word(self):
        self.assertEqual(1, hfc(["a"]))

    def test_one_word_multiple_times(self):
        self.assertEqual(2, hfc(["a", "a"]))

    def test_multiple_words(self):
        self.assertEqual(2, hfc(["a", "a", "b"]))

    def test_tie_for_most(self):
        self.assertEqual(2, hfc(["a", "a", "b", "b", "c"]))


    @timeout_decorator.timeout(10)
    def test_large_count(self):
        test_list = [str(i) for i in range(100_000)]
        test_list.append("A")
        test_list.append("A")

        self.assertEqual(2, hfc(test_list))

if __name__ == '__main__':
    unittest.main()
