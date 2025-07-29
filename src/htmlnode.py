from __future__ import annotations
from typing import Optional


class HTMLNode:
    def __init__(self, 
            tag: Optional[str] = None, 
            value: Optional[str] = None, 
            children: Optional[list[HTMLNode]] = None, 
            props: Optional[dict] = None):
        
        self.tag = tag
        self.value = value
        self.children: list[HTMLNode] = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        if self.tag is None:
            return self.value if self.value else ""
        
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        content = ""
        if self.value:
            content += self.value
        if self.children:
            content += "".join([child.to_html() for child in self.children])
        closing_tag = f"</{self.tag}>"

        return opening_tag + content + closing_tag
    
    def props_to_html(self):
        if self.props:
             return " " + " ".join([f'{key}="{value}"'for key, value in self.props.items()])
        return ""
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, 
                 tag: Optional[str], 
                 value: str = "", 
                 props: Optional[dict] = None):
        
        super().__init__(tag=tag, value=value, props=props)

    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return str(self.value)
        props_str = ""
        if self.props:
            props_str = " " + " ".join([f'{key}="{value}"'for key, value in self.props.items()])
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: Optional[dict] = None):
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