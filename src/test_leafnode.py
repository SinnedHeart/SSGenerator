import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(value="Hello, world!", tag="p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode(value="Click here", tag="a", props={"href": "https://www.boot.dev/"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.boot.dev/">Click here</a>'
        )
    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_empty_props(self):
        node = LeafNode(value="Empty props", tag="div", props={})
        self.assertEqual(node.to_html(), "<div>Empty props</div>")
    
    def test_leaf_to_html_multiple_props(self):
        node = LeafNode(
            value="Click me!",
            tag="a",
            props={"href": "https://www.boot.dev/", "target": "_blank"}
        )
        # Because attribute order isn't guaranteed in Python dicts before 3.7,
        # this test may need to check that both attributes are present.
        result = node.to_html()
        self.assertTrue(result.startswith('<a'))
        self.assertIn('href="https://www.boot.dev/"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.endswith('>Click me!</a>'))
    
    def test_leaf_to_html_raises_on_none_value(self):
        node = LeafNode(value=None, tag="div")
        with self.assertRaises(ValueError):
            node.to_html()
        
if __name__ == "__main__":
    unittest.main()