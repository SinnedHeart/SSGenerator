import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_no_tag(self):
        node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_no_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_mixed_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "bold!"),
                ParentNode("span", [LeafNode(None, "nested leaf")]),
                LeafNode(None, "plain"),
            ],
        )
        self.assertEqual(
            node.to_html(), "<p><b>bold!</b><span>nested leaf</span>plain</p>"
        )