import Main
import unittest

class Test_Main(unittest.TestCase):
    def test_string_reverser(self):
        result=Main.string_reverser("Hello")
        self.assertEqual(result, "olleH")
    def test_word_counter(self):
        result=Main.word_counter("Hi I read in class 6")
        self.assertEqual(result, 6)
if __name__=="__main__":
    unittest.main()