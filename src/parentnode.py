from typing import Optional
from htmlnode import HTMLNode

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