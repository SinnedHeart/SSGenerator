from htmlnode import HTMLNode
from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return(self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
            return HTMLNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
            return HTMLNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
            return HTMLNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
            return HTMLNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("Link text nodes must have a URL") 
        return HTMLNode("a", text_node.text, props={"href": text_node.url})  
    if text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("Link text nodes must have a URL")
        return HTMLNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Unknown text type: {text_node.text_type}")