import unittest
from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url_present(self):
        node = TextNode("Check LINK", TextType.LINK, url="https://www.boot.dev/")
        node2 = TextNode("Check LINK", TextType.LINK) #Url default to None
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()