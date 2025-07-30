import unittest
from generate_content import extract_title

class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):
        node = extract_title("# Hello")
        expected = "Hello"
        self.assertEqual(node, expected)

if __name__ == "__main__":
    unittest.main()
