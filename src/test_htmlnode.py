import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):

    def test_props_to_html_with_props(self):
        node = HTMLNode("a", "click me", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "hello", None, {}) # empty props
        result = node.props_to_html()
        expected = "" # should return empty string
        self.assertEqual(result, expected)
    
    def test_props_to_html_single_prop(self):
        node = HTMLNode("img", None, None, {"src": "image.jpg"})
        result = node.props_to_html()
        expected = ' src="image.jpg"'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()