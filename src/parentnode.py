from typing import Optional
from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props:Optional[dict]= None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError(f"ParentNode must have a tag value")
        if not self.children:
            raise ValueError(f"ParentNode must have a children value")
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        children_html = "".join([child.to_html() for child in self.children])
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{children_html}{closing_tag}"
    
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