
import unittest
from solution import Solution  

class TestMergeAlternately(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()  

    def test_equal_length_strings(self):
        self.assertEqual(self.solution.mergeAlternately("abc", "xyz"), "axbycz")
    
    def test_word1_longer(self):
        self.assertEqual(self.solution.mergeAlternately("abcde", "xyz"), "axbyczde")
    
    def test_word2_longer(self):
        self.assertEqual(self.solution.mergeAlternately("abc", "wxyz"), "awbxcyz")
    
    def test_empty_word1(self):
        self.assertEqual(self.solution.mergeAlternately("", "xyz"), "xyz")
    
    def test_empty_word2(self):
        self.assertEqual(self.solution.mergeAlternately("abc", ""), "abc")
    
    def test_both_empty(self):
        self.assertEqual(self.solution.mergeAlternately("", ""), "")

    # Negative Test Cases
    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            self.solution.mergeAlternately(123, "abc")
        
        with self.assertRaises(TypeError):
            self.solution.mergeAlternately("abc", 456)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            self.solution.mergeAlternately(None, "abc")
        
        with self.assertRaises(TypeError):
            self.solution.mergeAlternately("abc", None)
    
    def test_special_characters(self):
        self.assertEqual(self.solution.mergeAlternately("a!@", "123"), "a1!2@3")

if __name__ == '__main__':
    unittest.main()
